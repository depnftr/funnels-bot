import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8707251382:AAGF3Pjdtb_4-hVUG1wkA31Pn62QMeSlSgo"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Играть", url="https://t.me/FunnelsTV")],
            [InlineKeyboardButton(text="📺 Канал", url="https://t.me/FunnelsTV")],
            [InlineKeyboardButton(text="🎁 Пополнить инвентарь", url="https://t.me/funnelsbank")]
        ]
    )

    await message.answer(
        "Добро пожаловать в Funnels!",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if name == "__main__":
    asyncio.run(main())
