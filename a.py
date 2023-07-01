import asyncio
from aiogram import Bot, types
from googlesearch import search
import concurrent.futures
from linksCreating import search_links
bot_token = '6176941100:AAEPwvsTQAXYWpQ0RmGIA_nBH8nT1-KNQy0'
chat_id = '764803234'

bot = Bot(token=bot_token)
response ="""(1) Learn and take a course on programming languages such as Python, Java, or Ruby.
    (2) Learn and take a course on databases such as MySQL, PostgreSQL, or MongoDB.
    (3) Learn and take a course on web frameworks such as Django, Flask, or Ruby on Rails.
    (4) Learn and take a course on version control systems such as Git.
    (5) Learn and take a course on server management and deployment using tools such as Docker, Kubernetes, or AWS.
    (6) Learn and take a course on testing frameworks such as Pytest or JUnit.
    (7) Learn and take a course on security best practices for web applications."""
async def send_message():
    while not gather_links_done.is_set():
        await bot.send_message(chat_id, "Wait a few seconds...")
        await asyncio.sleep(2)


async def gather_links(response):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        links = await loop.run_in_executor(pool, search_links, response)
        gather_links_done.set()
        return links

gather_links_done = asyncio.Event()

async def main(response):
    task1 = asyncio.create_task(send_message())
    task2 = asyncio.create_task(gather_links(response))

    results = await asyncio.gather(task1, task2)

    await bot.close()

    return results[1]  # gather_links result is in the second position


loop = asyncio.get_event_loop()
links = loop.run_until_complete(main(response))
response = response.split("\n")
for i in range(len(links)):
    response[i] = response[i] + f"({links[i]})\n"
response = " ".join(response)

bot.send_message(chat_id, response)
