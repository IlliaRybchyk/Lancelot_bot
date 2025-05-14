from aiogram.types import Message
from storage.db_connection import get_connection

#--------------------------------------------------------------------------
# RU: Класс для работы с балансом пользователя
# EN: Class for working with user balance
# PL: Klasa do pracy z saldem użytkownika

class UserBalanceCommands:

    #--------------------------------------------------------------------------
    # RU: Получение баланса пользователя из базы данных
    # EN: Get user balance from the database
    # PL: Pobierz saldo użytkownika z bazy danych

    @staticmethod
    def get_user_balance_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(''' 
        SELECT amount FROM balances WHERE user_id = ? 
        ''', (user_id,))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return row[0]