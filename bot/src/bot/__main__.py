import os
import logging
import asyncio
import signal
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ParseMode
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
import bot.replies.btntxt as btntxt
import bot.replies.reply as reply
from bot.replies.nav import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

# Logging
# Create a logger instance
log = logging.getLogger('main.py-aiogram')

# Create logfile
# logging.basicConfig(filename="main.py.log")

# Create log formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create console logging handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)

# Create file logging handler and set its level
fh = logging.FileHandler(r'main.py.log')
fh.setFormatter(formatter)
log.addHandler(fh)

# Set logging level for this logger
logging_level_lower = os.getenv('LOGGING_LEVEL').lower()
if logging_level_lower == 'debug':
    log.setLevel(logging.DEBUG)
    log.critical("Log level set to debug")
elif logging_level_lower == 'info':
    log.setLevel(logging.INFO)
    log.critical("Log level set to info")
elif logging_level_lower == 'warning':
    log.setLevel(logging.WARNING)
    log.critical("Log level set to warning")
elif logging_level_lower == 'error':
    log.setLevel(logging.ERROR)
    log.critical("Log level set to error")
elif logging_level_lower == 'critical':
    log.setLevel(logging.CRITICAL)
    log.critical("Log level set to critical")

# System handling
class GracefulKiller:
    """Watches for SIGTERM and SIGKILL signals;
    if received, closes the database and exits gracefully"""
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):  # TODO: Why is *args required?
        """Saves the database and exits gracefully"""
        self.kill_now = True
        log.info('Storage closed')
        log.info('nShutting down...')
        exit(0)

# Get Telegram API token
TELEGRAM_API_TOKEN = os.getenv('TG_TOKEN')
STORAGE_PATH = os.getenv('STORAGE_PATH')

bot = Bot(token=TELEGRAM_API_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)

# setup start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    log.info(f"User {message.from_user.id} started the bot")
    await message.answer(reply.welcome_message())

# setup documment file recieve
@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message: types.Message):
    log.info(f"User {message.from_user.id} sent a document")
    await message.answer(reply.parsing_result('test'), reply_markup=parsing_markup)

# handle parsing result callback
@dp.callback_query_handler(lambda c: c.data == 'ok')
async def ok_callback(callback_query: types.CallbackQuery):
    log.info(f"User {callback_query.from_user.id} clicked OK")
    await callback_query.answer()
    await callback_query.message.answer(reply.parsing_ok())

@dp.callback_query_handler(lambda c: c.data == 'error')
async def error_callback(callback_query: types.CallbackQuery):
    log.info(f"User {callback_query.from_user.id} clicked ERROR")
    await callback_query.answer()
    await callback_query.message.answer(reply.error_in_parsing(), reply_markup=error_markup)

@dp.callback_query_handler(lambda c: c.data == 'res')
async def res_callback(callback_query: types.CallbackQuery):
    log.info(f"User {callback_query.from_user.id} clicked ERROR")
    await callback_query.answer()
    await callback_query.message.answer(reply.error_reply())


if __name__ == "__main__":
    log.info('Starting bot...')
    killer = GracefulKiller()
    log.info('Process manager is up')
    log.info('Starting aiogram...')
    executor.start_polling(dp, skip_updates=True)