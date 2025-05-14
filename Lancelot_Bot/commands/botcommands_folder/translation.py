from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

from config.states import BalanceStates
from storage.scripts.language_scripts import DbLanguageCommands
from commands.usercommands.user_info import UserInfoCommands

from user_interface.keyboards_folder.keyboards_folder.menu import Language_menu
from config.languages import ru,eng,pl

from user_interface.keyboards_folder.keyboards_folder.menu import main_menu_eng, main_menu_pl, main_menu_ru

#--------------------------------------------------------------------------

# RU: Класс для перевода и выбора языка
# EN: Class for translation and language selection
# PL: Klasa do tłumaczenia i wyboru języka

langs = {
    'ru': ru,
    'eng': eng,
    'pl': pl,
}

router = Router()

class BotTranslations:

    #--------------------------------------------------------------------------
    # RU: Отправка сообщения с выбором языка
    # EN: Send language selection message
    # PL: Wyślij wiadomość z wyborem języka

    @staticmethod
    async def chose_language(message: Message, state: FSMContext):
        await message.answer("Выбери язык:\nWybierz język:\nChoose a Language:", reply_markup=Language_menu)
        await state.set_state(BalanceStates.waiting_for_language)

    #--------------------------------------------------------------------------
    # RU: Перевод строки по ключу и языку пользователя
    # EN: Translate text string by user language and key
    # PL: Przetłumacz tekst według języka użytkownika i klucza

    @staticmethod
    async def translate(user_id: int, key: str, **kwargs):
        lang = UserInfoCommands.get_user_language(user_id) or 'ru'
        return langs.get(lang, ru).get(key, key)

    #--------------------------------------------------------------------------
    # RU: Выбор нужного меню в зависимости от языка
    # EN: Return correct menu based on user language
    # PL: Zwróć odpowiednie menu w zależności od języka użytkownika

    @staticmethod
    async def open_menu(user_id, ru_menu, eng_menu, pl_menu):
        lang = UserInfoCommands.get_user_language(user_id) or 'ru'
        if lang == "ru":
            return ru_menu
        elif lang == "eng":
            return eng_menu
        else:
            return pl_menu

    #--------------------------------------------------------------------------
    # RU: Сохранение выбранного языка пользователя
    # EN: Save the selected user language
    # PL: Zapisz wybrany język użytkownika

    @staticmethod
    @router.callback_query(BalanceStates.waiting_for_language)
    async def save_language(callback: CallbackQuery, state: FSMContext):
        user_id = callback.from_user.id
        result = callback.data.replace("lang_", "")

        DbLanguageCommands.chose_language(user_id, result)
        menu = await BotTranslations.open_menu(user_id, main_menu_ru, main_menu_eng, main_menu_pl)

        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer("...", reply_markup=menu)
        await state.clear()

    