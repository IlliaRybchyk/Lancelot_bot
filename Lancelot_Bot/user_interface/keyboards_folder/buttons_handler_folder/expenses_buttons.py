from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from commands.expеnses_folder.expenses_commands import BotExpensesCommands

router = Router()

#-------------------------------------------------------------------------- 
# RU: Маппинг текста кнопок на команды
# EN: Mapping button text to the corresponding handler commands
# PL: Mapowanie tekstu przycisków na odpowiednie komendy obsługi

button_to_command = {
    "История расходов": BotExpensesCommands.show_expense_handler,  # История расходов
    "Добавить расходы": BotExpensesCommands.open_expense_handler,  # Добавление расходов
    "Очистить расходы": BotExpensesCommands.clear_expense_handler,  # Очистка расходов
    "Add expenses": BotExpensesCommands.open_expense_handler,  # Add expenses (English)
    "Expenses history": BotExpensesCommands.show_expense_handler,  # Expenses history (English)
    "Clear expenses": BotExpensesCommands.clear_expense_handler,  # Clear expenses (English)
    "Dodaj wydatki": BotExpensesCommands.open_expense_handler,  # Dodaj wydatki (Polish)
    "Historia wydatków": BotExpensesCommands.show_expense_handler,  # Historia wydatków (Polish)
    "Wyczyść wydatki": BotExpensesCommands.clear_expense_handler,  # Wyczyść wydatki (Polish)
}

#-------------------------------------------------------------------------- 
# RU: Обработчик всех кнопок по маппингу
# EN: Handler for all buttons according to the mapping
# PL: Obsługuje wszystkie przyciski według mapowania

@router.message(F.text.in_(button_to_command.keys()))
async def handle_expense_buttons(message: Message, state: FSMContext):
    handler = button_to_command[message.text]  # Получаем соответствующий обработчик для текста кнопки
    if handler in [BotExpensesCommands.open_expense_handler, BotExpensesCommands.show_expense_handler]:  # Обработчик для добавления или отображения расходов
        await handler(message, state)  # Вызов обработчика с состоянием
    else:
        await handler(message)  # Вызов обработчика без состояния