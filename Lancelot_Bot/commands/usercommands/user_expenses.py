from aiogram.types import Message
from storage.db_connection import get_connection

#--------------------------------------------------------------------------
# RU: Класс для работы с расходами пользователя
# EN: Class for working with user expenses
# PL: Klasa do pracy z wydatkami użytkownika

class UserExpensesCommands:

    #--------------------------------------------------------------------------
    # RU: Получение всех расходов из базы данных
    # EN: Get all expenses from the database
    # PL: Pobierz wszystkie wydatki z bazy danych

    @staticmethod
    def get_expenses_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(''' 
        SELECT date, category, amount, comment FROM expenses WHERE user_id = ? 
        ''', (user_id,))

        rows = cursor.fetchall()
        conn.close()

        expenses = []

        for row in rows:
            expense = {
                "date": row[0],
                "category": row[1],
                "amount": row[2],
                "comment": row[3]
            }
            expenses.append(expense)

        return expenses
    
    #--------------------------------------------------------------------------
    # RU: Получение расходов из базы данных по категории
    # EN: Get expenses from the database by category
    # PL: Pobierz wydatki z bazy danych według kategorii

    @staticmethod
    def get_expenses_from_db_by_category(user_id, category):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(''' 
        SELECT date, category, amount, comment FROM expenses WHERE user_id = ? AND category = ? 
        ''', (user_id, category))

        rows = cursor.fetchall()
        conn.close()

        expenses = []

        for row in rows:
            expense = {
                "date": row[0],
                "category": row[1],
                "amount": row[2],
                "comment": row[3]
            }
            expenses.append(expense)

        return expenses