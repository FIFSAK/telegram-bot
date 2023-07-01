import asyncio
from aiogram import Bot, types
from linksCreating import search_links
bot_token = '6176941100:AAEPwvsTQAXYWpQ0RmGIA_nBH8nT1-KNQy0'  # вставьте токен вашего бота здесь
chat_id = '764803234'  # вставьте id чата, в который бот будет отправлять сообщения

bot = Bot(token=bot_token)


async def send_message():
    while not gather_links_done.is_set():
        await bot.send_message(chat_id, "wait a few minute")
        await asyncio.sleep(2)

async def some_async_function():
    # ваш асинхронный код здесь
    # для демонстрации, сделаем просто паузу в 2 минуты
    response = """(1) Learn programming languages such as Python, Java, or Ruby. 
# (2) Learn databases such as MySQL, PostgreSQL, or MongoDB."""
    a = search_links(response)
    await bot.send_message(chat_id, f"link ready {a}")

async def gather_links():
    await some_async_function()
    gather_links_done.set()

gather_links_done = asyncio.Event()

async def main():
    task1 = asyncio.create_task(send_message())
    task2 = asyncio.create_task(gather_links())
    
    await task2
    await task1

    await bot.close()

asyncio.run(main())