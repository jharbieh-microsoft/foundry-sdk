import os
import time
import asyncio
import argparse
from zipfile import Path

from dotenv import load_dotenv

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import CodeInterpreterTool
from azure.ai.agents.models import ListSortOrder

# Load environment variables from .env file
load_dotenv()

# Initialize the AI Project Client
project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Create an agent
def create_agent():
    agent = project_client.agents.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name=os.environ["AGENT_NAME"],
        instructions="You are my helpful agent",
    )
    print(f"Created agent, agent ID: {agent.id}")
    return agent

# Delete an agent by ID
def delete_agent(agent_id):
    project_client.agents.delete_agent(agent_id)
    print(f"Deleted agent with ID: {agent_id}")


# List all agents
def list_agents():
    agents = project_client.agents.list_agents()
    for agent in agents:
        print(f"Agent ID: {agent.id}")
        print(f"Agent Name: {agent.name}")

# List all deployments
def list_deployments():
    deployments = project_client.deployments.list()
    for deployment in deployments:
        print(f"Deployment Name: {deployment.name}")

# Chat completion with the agent
def chat_with_agent():
    with project_client.get_openai_client(api_version="2024-10-21") as client:

        response = client.chat.completions.create(
            model=os.environ["MODEL_DEPLOYMENT_NAME"],
            messages=[
                {
                    "role": "user",
                    "content": "How many feet are in a mile?",
                },
            ],
        )

        print(response.choices[0].message.content)

# Chat with a specific agent using its ID
def chat_with_specific_agent(agent_id):
    agent = project_client.agents.get_agent(agent_id)
    print(f"Chatting with agent: {agent.name}")

     # Create a thread for communication
    thread = project_client.agents.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Example question to ask the agent
    question = """Hello, can you help me understand the benefits of using Azure AI services for building intelligent applications?"""

    # Add a message to the thread
    message = project_client.agents.messages.create(
        thread_id=thread.id,
        role="user",  # Role of the message sender
        content=question,  # Message content
    )
    print(f"Created message, ID: {message['id']}")

    # Get the agent's response
    # Create and process an agent run
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id,
        additional_instructions="""Please address the user as Jane Doe.
        The user has a premium account.""",
    )

    print(f"Run finished with status: {run.status}")

    # Check if the run failed
    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # Fetch and log all messages
    messages = project_client.agents.messages.list(thread_id=thread.id)
    print(f"Messages: {messages}")

    for message in messages:
        print(f"Role: {message.role}, Content: {message.content}")
        for this_content in message.content:
            print(f"Content Type: {this_content.type}, Content Data: {this_content}")
            if this_content.text.annotations:
                for annotation in this_content.text.annotations:
                    print(f"Annotation Type: {annotation.type}, Text: {annotation.text}")
                    print(f"Start Index: {annotation.start_index}")
                    print(f"End Index: {annotation.end_index}")

def main():
    parser = argparse.ArgumentParser(description="Agent management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # create_agent command
    subparsers.add_parser("create_agent", help="Create a new agent")
    
    # delete_agent command
    delete_parser = subparsers.add_parser("delete_agent", help="Delete an agent")
    delete_parser.add_argument("agent_id", help="The ID of the agent to delete")

    # list_agents command
    subparsers.add_parser("list_agents", help="List all agents")

    # list_deployments command
    subparsers.add_parser("list_deployments", help="List all deployments")
    
    # chat_with_agent command
    subparsers.add_parser("chat_with_agent", help="Chat with an agent")

    # chat_with_specific_agent command
    chat_specific_parser = subparsers.add_parser("chat_with_specific_agent", help="Chat with a specific agent")
    chat_specific_parser.add_argument("agent_id", help="The ID of the agent to chat with")

    args = parser.parse_args()
    
    if args.command == "create_agent":
        create_agent()
    elif args.command == "delete_agent":
        delete_agent(args.agent_id)
    elif args.command == "list_agents":
        list_agents()
    elif args.command == "list_deployments":
        list_deployments()
    elif args.command == "chat_with_agent":
        chat_with_agent()
    elif args.command == "chat_with_specific_agent":
        chat_with_specific_agent(args.agent_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()