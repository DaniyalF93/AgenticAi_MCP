import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
import dotenv
import os

dotenv.load_dotenv()


async def main():
    config_file = "browser-mcp.json"
    client = MCPClient.from_config_file(filepath=config_file)

    # Create LLM
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    # Create agent with tools
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    # Run the query
    result = await agent.run("Find the best restaurant in San Francisco")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
