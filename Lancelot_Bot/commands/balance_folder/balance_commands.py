from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config.states import BalanceStates
from aiogram import Router
from commands.usercommands.user_info import UserInfoCommands
from commands.usercommands.user_balance import UserBalanceCommands
from commands.botcommands_folder.translation import BotTranslations

from storage.scripts.balance_scripts import DbBalanceCommands

router = Router()

#--------------------------------------------------------------------------
# RU: Класс для команд, работающих с балансом
# EN: Class for balance management commands
# PL: Klasa dla poleceń zarządzających balansem

class BotBalanceCommands:

    #--------------------------------------------------------------------------
    # RU: Ожидание ввода суммы для создания баланса
    # EN: Waiting for balance amount input
    # PL: Oczekiwanie na wprowadzenie kwoty do stworzenia salda
    
    @staticmethod
    async def open_balance_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        text = await BotTranslations.translate(user_id, "waiting_for_new_balance_amount")

        await message.answer(text)
        await state.set_state(BalanceStates.waiting_for_balance)

    #--------------------------------------------------------------------------
    # RU: Отображение текущего баланса пользователя
    # EN: Displaying the current balance of the user
    # PL: Wyświetlanie bieżącego salda użytkownika
    
    @staticmethod
    async def show_balance_handler(message: Message):
        user_id = UserInfoCommands.get_user_id(message)
        balance = UserBalanceCommands.get_user_balance_from_db(user_id)
        balance_none_text = await BotTranslations.translate(message.from_user.id, "not_balance")

        if balance is None:
            await message.answer(balance_none_text)
            return

        text = (await BotTranslations.translate(message.from_user.id, "show_balance")).format(balance=balance)
        await message.answer(text)

    #--------------------------------------------------------------------------
    # RU: Удаление баланса пользователя
    # EN: Deleting the user's balance
    # PL: Usuwanie salda użytkownika
    
    @staticmethod
    async def delete_balance_handler(message: Message):
        user_id = UserInfoCommands.get_user_id(message)

        DbBalanceCommands.delete_balance(user_id)
        text = await BotTranslations.translate(user_id, "balance_deleted")
        await message.answer(text)