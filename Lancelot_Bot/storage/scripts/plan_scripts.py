from storage.db_connection import get_connection

#-------------------------------------------------------------------------- 
# RU: Создание класса работы с командами
# EN: Class for working with commands
# PL: Klasa do pracy z poleceniami

class DbPlanCommands:

    #-------------------------------------------------------------------------- 
    # RU: Добавить новый бюджет в бд
    # EN: Add new budget to the database
    # PL: Dodaj nowy budżet do bazy danych

    @staticmethod
    def add_budget_to_db(user_id, total_amount, remaining_amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
        INSERT INTO budgets (user_id, total_amount, remaining_amount) 
        VALUES(?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE 
        SET total_amount = excluded.total_amount, 
            remaining_amount = excluded.remaining_amount
        ''', (user_id, total_amount, remaining_amount))
        conn.commit()
        conn.close()

    #-------------------------------------------------------------------------- 
    # RU: Добавить новую категорию в бд
    # EN: Add new category to the database
    # PL: Dodaj nową kategorię do bazy danych

    @staticmethod
    def add_categories_to_db(name, user_id ,amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
        INSERT INTO categories (name, user_id, amount, remaining_amount) 
        VALUES(?, ?, ?, ?)
        ON CONFLICT(name, user_id) DO UPDATE 
        SET name = excluded.name
        ''', (name, user_id, amount, amount))
        conn.commit()
        conn.close()

    #-------------------------------------------------------------------------- 
    # RU: Удалить бюджет из бд
    # EN: Delete budget from the database
    # PL: Usuń budżet z bazy danych

    @staticmethod
    def del_budget_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM budgets WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM categories WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()

    #-------------------------------------------------------------------------- 
    # RU: Обновление оставшейся суммы в категории
    # EN: Update remaining amount in category
    # PL: Aktualizacja pozostałej kwoty w kategorii

    @staticmethod
    def expense_remaining_amount(amount, user_id, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(''' 
        UPDATE categories SET remaining_amount = remaining_amount - ? 
        WHERE user_id = ? AND name = ?''', (amount, user_id, name))

        conn.commit()
        conn.close()
    