import sqlite3
import os

#-------------------------------------------------------------------------- 
# RU: Подключение к базе данных
# EN: Database connection
# PL: Połączenie z bazą danych

def get_connection():
    db_folder = os.path.join("storage")
    db_name = "database.db"
    db_path = os.path.join(db_folder, db_name)
    
    return sqlite3.connect(db_path)