import asyncio
import aiohttp
from lxml import html
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

API_TOKEN = 'your-telegram-bot-api-token'
URL = 'https://your-url-here.com'
CHAT_ID = 'your-chat-id'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
stop_signal = asyncio.Event()
target_text = "Yüksek oran" 
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def check_website():
    async with aiohttp.ClientSession() as session:
        while not stop_signal.is_set():
            try:
                page_content = await fetch(session, URL)
                tree = html.fromstring(page_content)
                if target_text in tree.text_content():
                    await bot.send_message(chat_id=CHAT_ID, text=f'Text "{target_text}" found on the website!')
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
            await asyncio.sleep(10)  # 10 saniye bekle

@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    stop_signal.clear()
    asyncio.create_task(check_website())
    await message.answer("Bot is monitoring the website.")

@router.message(Command(commands=["stop"]))
async def stop(message: types.Message):
    stop_signal.set()
    await message.answer("Stopped monitoring the website.")

@router.message(Command(commands=["change"]))
async def change_target(message: types.Message):
    global target_text
    new_target = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if new_target:
        target_text = new_target
        await message.answer(f"Target text changed to: {target_text}")
    else:
        await message.answer("Please provide the new target text after the command, e.g., /change new text")

async def on_startup():
    await bot.set_my_commands([BotCommand(command="start", description="Start monitoring"),
                               BotCommand(command="stop", description="Stop monitoring"),
                               BotCommand(command="change", description="Change target text")])

async def main():
    dp.include_router(router)
    await on_startup()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
