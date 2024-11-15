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
            KeyboardButton(text='Выбор снастей'),
            KeyboardButton(text='Не придумали еще')
        ],
        [
            KeyboardButton(text='Назад в меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие..'
)


forecast_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сегодня'),
            KeyboardButton(text='Завтра'),
            KeyboardButton(text='На 5 дней')
        ],
        [
            KeyboardButton(text='Назад в меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие..'
)