from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from config.states import BalanceStates

from user_interface.keyboards_folder.keyboards_folder.top_ups import *
from commands.botcommands_folder.translation import BotTranslations

from aiogram import Router, F
from commands.usercommands.user_info import UserInfoCommands
from commands.usercommands.user_top_ups import UserTopUpsCommands

router = Router()
"no_top_ups_in_category"
#--------------------------------------------------------------------------
# RU: Класс для обработки отображения пополнений
# EN: Class for handling top-up display
# PL: Klasa do obsługi wyświetlania doładowań
    
class BotShowTopUpsStates:
    
    #--------------------------------------------------------------------------
    # RU: Отображение всех пополнений
    # EN: Show all top-ups
    # PL: Pokaż wszystkie doładowania

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_top_up, F.data =="show_all_top_ups")
    async def show_all_top_ups(callback: CallbackQuery, state: FSMContext):

        await callback.message.edit_reply_markup(reply_markup=None)
        user_id = str(callback.from_user.id)
        top_ups = UserTopUpsCommands.get_top_ups_from_db(user_id)

        if not top_ups:
            text = await BotTranslations.translate(user_id, "not_top_up")
            await callback.message.answer(text)
            await state.clear()
            return

        top_ups_category_translator = await BotTranslations.open_menu(user_id, top_ups_category_translator_ru, top_ups_category_translator_eng, top_ups_category_translator_pl)
        top_ups_text = "\n".join([
            (await BotTranslations.translate(user_id, "show_all_top_up")).format(
                amount=topup['amount'],
                category_name=top_ups_category_translator.get(topup["category"]),
                date=topup["date"],
                comment=topup["comment"]
            ) for topup in top_ups
        ])
        all_amount = sum(topup['amount'] for topup in top_ups)

        text = (await BotTranslations.translate(user_id, "show_top_ups")).format(
            top_ups_text=top_ups_text,
            all_amount=all_amount
        )

        await callback.message.answer(text)
        await state.clear()
        await callback.answer()

    #--------------------------------------------------------------------------
    # RU: Ожидание категории отображения пополнений
    # EN: Waiting for top-up category display
    # PL: Oczekiwanie na kategorię doładowania

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_top_up, F.data == "show_category_top_ups")
    async def waiting_for_show_category_top_ups(callback: CallbackQuery, state: FSMContext):

        await callback.message.edit_reply_markup(reply_markup=None)
        user_id = UserInfoCommands.get_user_id(callback)

        text = await BotTranslations.translate(callback.from_user.id, "waiting_for_show_top_up_category")
        top_ups_category_keyboard = await BotTranslations.open_menu(
            callback.from_user.id, 
            top_ups_category_keyboard_ru, 
            top_ups_category_keyboard_eng, 
            top_ups_category_keyboard_pl
        )

        await callback.message.answer(text, reply_markup=top_ups_category_keyboard)
        await callback.answer()
        await state.set_state(BalanceStates.waiting_for_show_top_up_category)

    #--------------------------------------------------------------------------
    # RU: Отображение пополнений по категориям
    # EN: Display top-ups by category
    # PL: Wyświetlanie doładowań według kategorii

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_show_top_up_category, F.data.startswith("cat_"))
    async def show_top_up_by_category(callback: CallbackQuery, state: FSMContext):

        await callback.message.edit_reply_markup(reply_markup=None)
        user_id = str(callback.from_user.id)
        category = callback.data.replace("cat_", "")

        top_ups = UserTopUpsCommands.get_top_ups_from_db_by_category(user_id, category)

        if not top_ups:
            text = await BotTranslations.translate(callback.from_user.id, "not_top_up")
            await callback.message.answer(text)
            return

        result_text = ""
        all_amount = 0
        top_ups_category_translator = await BotTranslations.open_menu(
            callback.from_user.id, 
            top_ups_category_translator_ru, 
            top_ups_category_translator_eng, 
            top_ups_category_translator_pl
        )

        top_ups_text = "\n".join([
            (await BotTranslations.translate(callback.from_user.id, "show_all_top_up")).format(
                amount=topup['amount'],
                category_name=top_ups_category_translator.get(topup["category"]),
                date=topup["date"],
                comment=topup["comment"]
            )
            for topup in top_ups
        ])

        all_amount = sum(topup['amount'] for topup in top_ups)


        text = (await BotTranslations.translate(callback.from_user.id, "show_top_ups")).format(
            top_ups_text=top_ups_text,
            all_amount=all_amount
        )

        await callback.message.answer(text)
        await callback.answer()
        await state.clear()