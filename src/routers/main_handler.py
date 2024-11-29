from typing import Optional

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from keyboards import reply_keyboards, inline_keyboards
from parser import fishing_forecast


router = Router()



@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='🎣 Привет, рыбак!\n\n'
             'Я твой виртуальный помощник в мире рыбалки! Я здесь, чтобы помочь тебе с выбором места для ловли, подсказать лучшие приманки и снасти, а также поделиться советами по технике ловли. \n\n'
             'Не знаешь, где ловить? Хочешь узнать о лучших сезонах для ловли? Или, может быть, интересуешься, как правильно ухаживать за уловом? Просто задай вопрос, и я с радостью помогу!\n'
             'Удачной рыбалки! 🐟',
        reply_markup=reply_keyboards.main_kb
    )


@router.message(F.text.lower() == 'назад в меню')
async def back_in_menu(message: Message, state: Optional[FSMContext]=None):
    """ Back in main menu """

    await message.answer(
        "Вы вернулись в главное меню!",
        reply_markup=reply_keyboards.main_kb
    )

    if state:
        await state.clear()



@router.message(F.text == '🌅 Прогноз клёва')
async def bite_forecast_answer(message: Message):
    data: dict = await fishing_forecast()

    await message.answer(str(data))

    await message.answer(
            text='Выберите дату прогноза',
            reply_markup=reply_keyboards.forecast_kb
        )


@router.message(F.text == '🏝️ Места ловли')
async def fish_info_answer(message: Message):
    await message.answer(
        text='Подсказки о лучших местах для рыбной ловли в зависимости '
             'от региона, времени года и погодных условий.\n\n'
             'Пользовательские отзывы и отзывы о местах ловли.',
        reply_markup=inline_keyboards.back_in_menu_kb
    )


@router.message(F.text == '🎣 Советы по рыбалке')
async def guide_answer(message: Message):
    await message.answer(
        text='Здесь находятся все советы для помощи в ловле рыбы',
        reply_markup=reply_keyboards.guide_kb
    )



@router.message(F.text == 'Техника ловли')
async def guid_answer(message: Message):
    await message.answer(
        text='Указания по различным методам ловли '
        '(фидеры, спиннинг, поплавок и т.д.) '
        'с описанием особенностей и секретов.\n\n'
        'Советы по ловле определённых видов рыбы '
        '(щука, карп, лещ и др.).',
        reply_markup=inline_keyboards.back_in_guide_kb
    )


@router.message(F.text == 'Выбор снастей')
async def guid_answer(message: Message):
    await message.answer(
        text='Рекомендации по выбору удочек, '
        'катушек, лесок и приманок для различных '
        'видов рыбы и условий ловли.\n\n'
        'Пошаговые инструкции по сборке снасти.',
        reply_markup=inline_keyboards.back_in_guide_kb
    )


""" Handlers of the bite forecast """

# @router.message(F.text == 'Сегодня')
# async def today_answer(message: Message):

    # data: dict = await fishing_forecast()
    # days = list(data.keys())
    # day_now = data[days[0]]

    # # await message.answer('Пока что представлен демо вариант с одной рекой - Темерник')
    # await message.answer(
    #     text='Пока что представлен демо вариант с одной рекой - Темерник'
    #          f'      Сегодня      \n'
    #          f'     {day_now['date']}      \n\n'

    #          f'Время | температура воздуха      \n'
    #          f'Ночь 02:00  | {day_now['air_temp'][0]} °C \n'
    #          f'Утро 08:00  | {day_now['air_temp'][1]} °C \n'
    #          f'День 14:00  | {day_now['air_temp'][2]} °C \n'
    #          f'Вечер 20:00 | {day_now['air_temp'][3]} °C\n\n'

    #          f'Температура воды\n'
    #          f'поверхность/глубина\n'
    #          f'{day_now['water_temp'][0]} °C / {day_now['water_temp'][1]} °C\n\n'

    #          f'Время | облачность\n'
    #          f'Ночь 02:00  | {day_now['cloudiness'][0]} % \n'
    #          f'Утро 08:00  | {day_now['cloudiness'][1]} % \n'
    #          f'День 14:00  | {day_now['cloudiness'][2]} % \n'
    #          f'Вечер 20:00 | {day_now['cloudiness'][3]} %\n\n'

    #          f'Время | давление\n'
    #          f'Ночь 02:00  | {day_now['pressure'][0]} мм. рт. ст. \n'
    #          f'Утро 08:00  | {day_now['pressure'][1]} мм. рт. ст. \n'
    #          f'День 14:00  | {day_now['pressure'][2]} мм. рт. ст. \n'
    #          f'Вечер 20:00 | {day_now['pressure'][3]} мм. рт. ст.\n\n'

    #     )


@router.message(F.text == 'Завтра')
async def tomorrow_answer(message: Message):
    pass


@router.message(F.text == 'На 5 дней')
async def on_five_day_answer(message: Message):
    pass
