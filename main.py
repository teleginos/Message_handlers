import asyncio

from handlers import others, start_and_help
from loader import bot, dp


async def main():
    dp.include_router(start_and_help.router)
    dp.include_router(others.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
