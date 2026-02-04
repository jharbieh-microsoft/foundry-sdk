# This is an example of creating a basic Azure AI Agent Framework agent with a simple weather tool.

# Use the venv Python virtual environment

# Import necessary libraries
import argparse
import asyncio
from json import tool
import os
from random import randint
from typing import Annotated
from pydantic import Field

from dotenv import load_dotenv

from agent_framework import ChatAgent, AgentThread
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity.aio import AzureCliCredential

# Load environment variables from .env file
load_dotenv()

def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."

# Example of non-streaming response
async def non_streaming_agent() -> None:
    """Example of non-streaming response (get the complete result at once)."""
    print("=== Non-streaming Response Example ===")

    # For authentication, run `az login` command in terminal or replace AzureCliCredential with preferred
    # authentication option.
    async with (
        AzureCliCredential() as credential,
        AzureAIProjectAgentProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="BasicWeatherAgent",
            instructions="You are a helpful weather agent.",
            tools=get_weather,
        )

        query = "What's the weather like in Seattle?"
        print(f"User: {query}")
        result = await agent.run(query)
        print(f"Agent: {result}\n")

# Example of streaming response
async def streaming_agent() -> None:
    """Example of streaming response (get results as they are generated)."""
    print("=== Streaming Response Example ===")

    # For authentication, run `az login` command in terminal or replace AzureCliCredential with preferred
    # authentication option.
    async with (
        AzureCliCredential() as credential,
        AzureAIProjectAgentProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="BasicWeatherAgent",
            instructions="You are a helpful weather agent.",
            tools=get_weather,
        )

        query = "What's the weather like in Tokyo?"
        print(f"User: {query}")
        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream(query):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print("\n")

# Main entry point
async def main() -> None:
    parser = argparse.ArgumentParser(description="Azure AI Agent Framework Examples")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.add_parser("non_streaming", help="Run non-streaming agent example")
    subparsers.add_parser("streaming", help="Run streaming agent example")

    args = parser.parse_args()

    if args.command == "non_streaming":
        await non_streaming_agent()
    elif args.command == "streaming":
        await streaming_agent()
    else:
        parser.print_help()


if __name__ == "__main__":
    asyncio.run(main())