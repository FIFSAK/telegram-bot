from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# response = """(1) Learn programming languages such as Python, Java, or Ruby. 
# (2) Learn databases such as MySQL, PostgreSQL, or MongoDB."""
# response = response.split("\n")
# result = []
# for i in response:
#     result.append(agent.run(f"give 1 link of free resource for each topic to learn {i} CHECK THAT ALLL SITES ARE WORKING "))
# print("result is", result)

def search_links_lch(response):
    links = []
    response = response.split("\n")
    for i in response:
        query = llm.predict(f"give 1 link of free resource for each topic to learn {i} CHECK THAT ALLL SITES ARE WORKING ")
        links.append(query)
        print(links)
    return links


# response = """(1) Learn programming languages such as Python, Java, or Ruby. 
# (2) Learn databases such as MySQL, PostgreSQL, or MongoDB."""

# print(search_links_lch(response))



