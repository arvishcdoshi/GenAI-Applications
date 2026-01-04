import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os


from dotenv import load_dotenv
load_dotenv()


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


async def run_agent():
   client = MultiServerMCPClient(
       {

           "CustomFileSystem": {
               "command": "python",
               "args": [
                   "./custom_mcp/custom_mcp_server.py"
               ],
               "transport":"stdio"
           }

       }
   )
   tools = await client.get_tools()
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   response = await agent.ainvoke({"messages": "Add a new file called arvish.txt in GenAI-Applications"})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())