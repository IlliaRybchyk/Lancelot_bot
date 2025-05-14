from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#--------------------------------------------------------------------------
# RU: Клавиатура категорий пополнений на русском языке
# EN: Top-up categories keyboard in Russian
# PL: Klawiatura kategorii doładowań w języku rosyjskim

top_ups_category_keyboard_ru = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Зарплата", callback_data="cat_sallary"),
        InlineKeyboardButton(text="Возврат долгов", callback_data="cat_debts") 
    ],
    [
        InlineKeyboardButton(text="Продажа имущества", callback_data="cat_sells"), 
        InlineKeyboardButton(text="Банковские проценты", callback_data="cat_procents")
    ],
])

#--------------------------------------------------------------------------
# RU: Клавиатура категорий пополнений на английском языке
# EN: Top-up categories keyboard in English
# PL: Klawiatura kategorii doładowań w języku angielskim

top_ups_category_keyboard_eng = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Salary", callback_data="cat_sallary"),
        InlineKeyboardButton(text="Debt Repayment", callback_data="cat_debts")
    ],
    [
        InlineKeyboardButton(text="Asset Sale", callback_data="cat_sells"),
        InlineKeyboardButton(text="Bank Interest", callback_data="cat_procents")
    ],
])

#--------------------------------------------------------------------------
# RU: Клавиатура категорий пополнений на польском языке
# EN: Top-up categories keyboard in Polish
# PL: Klawiatura kategorii doładowań w języku polskim

top_ups_category_keyboard_pl = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Wynagrodzenie", callback_data="cat_sallary"),
        InlineKeyboardButton(text="Spłata długów", callback_data="cat_debts")
    ],
    [
        InlineKeyboardButton(text="Sprzedaż majątku", callback_data="cat_sells"),
        InlineKeyboardButton(text="Odsetki bankowe", callback_data="cat_procents")
    ],
])

#--------------------------------------------------------------------------
# RU: Клавиатура выбора отображения пополнений (все или по категориям)
# EN: Keyboard for selecting how to view top-ups (all or by category)
# PL: Klawiatura wyboru widoku doładowań (wszystkie lub według kategorii)

show_top_ups_keyboard_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Все пополнения", callback_data="show_all_top_ups"),
        InlineKeyboardButton(text="По категориям", callback_data="show_category_top_ups")
    ]
])

show_top_ups_keyboard_eng = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="All Top-Ups", callback_data="show_all_top_ups"),
        InlineKeyboardButton(text="By Category", callback_data="show_category_top_ups")
    ]
])

show_top_ups_keyboard_pl = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Wszystkie doładowania", callback_data="show_all_top_ups"),
        InlineKeyboardButton(text="Według kategorii", callback_data="show_category_top_ups")
    ]
])

#--------------------------------------------------------------------------
# RU: Словари-переводчики названий категорий по ключу
# EN: Dictionaries for translating category keys into names
# PL: Słowniki tłumaczące klucze kategorii na ich nazwy

top_ups_category_translator_ru = {
    "sallary": "Зарплата",
    "debts": "Возврат долгов",
    "sells": "Продажа имущества",
    "procents": "Банковские проценты"
}

top_ups_category_translator_eng = {
    "sallary": "Salary",
    "debts": "Debt Repayment",
    "sells": "Asset Sales",
    "procents": "Bank Interest"
}

top_ups_category_translator_pl = {
    "sallary": "Pensja",
    "debts": "Spłata długów",
    "sells": "Sprzedaż majątku",
    "procents": "Oprocentowanie bankowe"
}