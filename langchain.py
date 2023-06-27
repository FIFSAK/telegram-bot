from langchain.llms import OpenAI
import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)

llm.predict("What would be a good company name for a company that makes colorful socks?")


