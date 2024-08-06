from aiogram import F, Router, types

router = Router()


@router.message(lambda message: message.text.lower() in ['urban', 'ff'])
async def urban_message(message: types.Message):
    print('Urban message')
    await message.answer('Urban message')


@router.message(F.text)
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')
