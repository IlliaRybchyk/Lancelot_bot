import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from config.config import BOT_TOKEN
from config.initializing import include_all_routers
from storage.init_db import initialize_database

# ---------------------- Логгирование / Logging / Logowanie ----------------------
# Настройка базового логгирования, чтобы выводить сообщения в консоль.
# Basic logging setup to display messages in the console.
# Podstawowa konfiguracja logowania do wyświetlania komunikatów w konsoli.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------- Middleware / Middleware / Middleware ----------------------
# Класс промежуточного слоя, логирующий входящие текстовые сообщения пользователей.
# Middleware class that logs incoming user text messages.
# Klasa pośrednia logująca przychodzące wiadomości tekstowe od użytkowników.

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            logger.info(f"User {event.from_user.id} sent: {event.text or '<non-text message>'}")
        return await handler(event, data)

# ---------------------- Инициализация / Initialization / Inicjalizacja ----------------------
# Функция создаёт бота и диспетчер, регистрирует middleware и роутеры.
# This function creates the bot and dispatcher, registers middleware and routers.
# Funkcja tworzy bota i dispatcher, rejestruje middleware i routery.

def setup_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.message.middleware(LoggingMiddleware())
    include_all_routers(dp)
    return bot, dp

# ---------------------- Запуск / Run / Uruchomienie ----------------------
# Основная функция: инициализация базы данных и запуск бота.
# Main function: database initialization and bot launch.
# Główna funkcja: inicjalizacja bazy danych i uruchomienie bota.

async def main():
    initialize_database()  # ← Сделай async, если еще не сделано / Make async if needed / Zmień na async, jeśli to możliwe
    bot, dp = setup_bot()
    await dp.start_polling(bot)

# Точка входа / Entry point / Punkt wejścia
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот остановлен / Bot stopped / Bot zatrzymany")