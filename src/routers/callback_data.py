from typing import Optional

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards import reply_keyboards, inline_keyboards

router = Router()  # [2]


@router.callback_query(F.data == 'back_in_menu')
async def back_in_main_menu(callback: CallbackQuery, state: Optional[FSMContext]=None):
    
    await callback.answer()
    
    await callback.message.bot.delete_message(
        chat_id=callback.message.chat.id, 
        message_id=callback.message.message_id
    )

    await callback.message.answer(
        "Вы вернулись в главное меню", 
        reply_markup=reply_keyboards.main_kb
    )

    if state:
        await state.clear()
