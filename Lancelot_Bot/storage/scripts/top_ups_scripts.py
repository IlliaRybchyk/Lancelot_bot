from storage.db_connection import get_connection
from datetime import date

#-------------------------------------------------------------------------- 
# RU: Создание класса команд с пополнениями базы данных
# EN: Class for database top-up commands
# PL: Klasa poleceń do bazy danych z doładowaniami

class DbTopUpsCommand:

    #-------------------------------------------------------------------------- 
    # RU: Добавление пополнений в базу данных
    # EN: Adding top-ups to the database
    # PL: Dodawanie doładowań do bazy danych

    @staticmethod
    def add_top_ups_to_db(user_id, amount, category, comment):
        conn = get_connection()
        cursor = conn.cursor()
        today = date.today().strftime("%d/%m/%Y")
        cursor.execute(''' 
        INSERT INTO top_ups (user_id, date, amount, category, comment) 
        VALUES(?, ?, ?, ?, ?)''', (user_id, today, amount, category, comment))
        conn.commit()
        conn.close()

    #-------------------------------------------------------------------------- 
    # RU: Очистка истории пополнений
    # EN: Clearing top-up history
    # PL: Czyszczenie historii doładowań

    @staticmethod
    def clear_user_top_ups(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM top_ups WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()