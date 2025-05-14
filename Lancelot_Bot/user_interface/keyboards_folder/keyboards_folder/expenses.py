from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#--------------------------------------------------------------------------
# RU: Клавиатура выбора категории расходов
# EN: Expense category selection keyboard
# PL: Klawiatura wyboru kategorii wydatków

expense_category_keyboard_ru = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Продукты", callback_data="cat_groceries"),
        InlineKeyboardButton(text="Кафе", callback_data="cat_cafe")
    ],
    [
        InlineKeyboardButton(text="Аренда жилья", callback_data="cat_rent"),
        InlineKeyboardButton(text="Коммунальные платежи", callback_data="cat_utilities")
    ],
    [
        InlineKeyboardButton(text="Транспорт", callback_data="cat_transport"),
        InlineKeyboardButton(text="Связь и Интернет", callback_data="cat_mobile")
    ]
])

expense_category_keyboard_eng = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Groceries", callback_data="cat_groceries"),
        InlineKeyboardButton(text="Cafe", callback_data="cat_cafe")
    ],
    [
        InlineKeyboardButton(text="Rent", callback_data="cat_rent"),
        InlineKeyboardButton(text="Utilities", callback_data="cat_utilities")
    ],
    [
        InlineKeyboardButton(text="Transport", callback_data="cat_transport"),
        InlineKeyboardButton(text="Mobile & Internet", callback_data="cat_mobile")
    ]
])

expense_category_keyboard_pl = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Zakupy spożywcze", callback_data="cat_groceries"),
        InlineKeyboardButton(text="Kawiarnia", callback_data="cat_cafe")
    ],
    [
        InlineKeyboardButton(text="Wynajem mieszkania", callback_data="cat_rent"),
        InlineKeyboardButton(text="Opłaty komunalne", callback_data="cat_utilities")
    ],
    [
        InlineKeyboardButton(text="Transport", callback_data="cat_transport"),
        InlineKeyboardButton(text="Telefon i Internet", callback_data="cat_mobile")
    ]
])

#--------------------------------------------------------------------------
# RU: Клавиатура для просмотра расходов (все или по категориям)
# EN: Show expenses options (all or by category)
# PL: Wyświetlanie wydatków (wszystkie lub według kategorii)

show_expenses_keyboard_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Все расходы", callback_data="show_all_expenses"),
        InlineKeyboardButton(text="По категориям", callback_data="show_category_expenses")
    ]
])

show_expenses_keyboard_eng = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="All expenses", callback_data="show_all_expenses"),
        InlineKeyboardButton(text="By category", callback_data="show_category_expenses")
    ]
])

show_expenses_keyboard_pl = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="All expenses", callback_data="show_all_expenses"),
        InlineKeyboardButton(text="By category", callback_data="show_category_expenses")
    ]
])

#--------------------------------------------------------------------------
# RU: Словарь перевода категорий расходов
# EN: Category name translator (internal name -> display name)
# PL: Tłumacz kategorii wydatków

expense_category_translator_ru = {
    "groceries": "Продукты",
    "cafe": "Кафе",
    "transport": "Транспорт",
    "rent": "Аренда жилья",
    "utilities": "Коммунальные платежи",
    "mobile": "Связь и Интернет"
}

expense_category_translator_eng = {
    "groceries": "Groceries",
    "cafe": "Cafés/Restaurants",
    "transport": "Transport",
    "rent": "Renting",
    "utilities": "Utilities",
    "mobile": "Mobile & Internet"
}

expense_category_translator_pl = {
    "groceries": "Zakupy spożywcze",
    "cafe": "Kawiarnie/Restauracje",
    "transport": "Transport",
    "rent": "Wynajem",
    "utilities": "Rachunki",
    "mobile": "Telefon i Internet"
}