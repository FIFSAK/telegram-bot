# import os
# import dotenv
# import openai
# import logging
# from aiogram import Bot, Dispatcher, executor, types
# import asyncio

# dotenv.load_dotenv(dotenv.find_dotenv())




# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=os.getenv("API_TOKEN"))
# dp = Dispatcher(bot)

# chat_id = 764803234

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     global chat_id
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# @dp.message_handler()
# async def echo(message: types.Message):
#     response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo", 
#       messages=[
#             {"role": "system", "content": "You are a translater assistant only from english to russian if you see another language say no."},
#             {"role": "user", "content": f"Translate this English text to Russian: '{message.text}'"},
#         ]
#     )

#     response = response['choices'][0]['message']['content']
#     await bot.send_message(chat_id, response)




# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     # loop.create_task(send_message_from_terminal())  # start the send_message_from_terminal task
#     executor.start_polling(dp, skip_updates=True)