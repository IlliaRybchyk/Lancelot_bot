from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from config.states import BalanceStates
from storage.scripts.balance_scripts import DbBalanceCommands
from storage.scripts.top_ups_scripts import DbTopUpsCommand

from user_interface.keyboards_folder.keyboards_folder.top_ups import *

from aiogram import Router, F
from commands.usercommands.user_info import UserInfoCommands
from commands.botcommands_folder.translation import BotTranslations

router = Router()

#--------------------------------------------------------------------------
# RU: Класс состояний бота для обработки пополнений баланса
# EN: Bot state class for handling balance top-ups
# PL: Klasa stanów bota do obsługi doładowań salda


class BotTopUpsStates:

    #--------------------------------------------------------------------------
    # RU: Ожидание суммы пополнения баланса -> Ожидание категории пополнения
    # EN: Waiting for top-up amount -> Waiting for top-up category
    # PL: Oczekiwanie na kwotę doładowania -> Oczekiwanie na kategorię doładowania

    @staticmethod
    @router.message(BalanceStates.waiting_for_top_up)
    async def get_amount(message: Message, state: FSMContext):

        user_id = UserInfoCommands.get_user_id(message)
        
        value_error = await BotTranslations.translate(user_id, "incorrect_amount")
        greater_amount = await BotTranslations.translate(user_id, "amount_greater")
        waiting_for_category_text = await BotTranslations.translate(user_id, "waiting_for_top_up_category")

        top_ups_category_keyboard = await BotTranslations.open_menu(
            user_id, 
            top_ups_category_keyboard_ru, 
            top_ups_category_keyboard_eng, 
            top_ups_category_keyboard_pl
        )

        try:
            amount = float(message.text.replace(",", "."))

            if amount <= 0:
                await message.answer(greater_amount)
                await state.clear()
                return

            await state.update_data(amount=amount)
            await message.answer(waiting_for_category_text, reply_markup=top_ups_category_keyboard)
            await state.set_state(BalanceStates.waiting_for_top_up_category)

        except ValueError:
            await message.answer(value_error)
            await state.clear()

    #--------------------------------------------------------------------------
    # RU: Ожидание категории пополнения баланса -> Сохранение баланса
    # EN: Waiting for top-up category -> Saving top-up
    # PL: Oczekiwanie na kategorię doładowania -> Zapis doładowania

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_top_up_category, F.data.startswith("cat_"))
    async def get_category(callback: CallbackQuery, state: FSMContext):
        category = callback.data.replace("cat_", "") 
        user_id = UserInfoCommands.get_user_id(callback)
        waiting_for_comment_text = await BotTranslations.translate(user_id, "waiting_for_top_up_comment")

        await state.update_data(category=category)
        
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer(waiting_for_comment_text)
        await state.set_state(BalanceStates.waiting_for_top_up_comment)

    #--------------------------------------------------------------------------
    # RU: Ожидание комментария к пополнению и сохранение
    # EN: Waiting for top-up comment and saving
    # PL: Oczekiwanie na komentarz doładowania i zapis

    @staticmethod
    @router.message(BalanceStates.waiting_for_top_up_comment)
    async def save_top_up(message: Message, state: FSMContext):

        user_id = UserInfoCommands.get_user_id(message)
        user_data = await state.get_data()

        amount = user_data.get("amount")
        category = user_data.get("category")
        commentary = message.text

        DbBalanceCommands.top_up_balance(user_id, amount)
        DbTopUpsCommand.add_top_ups_to_db(user_id, amount, category, commentary)

        top_ups_category_translator = await BotTranslations.open_menu(
            message.from_user.id, 
            top_ups_category_translator_ru, 
            top_ups_category_translator_eng, 
            top_ups_category_translator_pl
        )
        confirm_text = (await BotTranslations.translate(message.from_user.id, "confirm_top_up")).format(
            amount=amount,
            category=top_ups_category_translator.get(category),
            commentary=commentary
        )

        await message.answer(confirm_text)
        await state.clear()