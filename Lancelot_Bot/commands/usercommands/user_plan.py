from storage.db_connection import get_connection

#--------------------------------------------------------------------------
# RU: Класс планирования пользователя
# EN: User planning class
# PL: Klasa planowania użytkownika

class UserPlanCommands:

    #--------------------------------------------------------------------------
    # RU: Получение бюджета
    # EN: Getting budget
    # PL: Pobieranie budżetu

    @staticmethod
    def get_budgets_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT total_amount, remaining_amount FROM budgets WHERE user_id = ?
        ''', (user_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "total_amount": row[0],
                "remaining_amount": row[1],
            }
    
    #--------------------------------------------------------------------------
    # RU: Получение категорий бюджета
    # EN: Getting budget categories
    # PL: Pobieranie kategorii budżetu

    @staticmethod
    def get_categories_from_db(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT name, amount, remaining_amount FROM categories WHERE user_id = ?
        ''', (user_id,))

        rows = cursor.fetchall()
        conn.close()

        categories = []

        for row in rows:
            category = {
                "name": row[0],
                "category_amount": row[1],
                "remaining_category_amount": row[2],
            }
            categories.append(category)
        
        return categories
    
    #--------------------------------------------------------------------------
    # RU: Получение оставшейся суммы по категории
    # EN: Getting remaining amount by category
    # PL: Pobieranie pozostałej kwoty według kategorii

    @staticmethod
    def get_plan_remaining_amount(user_id, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT remaining_amount FROM categories WHERE user_id = ? AND name = ?
        ''', (user_id, name))

        result = cursor.fetchone()
        conn.close()

        return result
