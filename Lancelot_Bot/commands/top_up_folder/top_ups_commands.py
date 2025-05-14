from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from config.states import BalanceStates
from aiogram import Router
from commands.usercommands.user_info import UserInfoCommands
from commands.usercommands.user_top_ups import UserTopUpsCommands
from commands.usercommands.user_balance import UserBalanceCommands
from commands.botcommands_folder.translation import BotTranslations

from storage.scripts.top_ups_scripts import DbTopUpsCommand
from user_interface.keyboards_folder.keyboards_folder.top_ups import *

router = Router()

#--------------------------------------------------------------------------
# RU: Класс для работы с пополнением баланса
# EN: Class for working with top-up balance
# PL: Klasa do pracy z doładowaniem salda

class BotTopUpCommands:

    #--------------------------------------------------------------------------

    #Пополнение баланса

    #--------------------------------------------------------------------------
    # RU: Обработчик команды пополнения баланса
    # EN: Handler for the balance top-up command
    # PL: Obsługa polecenia doładowania salda

    @staticmethod
    async def top_up_balance_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        
        if (UserBalanceCommands.get_user_balance_from_db
            (UserInfoCommands.get_user_id(message))) is None:
            text = await BotTranslations.translate(user_id, "not_balance")
            await message.answer(text)
            return

        text = await BotTranslations.translate(message.from_user.id, "waiting_for_top_up_amount")

        await message.answer(text)
        await state.set_state(BalanceStates.waiting_for_top_up)
        
    #--------------------------------------------------------------------------
    # RU: Обработчик показа истории пополнений
    # EN: Handler for showing top-up history
    # PL: Obsługa wyświetlania historii doładowań

    @staticmethod
    async def show_top_up_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)

        not_top_up = await BotTranslations.translate(user_id, "not_top_up")
        if not (UserTopUpsCommands.get_top_ups_from_db(user_id)):
            await message.answer(not_top_up)
            return

        text = await BotTranslations.translate(user_id, "waiting_for_show_top_ups_type")
        show_top_ups_keyboard = await BotTranslations.open_menu(
            message.from_user.id,
            show_top_ups_keyboard_ru,
            show_top_ups_keyboard_eng,
            show_top_ups_keyboard_pl
        )

        await message.answer(text, reply_markup=show_top_ups_keyboard)
        await state.set_state(BalanceStates.waiting_for_show_top_up)

    #--------------------------------------------------------------------------
    # RU: Очистка истории пополнений
    # EN: Clearing the top-up history
    # PL: Czyszczenie historii doładowań

    @staticmethod
    async def clear_top_ups_history(message: Message):
        user_id = UserInfoCommands.get_user_id(message)
        DbTopUpsCommand.clear_user_top_ups(user_id)
        text = await BotTranslations.translate(user_id, "clear_top_ups_list")
        await message.answer(text)