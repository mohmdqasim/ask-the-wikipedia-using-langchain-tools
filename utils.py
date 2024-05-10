from langchain_openai import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7)

tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

def get_wikipedia_answer(query: str):
    answer = agent.run(query)
    return answer