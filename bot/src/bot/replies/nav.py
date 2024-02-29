import os
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import bot.replies.btntxt as btntxt

load_dotenv()

ok_button = InlineKeyboardButton(btntxt.OK, callback_data='ok')
error_button = InlineKeyboardButton(btntxt.ERROR, callback_data='error')
parsing_markup = InlineKeyboardMarkup(row_width=2).add(ok_button, error_button)

mistake_general_button = InlineKeyboardButton(btntxt.MISTAKE_GENERAL, callback_data='res')
experience_error_button = InlineKeyboardButton(btntxt.EXPERIENCE_ERROR, callback_data='res')
education_error_button = InlineKeyboardButton(btntxt.EDUCATION_ERROR, callback_data='res')
skills_error_button = InlineKeyboardButton(btntxt.SKILLS_ERROR, callback_data='res')
languages_error_button = InlineKeyboardButton(btntxt.LANGUAGES_ERROR, callback_data='res')
error_markup = InlineKeyboardMarkup(row_width=2).add(mistake_general_button, experience_error_button, education_error_button, skills_error_button, languages_error_button)