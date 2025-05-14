from aiogram.types import  CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from config.states import BalanceStates

from user_interface.keyboards_folder.keyboards_folder.expenses import *

from commands.usercommands.user_info import UserInfoCommands
from commands.botcommands_folder.translation import BotTranslations
from commands.usercommands.user_expenses import UserExpensesCommands

router = Router()

#--------------------------------------------------------------------------
# RU: Класс для отображения расходов пользователя
# EN: Class for displaying user's expenses
# PL: Klasa do wyświetlania wydatków użytkownika


class BotShowexpensesStates:

    #--------------------------------------------------------------------------
    # RU: Показать все расходы
    # EN: Show all expenses
    # PL: Pokaż wszystkie wydatki

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_expense, F.data == "show_all_expenses")
    async def show_all_expenses(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()
        user_id = str(callback.from_user.id)
        expenses = UserExpensesCommands.get_expenses_from_db(user_id)

        expense_category_translator = await BotTranslations.open_menu(
            callback.from_user.id,
            expense_category_translator_ru,
            expense_category_translator_eng,
            expense_category_translator_pl
        )
        all_amount = sum(exp["amount"] for exp in expenses)
        expenses_text_result = "".join([
            (await BotTranslations.translate(user_id, "expense_details")).format(
                amount=exp["amount"],
                category=expense_category_translator.get(exp["category"]),
                date=exp["date"],
                comment=exp["comment"]
            )
            for exp in expenses
        ])
        text = (await BotTranslations.translate(user_id, "show_expense")).format(
            expenses_text_result=expenses_text_result,
            all_amount=all_amount
        )

        await callback.message.answer(text)
        await state.clear()

    #--------------------------------------------------------------------------
    # RU: Ожидание выбора категории для показа расходов
    # EN: Waiting for category selection to show expenses
    # PL: Oczekiwanie na wybór kategorii wydatków

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_expense, F.data == "show_category_expenses")
    async def waiting_for_expense_category(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()
        user_id = UserInfoCommands.get_user_id(callback)

        text = await BotTranslations.translate(user_id, "waiting_for_show_expense_category")
        expense_category_keyboard = await BotTranslations.open_menu(
            callback.from_user.id,
            expense_category_keyboard_ru,
            expense_category_keyboard_eng,
            expense_category_keyboard_pl
        )

        await callback.message.answer(text, reply_markup=expense_category_keyboard)
        await state.set_state(BalanceStates.waiting_for_show_expense_category)

    #--------------------------------------------------------------------------
    # RU: Показать расходы по выбранной категории
    # EN: Show expenses for selected category
    # PL: Pokaż wydatki według wybranej kategorii

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_expense_category, F.data.startswith("cat_"))
    async def show_expense_category(callback: CallbackQuery, state: FSMContext):
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()

        user_id = UserInfoCommands.get_user_id(callback)
        category = callback.data.replace("cat_", "")
        expenses = UserExpensesCommands.get_expenses_from_db_by_category(user_id, category)

        expense_category_translator = await BotTranslations.open_menu(
            callback.from_user.id,
            expense_category_translator_ru,
            expense_category_translator_eng,
            expense_category_translator_pl
        )
        all_amount = sum(exp["amount"] for exp in expenses)
        expenses_text_result = "".join([
            (await BotTranslations.translate(user_id, "expense_details")).format(
                amount=exp["amount"],
                category=expense_category_translator.get(exp["category"]),
                date=exp["date"],
                comment=exp["comment"]
            )
            for exp in expenses
        ])
        text = (await BotTranslations.translate(user_id, "show_expense")).format(
            expenses_text_result=expenses_text_result,
            all_amount=all_amount
        )

        await callback.message.answer(text)
        await state.clear()