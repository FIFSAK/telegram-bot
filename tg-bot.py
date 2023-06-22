import os
import dotenv
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from main import make_request


dotenv.load_dotenv(dotenv.find_dotenv())


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(bot)

chat_id = 764803234

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm your roadmap assistant!\n.")


@dp.message_handler()
async def echo(message: types.Message):
    response = make_request(message)
    await bot.send_message(chat_id, response)




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task(send_message_from_terminal())  # start the send_message_from_terminal task
    executor.start_polling(dp, skip_updates=True)