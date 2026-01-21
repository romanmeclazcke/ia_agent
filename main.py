from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from typing import cast
from schemas.pais import PaisInformation
from tools.send_email import send_pais_information_message
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# Create checkPointer
memory = InMemorySaver()
model = ChatOpenAI(model="gpt-4o-mini")

agent = create_agent(
    model=model,
    system_prompt=(
        "You are a geography expert. "
        "Remember the user's preferences throughout the conversation. "
        "You MUST generate information ONLY about the country explicitly provided by the user. "
        "Never change the country unless the user explicitly asks for a different one."
    ),
    response_format=PaisInformation,
    tools=[send_pais_information_message],
    checkpointer=memory
)

# Config thread_id 
config = cast(RunnableConfig, {"configurable": {"thread_id": "1"}})

response1 = agent.invoke(
    {"messages": [{"role": "user", "content": "My favorite country is Argentina"}]},
    config
)

# here the Agent response with its memory knowledge
response2 = agent.invoke(
    {"messages": [{"role": "user", "content": "Tell me more about my favorite country"}]},
    config
)

pais: PaisInformation = response2["structured_response"]
print(pais)
print(f"País: {pais.spanish_name}")
print(f"Habitantes: {pais.number_of_inhabitants}")
