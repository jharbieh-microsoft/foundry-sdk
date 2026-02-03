# Azure AI Foundry Agent Management & Framework Examples

This project provides tools for working with Azure AI Agents, including a management CLI and usage examples of the Microsoft Agent Framework.

## Project Contents

- **`agent.py`**: 
A command-line interface (CLI) for managing agents, listing resources, and testing chat interactions using the [Azure AI Projects SDK](https://pypi.org/project/azure-ai-projects/).

- **`agent-framework.py`**: 
A demonstration of the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), featuring a weather agent with streaming and non-streaming capabilities.

## Prerequisites

- Python 3.8+

- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed and authenticated

- Azure RBAC Role: [Azure Foundry RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-foundry?view=foundry&preserve-view=true) role (or higher) assigned on your Azure AI Foundry project

- [Azure AI Projects SDK](https://pypi.org/project/azure-ai-projects/) - Azure AI Foundry SDK for building AI applications

- [Azure Identity SDK](https://pypi.org/project/azure-identity/) - Azure authentication library

- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

## Azure Authentication Setup
This project uses `DefaultAzureCredential` for authentication, which automatically uses your Azure CLI credentials.

1. Install the Azure CLI from [here](https://learn.microsoft.com/cli/azure/install-azure-cli)
2. Log in to Azure:
   ```bash
   az login
   ```
3. Verify your login:
   ```bash
   az account show
   ```

### Required Azure RBAC Permissions

To create and manage AI agents in Azure AI Foundry, you need one of the following Azure RBAC roles assigned on your Azure AI Foundry project:

- **Azure AI Foundry Admin**: Full access to create, manage, and delete agents, configure resources, and manage team members.
- **Azure AI Foundry Developer**: Can create and manage agents, but cannot perform administrative tasks like managing project settings or team members.
- **Azure AI Foundry Contributor**: Has permissions to create and modify agents and resources within the project.

For more information, see [Azure Foundry RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-foundry?view=foundry&preserve-view=true).

NOTE: Azure AI Foundry RBAC roles may have changed given that Foundry is transitioning from classic to new. Check the documentation for the most up-to-date information.

## Installation

Install the required dependencies:

```bash
pip install azure-ai-projects azure-identity python-dotenv
pip install agent-framework --pre
```

### SDK Documentation

- [Azure AI Projects SDK](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme): Build and manage AI agents, run evaluations, and work with Azure AI Foundry projects
- [Azure Identity SDK](https://learn.microsoft.com/python/api/overview/azure/identity-readme): Provides Azure Active Directory token authentication support
- [python-dotenv](https://github.com/theskumar/python-dotenv): Reads key-value pairs from `.env` files
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework): A framework for building, orchestrating and deploying AI agents

## Usage

### Agent Management CLI (`agent.py`)

This script provides several commands to manage and interact with your Azure AI Agents.

#### Create an Agent
Creates a new agent using the configuration in your `.env` file.
```bash
python agent.py create_agent
```

#### Delete an Agent
Deletes an agent by its ID.
```bash
python agent.py delete_agent <agent_id>
```

#### List all Agents
Displays a list of all agents in the project.
```bash
python agent.py list_agents
```

#### List Deployments
Shows all model deployments in the project.
```bash
python agent.py list_deployments
```

#### Chat with Model (Basic)
Sends a simple test message ("How many feet are in a mile?") to the model deployment directly.
```bash
python agent.py chat_with_agent
```

#### Chat with Specific Agent
Interacts with a specific agent by ID. This creates a thread, sends a user message, runs the agent, and retrieves the response.
```bash
python agent.py chat_with_specific_agent <agent_id>
```

### Microsoft Agent Framework Demo (`agent-framework.py`)

This script demonstrates the usage of the Microsoft Agent Framework to create a functional agent with custom tools.

It creates a `BasicWeatherAgent` equipped with a `get_weather` tool and runs two examples:
1. Non-streaming: Waits for the full response.
2. Streaming: Displays the response chunk-by-chunk as it is generated.

To run the demo:
```bash
python agent-framework.py
```

