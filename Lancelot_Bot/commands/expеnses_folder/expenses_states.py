from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from datetime import date

from config.states import BalanceStates

from user_interface.keyboards_folder.keyboards_folder.expenses import *

from commands.usercommands.user_plan import UserPlanCommands
from commands.usercommands.user_plan import UserPlanCommands
from commands.botcommands_folder.translation import BotTranslations
from commands.usercommands.user_info import UserInfoCommands

from storage.scripts.balance_scripts import DbBalanceCommands
from storage.scripts.expenses_scripts import DbExpensesCommands
from storage.scripts.plan_scripts import DbPlanCommands


router = Router()

#--------------------------------------------------------------------------
# RU: Класс состояний для добавления расхода
# EN: State class for adding an expense
# PL: Klasa stanów do dodawania wydatku

class BotExpensesStates:

    #--------------------------------------------------------------------------
    # RU: Получение суммы расхода
    # EN: Receiving the expense amount
    # PL: Odbieranie kwoty wydatku

    @staticmethod
    @router.message(BalanceStates.waiting_for_expense_amount)
    async def get_amount(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        error_text = await BotTranslations.translate(user_id, "expense_greater")
        value_error_text = await BotTranslations.translate(user_id, "incorrect_amount")
        try:

            amount = float(message.text.replace(",", "."))
            if amount <= 0:
                await message.answer(error_text)
                await state.clear()
                return

            await state.update_data(amount=amount)

            text = await BotTranslations.translate(user_id, "waiting_for_expense_category")
            expense_category_keyboard = await BotTranslations.open_menu(
                message.from_user.id,
                expense_category_keyboard_ru,
                expense_category_keyboard_eng,
                expense_category_keyboard_pl
            )
            await message.answer(text, reply_markup=expense_category_keyboard)
            await state.set_state(BalanceStates.waiting_for_expense_category)

        except ValueError:
            await message.answer(value_error_text)
            await state.clear()

    #--------------------------------------------------------------------------
    # RU: Получение категории расхода
    # EN: Receiving the expense category
    # PL: Odbieranie kategorii wydatku

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_expense_category, F.data.startswith("cat_"))
    async def get_category(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()
        user_id = UserInfoCommands.get_user_id(callback)
        category = callback.data.replace("cat_", "")

        await state.update_data(category=category)

        text = await BotTranslations.translate(callback.from_user.id, "waiting_for_expense_commentary")

        await callback.message.answer(text)
        await state.set_state(BalanceStates.waiting_for_expenses_commentary)

    #--------------------------------------------------------------------------
    # RU: Получение комментария и сохранение расхода
    # EN: Receiving comment and saving the expense
    # PL: Odbieranie komentarza i zapisywanie wydatku

    @staticmethod
    @router.message(BalanceStates.waiting_for_expenses_commentary)
    async def get_commentary(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        user_data = await state.get_data()

        amount = user_data.get("amount")
        category = user_data.get("category")
        commentary = message.text

        DbBalanceCommands.expense_balance(user_id, amount)
        DbPlanCommands.expense_remaining_amount(amount, user_id, category)
        DbExpensesCommands.add_expense_to_db(
            user_id,
            date.today().strftime("%d/%m/%Y"),
            category,
            amount,
            commentary
        )
        remaining_budget = UserPlanCommands.get_plan_remaining_amount(user_id, category)
        expense_category_translator = await BotTranslations.open_menu(
            message.from_user.id,
            expense_category_translator_ru,
            expense_category_translator_eng,
            expense_category_translator_pl
        )
        text = (await BotTranslations.translate(user_id, "expense_saved")).format(
            amount=amount,
            category=expense_category_translator[category],
            commentary=commentary,
            remaining_budget=remaining_budget or "---"
        )

        await message.answer(text)
        await state.clear()