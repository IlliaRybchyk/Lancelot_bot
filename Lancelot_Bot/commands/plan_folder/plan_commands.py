from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from config.states import BalanceStates
from commands.usercommands.user_info import UserInfoCommands
from storage.scripts.plan_scripts import DbPlanCommands

from commands.botcommands_folder.translation import BotTranslations
from commands.usercommands.user_plan import UserPlanCommands
from user_interface.keyboards_folder.keyboards_folder.expenses import *

router = Router()

#--------------------------------------------------------------------------
# RU: Создание класса работы с командами планирования
# EN: Creation of class for handling planning commands
# PL: Utworzenie klasy do obsługi komend planowania

class BotPlanCommands:

    #--------------------------------------------------------------------------
    # RU: Обработка создания нового плана
    # EN: Handler for creating a new plan
    # PL: Obsługa tworzenia nowego planu

    @staticmethod
    async def create_new_plan_handler(message: Message, state: FSMContext):
        user_id = UserInfoCommands.get_user_id(message)
        budgets = UserPlanCommands.get_budgets_from_db(user_id)
        text = await BotTranslations.translate(user_id, "waiting_for_plan_amount")

        if budgets:
            DbPlanCommands.del_budget_from_db(user_id)

        await message.answer(text)
        await state.set_state(BalanceStates.waiting_for_new_plan_amount)

    #--------------------------------------------------------------------------
    # RU: Отображение текущего плана пользователя
    # EN: Display user's current plan
    # PL: Wyświetlenie aktualnego planu użytkownika

    @staticmethod
    async def show_plan(message: Message):
        user_id = UserInfoCommands.get_user_id(message)
        budget = UserPlanCommands.get_budgets_from_db(user_id)

        if budget is None:
            errortext = await BotTranslations.translate(user_id, "not_plan")
            await message.answer(errortext)
            return

        budget_amount = budget["total_amount"]
        remaining_amount = budget["remaining_amount"]
        categories = UserPlanCommands.get_categories_from_db(user_id)

        expense_category_translator = await BotTranslations.open_menu(
            message.from_user.id,
            expense_category_translator_ru,
            expense_category_translator_eng,
            expense_category_translator_pl
        )
        category_text = "\n".join([
            (await BotTranslations.translate(user_id, "plan_category_show")).format(
                category_name=expense_category_translator.get(cat["name"]),
                category_amount=cat["category_amount"],
                remaining_category_amount=cat["remaining_category_amount"]
            )
            for cat in categories
        ])
        text = (await BotTranslations.translate(user_id, "save_plan")).format(
            budget_amount=budget_amount,
            category_text="\n" + category_text,
            remaining_amount=remaining_amount
        )

        await message.answer(text)