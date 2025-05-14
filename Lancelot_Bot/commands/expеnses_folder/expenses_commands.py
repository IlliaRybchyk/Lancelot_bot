from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram import Router

from commands.usercommands.user_info import UserInfoCommands

from commands.usercommands.user_balance import UserBalanceCommands
from commands.usercommands.user_expenses import UserExpensesCommands
from commands.botcommands_folder.translation import BotTranslations

from config.states import BalanceStates

from user_interface.keyboards_folder.keyboards_folder.expenses import *

from storage.scripts.expenses_scripts import DbExpensesCommands

router = Router()

#--------------------------------------------------------------------------
# RU: Класс команд по работе с расходами
# EN: Command class for handling expenses
# PL: Klasa komend do obsługi wydatków

class BotExpensesCommands:

    #--------------------------------------------------------------------------
    # RU: Обработка создания нового расхода
    # EN: Handle creating a new expense
    # PL: Obsługa tworzenia nowego wydatku

    @staticmethod
    async def open_expense_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        balance_none_text = await BotTranslations.translate(user_id, "not_balance")
        text = await BotTranslations.translate(user_id, "waiting_for_expense_amount")

        if not UserBalanceCommands.get_user_balance_from_db(user_id):
            await message.answer(balance_none_text)
            return

        await message.answer(text)
        await state.set_state(BalanceStates.waiting_for_expense_amount)

    #--------------------------------------------------------------------------
    # RU: Обработка показа истории расходов
    # EN: Handle showing expense history
    # PL: Obsługa wyświetlania historii wydatków

    @staticmethod
    async def show_expense_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        not_expenses = await BotTranslations.translate(message.from_user.id, "not_expenses")
        text = await BotTranslations.translate(message.from_user.id, "how_to_show_expenses")

        if not UserExpensesCommands.get_expenses_from_db(user_id):
            await message.answer(not_expenses)
            return

        show_expenses_keyboard = await BotTranslations.open_menu(
            message.from_user.id,
            show_expenses_keyboard_ru,
            show_expenses_keyboard_eng,
            show_expenses_keyboard_pl
        )

        await message.answer(text, reply_markup=show_expenses_keyboard)
        await state.set_state(BalanceStates.waiting_for_show_expense)

    #--------------------------------------------------------------------------
    # RU: Очистка истории расходов пользователя
    # EN: Clear user's expense history
    # PL: Wyczyść historię wydatków użytkownika

    @staticmethod
    async def clear_expense_handler(message: Message):
        user_id = UserInfoCommands.get_user_id(message)
        not_expense = await BotTranslations.translate(message.from_user.id, "not_expenses")
        text = await BotTranslations.translate(message.from_user.id, "clear_expenses_list")

        if not UserExpensesCommands.get_expenses_from_db(user_id):
            await message.answer(not_expense)
            return

        DbExpensesCommands.clear_user_expenses(user_id)
        
        await message.answer(text)