from langchain.llms import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)


def search_links_lch(response):
    links = []
    response = response.split("\n")
    for i in response:
        query = llm.predict(f"give 1 link of free resource for each topic to learn {i} CHECK THAT ALLL SITES ARE WORKING ")
        links.append(query)
    return links


# response = """(1) Learn programming languages such as Python, Java, or Ruby. 
# (2) Learn databases such as MySQL, PostgreSQL, or MongoDB."""

# print(search_links_lch(response))

# links =['\n\n1. Python: https://www.codecademy.com/learn/learn-python\n2. Java: https://www.codecademy.com/learn/learn-java\n3. Ruby: https://www.codecademy.com/learn/learn-ruby', '\n\n1. MySQL: https://www.mysqltutorial.org/\n2. PostgreSQL: https://www.postgresqltutorial.com/\n3. MongoDB: https://university.mongodb.com/']

