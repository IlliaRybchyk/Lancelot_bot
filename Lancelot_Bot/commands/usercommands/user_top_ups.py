from storage.db_connection import get_connection

#--------------------------------------------------------------------------
# RU: Класс пополнений пользователя
# EN: User top-ups class
# PL: Klasa doładowań użytkownika

class UserTopUpsCommands:

    #--------------------------------------------------------------------------
    # RU: Получение истории пополнений
    # EN: Getting top-up history
    # PL: Pobieranie historii doładowań

    @staticmethod
    def get_top_ups_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT date, amount, category, comment FROM top_ups WHERE user_id = ?
        ''', (user_id,))

        rows = cursor.fetchall()
        conn.close()

        expenses = []

        for row in rows:
            expense = {
                "date": row[0],
                "amount": row[1],
                "category": row[2],
                "comment": row[3]
            }
            expenses.append(expense)

        return expenses
    
    #--------------------------------------------------------------------------
    # RU: Получить историю пополнений по категории
    # EN: Get top-up history by category
    # PL: Pobieranie historii doładowań według kategorii

    @staticmethod
    def get_top_ups_from_db_by_category(user_id, category):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT date, amount, category, comment FROM top_ups WHERE user_id = ? AND category = ?
        ''', (user_id, category))

        rows = cursor.fetchall()
        conn.close()

        expenses = []

        for row in rows:
            expense = {
                "date": row[0],
                "amount": row[1],
                "category": row[2],
                "comment": row[3]
            }
            expenses.append(expense)

        return expenses