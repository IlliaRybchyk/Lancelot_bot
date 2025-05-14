from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from commands.balance_folder.balance_commands import BotBalanceCommands
from commands.top_up_folder.top_ups_commands import BotTopUpCommands

router = Router()

#-------------------------------------------------------------------------- 
# RU: Маппинг текста кнопок на команды
# EN: Mapping button text to the corresponding handler commands
# PL: Mapowanie tekstu przycisków na odpowiednie komendy obsługi

button_to_command = {
    "Новый баланс": BotBalanceCommands.open_balance_handler,
    "Показать баланс": BotBalanceCommands.show_balance_handler,
    "Пополнить баланс": BotTopUpCommands.top_up_balance_handler,
    "История пополнений": BotTopUpCommands.show_top_up_handler,
    "Удалить баланс": BotBalanceCommands.delete_balance_handler,
    "Очистить пополнения":BotTopUpCommands.clear_top_ups_history,
    "New balance": BotBalanceCommands.open_balance_handler,
    "Show balance": BotBalanceCommands.show_balance_handler,
    "Top up balance": BotTopUpCommands.top_up_balance_handler,
    "Top-ups history": BotTopUpCommands.show_top_up_handler,
    "Delete balance": BotBalanceCommands.delete_balance_handler,
    "Clear top-ups": BotTopUpCommands.clear_top_ups_history,
    "Nowy saldo": BotBalanceCommands.open_balance_handler,
    "Pokaż saldo": BotBalanceCommands.show_balance_handler,
    "Doładuj saldo": BotTopUpCommands.top_up_balance_handler,
    "Historia doładowań": BotTopUpCommands.show_top_up_handler,
    "Usuń saldo": BotBalanceCommands.delete_balance_handler,
    "Wyczyść doładowania": BotTopUpCommands.clear_top_ups_history,
}

#-------------------------------------------------------------------------- 
# RU: Обработчик всех кнопок по маппингу
# EN: Handler for all buttons according to the mapping
# PL: Obsługuje wszystkie przyciski według mapowania

@router.message(F.text.in_(button_to_command.keys()))
async def handle_balance_buttons(message: Message, state: FSMContext):
    handler = button_to_command[message.text]
    # Передаем state, если обработчику он нужен
    if handler in [BotBalanceCommands.open_balance_handler, BotTopUpCommands.top_up_balance_handler, BotTopUpCommands.show_top_up_handler]:
        await handler(message, state)
    else:
        await handler(message)