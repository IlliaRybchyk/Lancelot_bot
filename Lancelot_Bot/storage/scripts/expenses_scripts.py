from storage.db_connection import get_connection

#-------------------------------------------------------------------------- 
# RU: Создание класса комманд с расходами базы данных
# EN: Creating a class with database expense commands
# PL: Tworzenie klasy komend do bazy danych wydatków

class DbExpensesCommands:
    
    #-------------------------------------------------------------------------- 
    # RU: Добавление расходов в базу данных
    # EN: Adding expenses to the database
    # PL: Dodawanie wydatków do bazy danych

    @staticmethod
    def add_expense_to_db(user_id, date, category, amount, comment):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO expenses (user_id, date, category, amount, comment)
        VALUES(?, ?, ?, ?, ?)
        ''', (user_id, date, category, amount, comment))
        conn.commit()
        conn.close()

    #---------------------------------------------------------------------------
    # RU: Очистка расходов из базы данных
    # EN: Clearing expenses from the database
    # PL: Czyszczenie wydatków z bazy danych
    
    @staticmethod
    def clear_user_expenses(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()