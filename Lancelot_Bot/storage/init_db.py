from storage.db_connection import get_connection

#-------------------------------------------------------------------------- 
# RU: Создание базы данных
# EN: Database initialization
# PL: Inicjalizacja bazy danych

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    #-------------------------------------------------------------------------- 
    # RU: Создание бд с балансами
    # EN: Create the balances table
    # PL: Tworzenie tabeli z balansami

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS balances(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE,
    amount REAL
    )
    ''')

    #-------------------------------------------------------------------------- 
    # RU: Создание бд с пополнениями
    # EN: Create the top-ups table
    # PL: Tworzenie tabeli z doładowaniami

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS top_ups(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    amount REAL,
    date TEXT,
    category TEXT,
    comment TEXT
    )''')

    #-------------------------------------------------------------------------- 
    # RU: Создание бд с расходами
    # EN: Create the expenses table
    # PL: Tworzenie tabeli z wydatkami

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    date TEXT,
    category TEXT,
    amount REAL,
    comment TEXT
    )
    ''')

    #-------------------------------------------------------------------------- 
    # RU: Создание бд с бюджетом
    # EN: Create the budgets table
    # PL: Tworzenie tabeli z budżetami

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE,
    total_amount FLOAT,
    remaining_amount FLOAT
    )
    ''')

    #-------------------------------------------------------------------------- 
    # RU: Создание бд с категориями бюджета
    # EN: Create the categories table
    # PL: Tworzenie tabeli z kategoriami budżetu

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    user_id TEXT,
    amount FLOAT,
    remaining_amount FLOAT,
    UNIQUE(name, user_id)
    );         
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE,
    language TEXT
    );         
    ''')

    conn.commit()
    conn.close()