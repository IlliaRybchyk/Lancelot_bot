from storage.db_connection import get_connection

#--------------------------------------------------------------------------
# RU: Создание базы данных
# EN: Creating a database
# PL: Tworzenie bazy danych

class DbBalanceCommands:

    #--------------------------------------------------------------------------
    # RU: Создание нового баланса
    # EN: Creating a new balance
    # PL: Tworzenie nowego salda

    @staticmethod
    def create_new_balance(user_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO balances (user_id, amount)
        VALUES(?, ?)
        ON CONFLICT(user_id) DO UPDATE SET amount = excluded.amount
        ''', (user_id, amount))
        conn.commit()
        conn.close()

    #--------------------------------------------------------------------------
    # RU: Пополнение баланса
    # EN: Top-up balance
    # PL: Doładowanie salda

    @staticmethod
    def top_up_balance(user_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE balances SET amount = amount + ? WHERE user_id = ?', (amount, user_id))
        conn.commit()
        conn.close()

    #--------------------------------------------------------------------------
    # RU: Расход баланса
    # EN: Expense balance
    # PL: Wydatki z salda

    @staticmethod
    def expense_balance(user_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE balances SET amount = amount - ? WHERE user_id = ?', (amount, user_id))
        conn.commit()
        conn.close()

    #--------------------------------------------------------------------------
    # RU: Удаление баланса
    # EN: Deleting balance
    # PL: Usuwanie salda
    
    @staticmethod
    def delete_balance(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM balances WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()