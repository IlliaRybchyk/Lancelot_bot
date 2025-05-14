from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config.states import BalanceStates
from storage.scripts.balance_scripts import DbBalanceCommands
from aiogram import Router
from commands.usercommands.user_info import UserInfoCommands

from commands.botcommands_folder.translation import BotTranslations

router = Router()

#--------------------------------------------------------------------------
# RU: Класс состояний для работы с балансом
# EN: Class for balance states management
# PL: Klasa zarządzania stanami balansu

class BotBalanceStates:

    #--------------------------------------------------------------------------
    # RU: Ожидание ввода суммы для создания баланса и сохранение нового баланса
    # EN: Waiting for balance amount input and saving the new balance
    # PL: Oczekiwanie na wprowadzenie kwoty do stworzenia salda i zapisanie nowego salda

    @staticmethod
    @router.message(BalanceStates.waiting_for_balance)
    async def balance_save_handler(message: Message, state: FSMContext):
        amount_error = await BotTranslations.translate(message.from_user.id, "amount_greater")
        valueerror = (await BotTranslations.translate(message.from_user.id, "incorrect_amount"))
        user_id = UserInfoCommands.get_user_id(message)
        try:
            amount = float(message.text.replace(",", "."))

            if amount < 0 or amount == 0:
                await message.answer(amount_error)
                await state.clear()
                return

            DbBalanceCommands.create_new_balance(user_id, float(amount))

            text = (await BotTranslations.translate(user_id, "saved_balance")).format(amount=amount)

            await message.answer(text)
            await state.clear()

        except ValueError:
            
            await message.answer(valueerror)
            await state.clear()
            return