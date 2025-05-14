from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

#--------------------------------------------------------------------------
# RU: Главное меню с разделами управления
# EN: Main menu with management sections
# PL: Menu główne z sekcjami zarządzania

main_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Работа с балансом"), KeyboardButton(text="Работа с пополнениями")],  # Управление балансом и пополнениями
    [KeyboardButton(text="Работа с расходами"), KeyboardButton(text="Работа с планированием")],  # Расходы и планирование
    [KeyboardButton(text="Язык/Language/Język")]  # Кнопка смены языка
], resize_keyboard=True)

main_menu_eng = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Balance management"), KeyboardButton(text="Top-ups management")],
        [KeyboardButton(text="expenses management"), KeyboardButton(text="Planning management")],
        [KeyboardButton(text="Язык/Language/Język")]
    ],
    resize_keyboard=True
)

main_menu_pl = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Zarządzanie saldem"), KeyboardButton(text="Zarządzanie doładowaniami")],
        [KeyboardButton(text="Zarządzanie wydatkami"), KeyboardButton(text="Zarządzanie planowaniem")],
        [KeyboardButton(text="Язык/Language/Język")]
    ],
    resize_keyboard=True
)

#--------------------------------------------------------------------------
# RU: Меню управления балансом
# EN: Balance management menu
# PL: Menu zarządzania saldem

balance_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Новый баланс"), KeyboardButton(text="Удалить баланс")],  # Создание и удаление баланса
    [KeyboardButton(text="Показать баланс"), KeyboardButton(text="Вернуться назад")]  # Просмотр и возврат
], resize_keyboard=True)

balance_menu_eng = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="New balance"), KeyboardButton(text="Delete balance")],
        [KeyboardButton(text="Show balance"), KeyboardButton(text="Go back")]
    ],
    resize_keyboard=True
)

balance_menu_pl = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Nowy saldo"), KeyboardButton(text="Usuń saldo")],
        [KeyboardButton(text="Pokaż saldo"), KeyboardButton(text="Wróć")]
    ],
    resize_keyboard=True
)

#--------------------------------------------------------------------------
# RU: Меню работы с расходами
# EN: Expenses management menu
# PL: Menu zarządzania wydatkami

expenses_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить расходы"), KeyboardButton(text="История расходов")],  # Добавление и просмотр расходов
    [KeyboardButton(text="Очистить расходы"), KeyboardButton(text="Вернуться назад")]  # Очистка и возврат
], resize_keyboard=True)

expenses_menu_eng = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Add expenses"), KeyboardButton(text="Expenses history")],
    [KeyboardButton(text="Clear expenses"), KeyboardButton(text="Go back")]
], resize_keyboard=True)

expenses_menu_pl = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Dodaj wydatki"), KeyboardButton(text="Historia wydatków")],
    [KeyboardButton(text="Wyczyść wydatki"), KeyboardButton(text="Wróć")]
], resize_keyboard=True)

#--------------------------------------------------------------------------
# RU: Меню работы с пополнениями
# EN: Top-ups management menu
# PL: Menu zarządzania doładowaniami

top_ups_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пополнить баланс"), KeyboardButton(text="Показать баланс"), KeyboardButton(text="История пополнений")],  # Добавить, показать, история
    [KeyboardButton(text="Очистить пополнения"), KeyboardButton(text="Вернуться назад")]  # Очистить и вернуться
], resize_keyboard=True)

top_ups_menu_eng = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Top up balance"), KeyboardButton(text="Show balance"), KeyboardButton(text="Top-ups history")],
    [KeyboardButton(text="Clear top-ups"), KeyboardButton(text="Go back")]
], resize_keyboard=True)

top_ups_menu_pl = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Doładuj saldo"), KeyboardButton(text="Pokaż saldo"), KeyboardButton(text="Historia doładowań")],
    [KeyboardButton(text="Wyczyść doładowania"), KeyboardButton(text="Wróć")]
], resize_keyboard=True)

#--------------------------------------------------------------------------
# RU: Меню управления планированием бюджета
# EN: Budget planning menu
# PL: Menu planowania budżetu

plan_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Создать новый план"), KeyboardButton(text="Показать мой план")],  # Создание и просмотр
    [KeyboardButton(text="Вернуться назад")]
], resize_keyboard=True)

plan_menu_eng = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Create new plan"), KeyboardButton(text="Show my plan")],
    [KeyboardButton(text="Go back")]
], resize_keyboard=True)

plan_menu_pl = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Utwórz nowy plan"), KeyboardButton(text="Pokaż mój plan")],
    [KeyboardButton(text="Wróć")]
], resize_keyboard=True)

#--------------------------------------------------------------------------
# RU: Клавиатура "Да / Нет" (inline)
# EN: Yes / No inline keyboard
# PL: Klawiatura Tak / Nie (inline)

yes_no_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Да", callback_data="yes"),
        InlineKeyboardButton(text="Нет", callback_data="no")
    ]
])

#--------------------------------------------------------------------------
# RU: Клавиатура выбора языка (inline)
# EN: Inline language selection menu
# PL: Klawiatura wyboru języka (inline)

Language_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Русский язык", callback_data="lang_ru")],
    [InlineKeyboardButton(text="English Language", callback_data="lang_eng")],
    [InlineKeyboardButton(text="Język Polski", callback_data="lang_pl")]
])