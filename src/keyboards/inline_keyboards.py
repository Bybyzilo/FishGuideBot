import json

from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup



back_in_menu_kb = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Назад в меню', callback_data='back_in_menu')
		]
	]
)