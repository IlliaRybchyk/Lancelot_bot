from aiogram import F, Router
from aiogram.types import Message
from commands.plan_folder.plan_commands import BotPlanCommands
from aiogram.fsm.context import FSMContext

router = Router()

#----------------------------------------------------------------------
# RU: Маппинг текста кнопок на соответствующие команды обработчиков
# EN: Mapping button text to the corresponding handler commands
# PL: Mapowanie tekstu przycisków na odpowiednie komendy obsługi

button_to_command = {
    "Создать новый план": BotPlanCommands.create_new_plan_handler,
    "Показать мой план": BotPlanCommands.show_plan,
    "Create new plan": BotPlanCommands.create_new_plan_handler,
    "Show my plan": BotPlanCommands.show_plan,
    "Utwórz nowy plan": BotPlanCommands.create_new_plan_handler,
    "Pokaż mój plan": BotPlanCommands.show_plan,
}

#----------------------------------------------------------------------
# RU: Обработчик для всех кнопок, текст которых указан в маппинге button_to_command
# EN: Handler for all buttons whose text is listed in button_to_command mapping
# PL: Obsługuje wszystkie przyciski, których tekst znajduje się w mapowaniu button_to_command

@router.message(F.text.in_(button_to_command.keys()))
async def handlers_plan_buttons(message: Message, state: FSMContext):
    handler = button_to_command[message.text]
    if handler in [BotPlanCommands.create_new_plan_handler]:
        await handler(message, state)
    else:
        await handler(message)