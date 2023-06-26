import os
import dotenv
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from main import make_request
from majors import majors_dataset
from survey import survey
dotenv.load_dotenv(dotenv.find_dotenv())
global personal_preferences_flag 
global survey_flag
personal_preferences_flag = False
survey_flag = False
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(bot)

chat_id = 764803234

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm your roadmap assistant!.")



@dp.message_handler(commands=['command1'])
async def send_command1(message: types.Message):
    keyboard_command1 = types.InlineKeyboardMarkup()
    
    button1 = types.InlineKeyboardButton("Show list of majors", callback_data='majors')
    button2 = types.InlineKeyboardButton("I have some skills", callback_data='skills')
    button3 = types.InlineKeyboardButton("Take a survey", callback_data='survey')

    keyboard_command1.add(button1, button2, button3)
    
    await message.reply("Please choose an option:", reply_markup=keyboard_command1)

@dp.callback_query_handler(lambda c: c.data == 'majors')
async def process_callback_majors(callback_query: types.CallbackQuery):
    global personal_preferences_flag
    global survey_flag
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, majors_dataset, parse_mode='Markdown')
    personal_preferences_flag = False
    survey_flag = False

@dp.callback_query_handler(lambda c: c.data == 'skills')
async def process_callback_skills(callback_query: types.CallbackQuery):
    global personal_preferences_flag
    global survey_flag
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Which back graound you have and who do you want to be?")
    personal_preferences_flag = True
    survey_flag = False
    

@dp.callback_query_handler(lambda c: c.data == 'survey')
async def process_callback_survey(callback_query: types.CallbackQuery):
    global personal_preferences_flag
    global survey_flag
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, survey,  parse_mode='Markdown')
    survey_flag = True
    personal_preferences_flag = False


@dp.message_handler()
async def responce_skills(message: types.Message):
    global personal_preferences_flag
    global survey_flag
    if personal_preferences_flag:
        response = make_request(message.text, """I want you to be a roadmap assistant. 
        I will provide programming skills that I already have and in which area I want to be a specialist. 
        You will provide a list of topics that need to be further studied and immediately in the order of study. 
        If I do not provide in which area I want to be a specialist, then you will offer no more than three professions based on the skills you already own and make a roadmap.
        Does not answer topics not related to IT and work, the answer should contain only a roadmap and no greetings, wishes, nothing more.""")
        await bot.send_message(chat_id, response)
        personal_preferences_flag = False    
    if survey_flag:
        answers = message.text.split()
        if len(answers)!=20:
            await bot.send_message(chat_id, "you did not answer all 20 questions or did not close the gaps between the answers, answer again")
        else:
            response = make_request(f"""Do you enjoy solving complex mathematical problems? ({answers[0]})\n- 
                                    Are you comfortable working with numbers and statistics? ({answers[1]})\n- 
                                    Do you have strong attention to detail? ({answers[2]})\n- 
                                    Are you creative and enjoy designing or drawing? ({answers[3]})\n- 
                                    Do you like working with people and helping them solve their problems? ({answers[4]})\n- 
                                    Do you prefer working in a team or on your own? ({answers[5]})\n- 
                                    Are you interested in how software applications work or more fascinated by how the hardware operates? ({answers[6]})\n- 
                                    Do you enjoy reading and writing more than playing with gadgets? ({answers[7]})\n- 
                                    Are you interested in exploring new technological trends like Artificial Intelligence and Machine Learning? ({answers[8]})\n- 
                                    Do you prefer a role that involves a lot of analysis and problem solving? ({answers[9]})\n- 
                                    Are you more interested in web development (working on websites and web applications) or mobile development (creating apps for smartphones and tablets)? ({answers[10]})\n- 
                                    Do you like to play video games? Would you be interested in creating them? ({answers[11]})\n- 
                                    Do you have good communication skills and would like a role that involves a lot of interaction with clients and team members? ({answers[12]})\n- 
                                    Do you enjoy taking a large amount of information and organizing it in a meaningful way? ({answers[13]})\n- 
                                    Are you intrigued by cyber security and the thought of protecting systems from threats? ({answers[14]})\n- 
                                    Do you enjoy learning new languages (like programming languages)? ({answers[15]})\n- 
                                    Are you interested in the business side of technology, like project management or business analysis? ({answers[16]})\n- 
                                    Would you prefer a job that is constantly evolving and requires continuous learning? ({answers[17]})\n- 
                                    Are you comfortable with abstraction and conceptualizing ideas? ({answers[18]})\n- 
                                    Do you like to troubleshoot and fix things when they go wrong? ({answers[19]})""", "Given the following responses to a set of questions, please suggest the most suitable specialty in the IT field. briefly and clearly within 40 tokens, if for 40 tokens you managed to finish earlier. answer must be finished by dot. the answer does not need to enumerate the qualities of a person", 40)
            await bot.send_message(chat_id, response)
            response = make_request(response ,f"""I want you to be a roadmap assistant. I will provide in which area I want to be a specialist. 
You will provide a list of topics that need to be further studied and immediately in the order of study like roadmap.""")
            await bot.send_message(chat_id, response)
            survey_flag = False


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task(send_message_from_terminal())  # start the send_message_from_terminal task
    executor.start_polling(dp, skip_updates=True)
