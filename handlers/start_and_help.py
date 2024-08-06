from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def start_handlers(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

