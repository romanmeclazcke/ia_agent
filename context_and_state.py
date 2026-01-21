from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from typing import cast
from schemas.colour_state import ColourState
from tools.favorite_color import get_colour

load_dotenv()


memory = InMemorySaver()
model = ChatOpenAI(model="gpt-4o-mini")

agent = create_agent(
    model=model,
    context_schema=ColourState,
    tools=[get_colour],
    checkpointer=memory
)

# Create an instance of ColourState with the context
colour_context = ColourState(favourite_color="Red", least_favourite_color="Green")

# Config with thread_id
config = cast(
    RunnableConfig,
    {
        "configurable": {
            "thread_id": "1",
            "context": colour_context, # Here we pass the context
        },
    },
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is my favourite color ?"}]},
    config=config
)

print(response)
