from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)

# tools = load_tools(["serpapi", "llm-math"], llm=llm)

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


def search_links_lch(response):
    query = llm.predict(f"give links of free resource for each topic to learn {response} CHECK THAT ALLL SITES ARE WORKING. IMPORTANT adjust to the limit of up to 4,096 characters. ")
    print(query)
    return query
