from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from commands.botcommands_folder.translation import BotTranslations
from commands.usercommands.user_info import UserInfoCommands


from user_interface.keyboards_folder.keyboards_folder.menu import *

router = Router()

#--------------------------------------------------------------------------
# RU: Класс команд Telegram-бота
# EN: Class for Telegram bot commands
# PL: Klasa komend bota Telegram

class BotCommands:

    #--------------------------------------------------------------------------
    # RU: Команда /start — приветственное сообщение и главное меню
    # EN: /start command — welcome message and main menu
    # PL: Komenda /start — powitanie i główne menu

    @staticmethod
    @router.message(Command("start"))
    async def start_handler(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "start")
        menu = await BotTranslations.open_menu(message.from_user.id, main_menu_ru, main_menu_eng, main_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Команда /help — справка по использованию бота
    # EN: /help command — help information
    # PL: Komenda /help — pomoc i informacje

    @staticmethod
    @router.message(Command("help"))
    async def help_handler(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "help")
        menu = await BotTranslations.open_menu(message.from_user.id, main_menu_ru, main_menu_eng, main_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Открытие меню работы с балансом
    # EN: Open balance management menu
    # PL: Otwórz menu zarządzania saldem

    @staticmethod
    async def open_balance_menu(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "open_balance_menu")
        menu = await BotTranslations.open_menu(message.from_user.id, balance_menu_ru, balance_menu_eng, balance_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Открытие меню управления расходами
    # EN: Open expenses management menu
    # PL: Otwórz menu zarządzania wydatkami

    @staticmethod
    async def open_expenses_menu(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "open_expense_menu")
        menu = await BotTranslations.open_menu(message.from_user.id, expenses_menu_ru, expenses_menu_eng, expenses_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Кнопка "Назад" в главное меню
    # EN: "Back" button to main menu
    # PL: Przycisk "Wstecz" do menu głównego

    @staticmethod
    async def get_back(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "open_main_menu")
        menu = await BotTranslations.open_menu(message.from_user.id, main_menu_ru, main_menu_eng, main_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Открытие меню работы с пополнениями
    # EN: Open top-up menu
    # PL: Otwórz menu doładowań

    @staticmethod
    async def open_top_up_menu(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "open_top_up_menu")
        menu = await BotTranslations.open_menu(message.from_user.id, top_ups_menu_ru, top_ups_menu_eng, top_ups_menu_pl)
        await message.answer(text, reply_markup=menu)

    #--------------------------------------------------------------------------
    # RU: Открытие меню управления планированием
    # EN: Open planning management menu
    # PL: Otwórz menu zarządzania planowaniem

    @staticmethod
    async def open_plan_menu(message: Message):
        text = await BotTranslations.translate(message.from_user.id, "open_plan_menu")
        menu = await BotTranslations.open_menu(message.from_user.id, plan_menu_ru, plan_menu_eng, plan_menu_pl)
        await message.answer(text, reply_markup=menu)
