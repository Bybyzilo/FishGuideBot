from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove



main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌅 Прогноз клёва'),
            KeyboardButton(text='🏝️ Места ловли'),
            KeyboardButton(text='🎣 Советы по рыбалке')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие..'
)



guide_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Техника ловли'),
            KeyboardButton(text='Выбор снасти'),
            KeyboardButton(text='Не придумали еще')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


