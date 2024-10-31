from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from keyboards import reply_keyboards, inline_keyboards

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


@router.message(F.text == '🌅 Прогноз клёва')
async def bite_forecast_answer(message: Message):
    await message.answer(
        text='Астрологические и метеорологические рекомендации '
             'по лучшим дням и часам для ловли рыбы.\n\n'
             'Прогнозы на основе фаз луны и погодных изменений.',
        reply_markup=inline_keyboards.back_in_menu_kb
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



@router.message(F.text == 'Техники ловли')
async def guid_answer(message: Message):
    await message.answer(
        text='Указания по различным методам ловли '
        '(фидеры, спиннинг, поплавок и т.д.) '
        'с описанием особенностей и секретов.\n\n'
        'Советы по ловле определённых видов рыбы '
        '(щука, карп, лещ и др.).',
        reply_markup=inline_keyboards.back_in_menu_kb
    )


@router.message(F.text == 'Выбор снастей')
async def guid_answer(message: Message):
    await message.answer(
        text='Рекомендации по выбору удочек, '
        'катушек, лесок и приманок для различных '
        'видов рыбы и условий ловли.\n\n'
        'Пошаговые инструкции по сборке снасти.',
        reply_markup=inline_keyboards.back_in_menu_kb
    )


