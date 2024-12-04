from typing import Optional

from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State

from keyboards import reply_keyboards, inline_keyboards
from parser import fishing_forecast
from config import moon_image
from generators import generate_response


router = Router()


class GetAiMessage(StatesGroup):
    send_message = State()


# @router.message(F.text == 'Спросить у нейросети')
# async def ai(message: Message, state: FSMContext):

#     res = await generate_response(message.text)
#     print(res)
#     await message.answer(res.choices[0].message.content)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='🎣 Привет, рыбак!\n\n'
             'Я твой виртуальный помощник в мире рыбалки! Я здесь, чтобы помочь тебе с выбором места для ловли, подсказать лучшие приманки и снасти, а также поделиться советами по технике ловли. \n\n'
             'Не знаешь, где ловить? Хочешь узнать о лучших сезонах для ловли? Или, может быть, интересуешься, как правильно ухаживать за уловом? Просто задай вопрос, и я с радостью помогу!\n'
             'Удачной рыбалки! 🐟',
        reply_markup=reply_keyboards.main_kb
    )


@router.message(StateFilter(None), F.text == 'Спросить у нейросети')
async def cmd_ai(message: Message, state: FSMContext):
    await message.answer(
        text='Задайте вопрос:'
    )
    await state.set_state(GetAiMessage.send_message)


@router.message(
        GetAiMessage.send_message,
        F.text != 'Спросить у нейросети'
)
async def get_ai_answer(message: Message, state: FSMContext):
    # await state.update_data()

    res = await generate_response(message.text)
    print(res)
    await message.answer(res.choices[0].message.content)


@router.message(F.text.lower() == '⬅ назад в меню')
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

@router.message(F.text == '📅 Завтра')
@router.message(F.text == '📆 Послезавтра')
async def tomorrow_answer(message: Message):

    data: dict = await fishing_forecast()

    if 'послезавтра' in message.text.lower():
        day_now = list(data.keys())[1]
    else:
        day_now = list(data.keys())[0]


    await message.answer(
        text='~~~~~~~~~~~~\n'
            f"<b>{data[day_now]['day']} {day_now}:</b>\n\n"
            "<u><i>Влияющие факторы:</i></u>\n"
            f"Температура воздуха: <b>{data[day_now]['air_temp']}</b> 🌡️\n"
            f"Давление: <b>{data[day_now]['pressure']}</b>\n"
            f"Ветер: <b>{data[day_now]['wind']} 💨</b>\n"
            f"Фаза луны: <b>{data[day_now]['moon_phase']}</b> {moon_image[data[day_now]['moon_phase']]}\n\n"
            f"{data[day_now]['discription']}\n"
            f'~~~~~~~~~~~~',
            parse_mode='html'
        )


@router.message(F.text == '🗓 На неделю')
async def on_five_day_answer(message: Message):

    data: dict = await fishing_forecast()

    day_now = list(data.keys())
    
    text = 'Прогноз клёва рыбы на 7 дней для <b>Ростов-на-Дону:</b>\n\n~~~~~~~~~~~~\n'
    
    for i in range(7):
        text += (
            f"<b>{data[day_now[i]]['day']} {day_now[i]}:</b>\n"
            
            "<u><i>Влияющие факторы:</i></u>\n"
            f"Температура воздуха: <b>{data[day_now[i]]['air_temp']}</b> 🌡️\n"
            f"Давление: <b>{data[day_now[i]]['pressure']}</b>\n"
            f"Ветер: <b>{data[day_now[i]]['wind']} 💨</b>\n"
            f"Фаза луны: <b>{data[day_now[i]]['moon_phase']}</b> {moon_image[data[day_now[i]]['moon_phase']]}\n\n"
            f"{data[day_now[i]]['discription']}\n\n"
            
            f'<i>{data[day_now[i]]["discription"]}</i>\n\n'
           '———————\n\n'
        )
    
    await message.answer(text, parse_mode='html')
        
        