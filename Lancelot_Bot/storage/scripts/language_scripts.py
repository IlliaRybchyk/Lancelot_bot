from storage.db_connection import get_connection

class DbLanguageCommands:

    #-------------------------------------------------------------------------- 
    # RU: Выбор языка пользователем
    # EN: User language selection
    # PL: Wybór języka przez użytkownika

    @staticmethod
    def chose_language(user_id, language):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
        INSERT INTO languages (user_id, language) 
        VALUES(?, ?) 
        ON CONFLICT(user_id) DO UPDATE SET language = excluded.language
        ''', (user_id, language))
        conn.commit()
        conn.close()