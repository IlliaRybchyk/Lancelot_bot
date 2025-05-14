from aiogram.fsm.state import State, StatesGroup

#-------------------------------------------------------------------------- 
# RU: Определение состояний для работы с балансами и расходами
# EN: Defining states for working with balances and expenses
# PL: Definiowanie stanów do pracy z saldami i wydatkami

class BalanceStates(StatesGroup):

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода суммы при создании баланса
    # EN: Waiting for the input of the balance amount
    # PL: Czekanie na wprowadzenie kwoty salda

    waiting_for_balance = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода суммы расходов
    # EN: Waiting for the input of the expense amount
    # PL: Czekanie na wprowadzenie kwoty wydatków

    waiting_for_expense_amount = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода категории расходов
    # EN: Waiting for the input of the expense category
    # PL: Czekanie na wprowadzenie kategorii wydatków

    waiting_for_expense_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода комментария к расходам
    # EN: Waiting for the input of the expense commentary
    # PL: Czekanie na wprowadzenie komentarza do wydatków

    waiting_for_expenses_commentary = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода суммы пополнения
    # EN: Waiting for the input of the top-up amount
    # PL: Czekanie na wprowadzenie kwoty doładowania

    waiting_for_top_up = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидания выбора типа расходов
    # EN: Waiting for choosing the type of expense
    # PL: Czekanie na wybór typu wydatku

    waiting_for_show_expense = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание выбора категории расходов
    # EN: Waiting for choosing the expense category
    # PL: Czekanie na wybór kategorii wydatków

    waiting_for_show_expense_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание выбора категории пополнения
    # EN: Waiting for choosing the top-up category
    # PL: Czekanie na wybór kategorii doładowania

    waiting_for_top_up_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода комментария к пополнению
    # EN: Waiting for the input of the top-up commentary
    # PL: Czekanie na wprowadzenie komentarza do doładowania

    waiting_for_top_up_comment = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание отображения пополнений
    # EN: Waiting for displaying top-ups
    # PL: Czekanie na wyświetlenie doładowań

    waiting_for_show_top_up = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание выбора категории пополнений
    # EN: Waiting for choosing the top-up category
    # PL: Czekanie na wybór kategorii doładowań

    waiting_for_show_top_up_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода новой суммы для бюджета
    # EN: Waiting for entering a new amount for the budget
    # PL: Czekanie na wprowadzenie nowej kwoty dla budżetu

    waiting_for_new_plan_amount = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода новой категории для бюджета
    # EN: Waiting for entering a new category for the budget
    # PL: Czekanie na wprowadzenie nowej kategorii dla budżetu

    waiting_for_new_plan_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание ввода новой суммы для категории бюджета
    # EN: Waiting for entering a new amount for the budget category
    # PL: Czekanie na wprowadzenie nowej kwoty dla kategorii budżetu

    waiting_for_new_plan_category_amount = State()

    #--------------------------------------------------------------------------  
    # RU: Подтверждение новой категории для бюджета
    # EN: Confirming a new category for the budget
    # PL: Potwierdzenie nowej kategorii dla budżetu

    confirm_new_plan_category = State()

    #--------------------------------------------------------------------------  
    # RU: Ожидание выбора языка
    # EN: Waiting for language selection
    # PL: Czekanie na wybór języka

    waiting_for_language = State()