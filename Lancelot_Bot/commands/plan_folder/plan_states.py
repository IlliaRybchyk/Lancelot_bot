from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from config.states import BalanceStates
from aiogram import Router, F

from user_interface.keyboards_folder.keyboards_folder.expenses import *
from user_interface.keyboards_folder.keyboards_folder.menu import yes_no_menu

from storage.scripts.plan_scripts import DbPlanCommands
from commands.botcommands_folder.translation import BotTranslations
from commands.usercommands.user_info import UserInfoCommands

router = Router()

#--------------------------------------------------------------------------
# RU: Класс для работы с состояниями при создании плана
# EN: Class for managing states when creating a plan
# PL: Klasa do zarządzania stanami przy tworzeniu planu

class BotPlanStates:

    #--------------------------------------------------------------------------
    # RU: Получение бюджета нового плана
    # EN: Get the budget for a new plan
    # PL: Uzyskiwanie budżetu dla nowego planu

    @staticmethod
    @router.message(BalanceStates.waiting_for_new_plan_amount)
    async def get_new_plan_amount(message: Message, state: FSMContext):
        errortext = await BotTranslations.translate(message.from_user.id, "amount_greater")
        valuerror = await BotTranslations.translate(message.from_user.id, "incorrect_amount")
        user_id = UserInfoCommands.get_user_id(message)

        try:
            amount = float(message.text.replace(",", "."))

            if amount <= 0:
                await message.answer(errortext)
                await state.clear()
                return

            await state.update_data(plane_amount=amount)

            text = await BotTranslations.translate(message.from_user.id, "waiting_for_plan_category")
            expense_category_keyboard = await BotTranslations.open_menu(
                message.from_user.id, 
                expense_category_keyboard_ru, 
                expense_category_keyboard_eng, 
                expense_category_keyboard_pl
            )

            await message.answer(text, reply_markup=expense_category_keyboard)
            await state.set_state(BalanceStates.waiting_for_new_plan_category)

        except ValueError: 
            await message.answer(valuerror)
            await state.clear() 

    #--------------------------------------------------------------------------
    # RU: Получение категории нового плана
    # EN: Getting the category for the new plan
    # PL: Pobieranie kategorii dla nowego planu

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_new_plan_category, F.data.startswith("cat_"))
    async def get_new_plan_category(callback: CallbackQuery, state: FSMContext):
        await callback.answer()
        await callback.message.edit_reply_markup(reply_markup=None)

        user_id = UserInfoCommands.get_user_id(callback)
        selected_category = callback.data.replace("cat_", "")
        data = await state.get_data()
        selected = data.get("selected_categories", [])
        text_selected = await BotTranslations.translate(user_id, "category_chosen")

        if selected_category in selected:
            await callback.message.answer(text_selected)
            await state.clear()
            return

        await state.update_data(current_category=selected_category)

        expense_category_translator = await BotTranslations.open_menu(
            callback.from_user.id, 
            expense_category_translator_ru, 
            expense_category_translator_eng, 
            expense_category_translator_pl
        )
        translated_category = expense_category_translator.get(selected_category)
        text = (await BotTranslations.translate(callback.from_user.id, "waiting_for_plan_category_amount")).format(
            translated_category=translated_category
        )

        await callback.message.answer(text)
        await state.set_state(BalanceStates.waiting_for_new_plan_category_amount)

    #--------------------------------------------------------------------------
    # RU: Получение суммы категории нового плана
    # EN: Getting the amount for the new plan category
    # PL: Pobieranie kwoty dla kategorii nowego planu

    @staticmethod
    @router.message(BalanceStates.waiting_for_new_plan_category_amount)
    async def get_new_plan_category_amount(message: Message, state: FSMContext):
        error_text = await BotTranslations.translate(message.from_user.id, "amount_greater")
        valueerror = await BotTranslations.translate(message.from_user.id, "incorrect_amount")
        user_id = UserInfoCommands.get_user_id(message)
        try:
            amount = float(message.text.replace(",", "."))

            if amount <= 0:
                await message.answer(error_text)
                await state.clear()
                return
            
            data = await state.get_data()
            current_category = data["current_category"]
            category_plan = data.get("category_plan", {})
            category_plan[current_category] = amount
            selected = data.get("selected_categories", [])
            selected.append(current_category)

            await state.update_data(category_plan=category_plan, selected_categories=selected)
            expense_category_translator = await BotTranslations.open_menu(
                message.from_user.id, 
                expense_category_translator_ru, 
                expense_category_translator_eng, 
                expense_category_translator_pl
            )
            translated = [
                        f"{expense_category_translator.get(cat)} — {category_plan[cat]}"
                        for cat in selected
                        ]
            
            text1 = await BotTranslations.translate(message.from_user.id, "show_chosen_categories") + "\n".join(translated)
            text2 = await BotTranslations.translate(message.from_user.id, "chose_another_category")
            
            await message.answer(text1)
            await message.answer(text2, reply_markup=yes_no_menu)
            await state.set_state(BalanceStates.confirm_new_plan_category)

        except ValueError:
            await message.answer(valueerror)
            await state.clear()

    #--------------------------------------------------------------------------
    # RU: Добавление новой категории в план
    # EN: Adding a new category to the plan
    # PL: Dodawanie nowej kategorii do planu

    @staticmethod
    @router.callback_query(BalanceStates.confirm_new_plan_category, F.data == "yes")
    async def add_another_category(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()
        user_id = UserInfoCommands.get_user_id(callback)

        text = await BotTranslations.translate(user_id, "waiting_for_plan_new_category")
        expense_category_keyboard = await BotTranslations.open_menu(
            callback.from_user.id,
            expense_category_keyboard_ru,
            expense_category_keyboard_eng,
            expense_category_keyboard_pl
        )
        await callback.message.answer(text, reply_markup=expense_category_keyboard)
        await state.set_state(BalanceStates.waiting_for_new_plan_category)

   #--------------------------------------------------------------------------
    # RU: Финальное создание плана и сохранение в базу
    # EN: Finalizing the plan and saving it to the database
    # PL: Finalizacja planu i zapisanie go do bazy danych

    @staticmethod
    @router.callback_query(BalanceStates.confirm_new_plan_category, F.data == "no")
    async def finalize_new_plan(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()

        user_id = callback.from_user.id
        data = await state.get_data()
        plane_amount = data.get("plane_amount")
        category_plan = data.get("category_plan", {})

        expense_category_translator = await BotTranslations.open_menu(
            user_id,
            expense_category_translator_ru,
            expense_category_translator_eng,
            expense_category_translator_pl
        )

        summary_lines = []
        total = 0
        for cat, amount in category_plan.items():
            translated = expense_category_translator.get(cat)
            summary_lines.append(f"{translated} — {amount}")
            total += amount
            DbPlanCommands.add_categories_to_db(cat, user_id, amount)
            

        summary = "\n".join(summary_lines)
        remaining_amount = plane_amount - total

        DbPlanCommands.add_budget_to_db(user_id, plane_amount, remaining_amount)

        text = (await BotTranslations.translate(user_id, "confirm_plan")).format(
            plane_amount=plane_amount,
            summary=summary,
            total=total,
            remaining_amount=remaining_amount
        )
        await callback.message.answer(text)
        await state.clear()