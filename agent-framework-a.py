# This is an example of creating a basic Azure AI Agent Framework agent with a simple weather tool.

# Import necessary libraries
import argparse
import asyncio
import os
from random import randint
from typing import Annotated
from pydantic import Field

from dotenv import load_dotenv

from agent_framework import ChatAgent, AgentThread
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

# Load environment variables from .env file
load_dotenv()

def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."

# Example of a Basic Foundry Agent
async def basic_agent() -> None:
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentClient(credential=credential).as_agent(
            name="HelperAgent",
            instructions="You are a helpful digital assistant."
        ) as agent,
    ):
        result = await agent.run("Briefly describe agent framework agent types.")
        print(result.text)

# Example using an existing Foundry Agent by ID
# Expects an ID that begins with 'asst'.
async def existing_agent() -> None:
    # Define agent name and make sure it begins with an 'asst' prefix
    agent_name = os.environ["AGENT_NAME_CLASSIC"]

    async with (
        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(
                credential=credential,
                agent_id=agent_name,
            ),
            instructions="You are a helpful digital assistant agent."
        ) as agent,
    ):
        result = await agent.run("Briefly describe agentic commerce.")
        print(result.text)

# Example of a ChatAgent using Agent Framework with a tool
async def chat_agent_with_tool() -> None:
    # Create a ChatAgent with Azure AI client
    async with (
        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(credential=credential),
            instructions="You are a helpful digital assistant agent.",
            tools=get_weather,
        ) as agent,
    ):
        # Agent is now ready to use
        # Create the agent thread for ongoing conversation
        thread = agent.get_new_thread()

        # Ask questions and get responses
        first_query = "What's the weather like in Seattle?"
        print(f"User: {first_query}")

        first_result = await agent.run(first_query, thread=thread)
        print(f"Agent: {first_result.text}")

# Main entry point
async def main() -> None:
    parser = argparse.ArgumentParser(description="Azure AI Agent Framework Examples")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("basic", help="Run basic agent example")
    subparsers.add_parser("existing", help="Run existing agent example")
    subparsers.add_parser("chat_tool", help="Run chat agent with tool example")

    args = parser.parse_args()

    if args.command == "basic":
        await basic_agent()
    elif args.command == "existing":
        await existing_agent()
    elif args.command == "chat_tool":
        await chat_agent_with_tool()
    else:
        parser.print_help()


if __name__ == "__main__":
    asyncio.run(main())