from dotenv import load_dotenv
load_dotenv()
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent

# Stored in RAM
checkpointer = InMemorySaver()
agent = create_react_agent(
   model="groq:llama-3.3-70b-versatile",
   tools=[],
   checkpointer=checkpointer,
   prompt="You are a helpful assistant"
)


config = {"configurable": {"thread_id": "1"}}
first_response = agent.invoke(
   {"messages": [{"role": "user", "content": "Who is Virat Kohli"}]},
   config
)
second_response = agent.invoke(
   {"messages": [{"role": "user", "content": "When was he born?"}]},
   config
)
print(first_response)
print('-------------')
print(second_response)