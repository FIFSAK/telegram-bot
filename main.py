import os
import dotenv
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio

dotenv.load_dotenv(dotenv.find_dotenv())



openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)



def make_request(message:  types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
                {"role": "system", "content": "You are a assistant which give list of majors in programming."},
                {"role": "user", "content": f"'{message.text}'"},
            ]
        )

    return response['choices'][0]['message']['content']