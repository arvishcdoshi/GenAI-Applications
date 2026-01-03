import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

# Tools
def addFile(filename: str) -> str:
    """Create a new file in current directory"""
    if not os.path.exists(filename):
        with open(filename, "w"):
            pass
        return f"File '{filename}' created."
    return f"File '{filename}' already exists."


def addFolder(directory_name: str) -> str:
    """Create a new Directory in current directory"""
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created."
    return f"Directory '{directory_name}' already exists."


# Pre-built agent

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[addFile, addFolder],
    system_prompt="You are a helpful assistant that manages files and directories."
)

# Run the agent

response = agent.invoke(
    {"messages": [{"role": "user", "content": "create a new directory with name apps"}]}
)

print(response)
