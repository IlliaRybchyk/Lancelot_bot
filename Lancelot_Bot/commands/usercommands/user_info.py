from aiogram.types import Message, CallbackQuery
from storage.db_connection import get_connection
from typing import Union

#--------------------------------------------------------------------------
# RU: Класс для работы с информацией пользователя
# EN: Class for working with user information
# PL: Klasa do pracy z informacjami użytkownika

class UserInfoCommands:

    #--------------------------------------------------------------------------
    # RU: Получение id пользователя из Message или CallbackQuery
    # EN: Get user id from Message or CallbackQuery
    # PL: Pobieranie id użytkownika z Message lub CallbackQuery

    @staticmethod
    def get_user_id(data: Union[Message, CallbackQuery]):
        if isinstance(data, Message):
            return str(data.from_user.id)
        elif isinstance(data, CallbackQuery):
            return str(data.from_user.id)
    
    #--------------------------------------------------------------------------
    # RU: Получение языка пользователя из базы данных
    # EN: Get user language from the database
    # PL: Pobieranie języka użytkownika z bazy danych

    @staticmethod
    def get_user_language(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
        SELECT language FROM languages WHERE user_id = ? 
        ''', (user_id,))

        row = cursor.fetchone()
        conn.close()

        #--------------------------------------------------------------------------
        # RU: Если язык не найден, по умолчанию возвращается русский
        # EN: If language is not found, return Russian by default
        # PL: Jeśli język nie jest znaleziony, domyślnie zwróć rosyjski

        if row is None:
            return "ru"

        return row[0]