from aiogram import F, Router
from aiogram.types import Message
from commands.botcommands_folder.botcommands import BotCommands
from commands.botcommands_folder.translation import BotTranslations
from aiogram.fsm.context import FSMContext

router = Router()

#---------------------------------------------------------------------- 
# RU: Маппинг текста кнопок на команды 
# EN: Mapping button text to the corresponding handler commands 
# PL: Mapowanie tekstu przycisków na odpowiednie komendy obsługi

button_to_command = {
    "Работа с балансом":BotCommands.open_balance_menu,
    "Работа с расходами":BotCommands.open_expenses_menu,
    "Вернуться назад":BotCommands.get_back,
    "Работа с пополнениями":BotCommands.open_top_up_menu,
    "Работа с планированием":BotCommands.open_plan_menu,
    "Язык/Language/Język":BotTranslations.chose_language,
    "Balance management": BotCommands.open_balance_menu,
    "Expenses management": BotCommands.open_expenses_menu,
    "Top-ups management": BotCommands.open_top_up_menu,
    "Planning management": BotCommands.open_plan_menu,
    "Go back": BotCommands.get_back,
    "Language/Язык/Język": BotTranslations.chose_language,
    "Zarządzanie saldem": BotCommands.open_balance_menu,
    "Zarządzanie wydatkami": BotCommands.open_expenses_menu,
    "Zarządzanie doładowaniami": BotCommands.open_top_up_menu,
    "Zarządzanie planowaniem": BotCommands.open_plan_menu,
    "Wróć": BotCommands.get_back,
    "Język/Язык/Language": BotTranslations.chose_language
}

#---------------------------------------------------------------------- 
# RU: Обработчик всех кнопок по маппингу
# EN: Handler for all buttons according to the mapping
# PL: Obsługuje wszystkie przyciski według mapowania

@router.message(F.text.in_(button_to_command.keys()))
async def handle_balance_buttons(message: Message, state:FSMContext):
    handler = button_to_command[message.text]
    if handler in [BotTranslations.chose_language]:
        await handler(message, state)
    else:
        await handler(message)