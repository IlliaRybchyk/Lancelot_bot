from aiogram import Dispatcher

from commands.balance_folder import balance_states, balance_commands
from commands.expеnses_folder import expenses_states, expenses_commands, show_expenses_states
from commands.botcommands_folder import botcommands, translation
from commands.top_up_folder import top_ups_commands, top_ups_states, show_top_ups_states
from commands.plan_folder import plan_commands, plan_states


from user_interface.keyboards_folder.buttons_handler_folder import expenses_buttons
from user_interface.keyboards_folder.buttons_handler_folder import (
    balance_buttons, menu_buttons, plan_buttons
    )
from storage.init_db import initialize_database

#--------------------------------------------------------------------------
# RU: Добавление всех роутеров в диспетчер
# EN: Adding all routers to the dispatcher
# PL: Dodanie wszystkich routerów do dyspozytora

def include_all_routers(dp: Dispatcher):

    routers = [
        show_expenses_states.router,
        balance_states.router,
        balance_commands.router,
        expenses_states.router,
        expenses_commands.router,
        botcommands.router,
        expenses_buttons.router,
        balance_buttons.router,
        top_ups_commands.router,
        top_ups_states.router,
        menu_buttons.router,
        show_top_ups_states.router,
        plan_commands.router,
        plan_states.router,
        plan_buttons.router,
        translation.router
    ]

    for router in routers:
        dp.include_router(router)

#--------------------------------------------------------------------------
# RU: Инициализация всех баз данных
# EN: Initialization of all databases
# PL: Inicjalizacja wszystkich baz danych

async def initialize_databases():
    initialize_database()
