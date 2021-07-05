from loader import dp
from aiogram.types import Message
from keyboards.default import menu
from aiogram.dispatcher.filters import Command

@dp.message_handlers(Command("menu"))
async def show_menu (message:Message):
    await message.answer('Выберите товар из меню ниже', reply_markup=menu)
