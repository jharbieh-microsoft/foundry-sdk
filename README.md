# Azure AI Foundry Agent SDK and Agent Framework Examples
This project provides tools for working with Azure AI Agents, including a management CLI and usage examples of the Microsoft Agent Framework.

## Prerequisites
- Python 3.8+

- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

- [Azure Foundry RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-foundry?view=foundry&preserve-view=true)

- [Azure AI Projects SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python)

- [Azure Identity SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python)

- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Authentication Setup
This project uses `DefaultAzureCredential` for authentication, which automatically uses your Azure CLI credentials.

1. Install the Azure CLI
2. Log in to Azure:
   ```bash
   az login
   ```
3. Verify your login:
   ```bash
   az account show
   ```
## RBAC Permissions Setup

To create and manage AI agents in Azure AI Foundry, you need one of the following Azure RBAC roles assigned on your Azure AI Foundry project:

- Azure AI User

For more information, see [Azure Foundry RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-foundry?view=foundry&preserve-view=true)

## Create and Activate a Python Virtual Environment named venv for (agent-framework-a.py, agent-framework-b.py)
It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies for venv virtual environment
Install the required dependencies:

```bash
pip install azure-ai-projects azure-identity python-dotenv
pip install agent-framework --pre
```

### Deactivate the venv virtual environment
After you're done working in the virtual environment, you can deactivate it:

```bash
deactivate
```

## Create and Activate a Python Virtual Environment named venv2 (foundry.py)
It's recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv2
source venv2/bin/activate  # On Windows use `venv2\Scripts\activate`
```
### Install dependencies for venv2 virtual environment
Install the required dependencies:

```bash
pip install python-dotenv
pip install agent-framework-azure-ai --pre
pip install azure-ai-projects azure-identity
```

### Deactivate the venv2 virtual environment
After you're done working in the virtual environment, you can deactivate it:

```bash  
deactivate
```

## Verify Installation
Check that the packages are installed correctly:

```bash
pip list
```

```bash
python -c "import agent_framework.azure; print(dir(agent_framework.azure))"
```

## Usage

### Agent Management CLI (`foundry.py`)

This script provides several commands to manage and interact with your Azure AI Agents.

#### Create an Agent
Creates a new agent using the configuration in your `.env` file.
```bash
python foundry.py create_agent
```

#### Delete an Agent
Deletes an agent by its ID.
```bash
python foundry.py delete_agent <agent_id>
```

#### List all Agents
Displays a list of all agents in the project.
```bash
python foundry.py list_agents
```

#### List Deployments
Shows all model deployments in the project.
```bash
python foundry.py list_deployments
```

#### Chat with Model (Basic)
Sends a simple test message ("How many feet are in a mile?") to the model deployment directly.
```bash
python foundry.py chat_with_agent
```

#### Chat with Specific Agent
Interacts with a specific agent by ID. This creates a thread, sends a user message, runs the agent, and retrieves the response.
```bash
python foundry.py chat_with_specific_agent <agent_id>
```

## Reading Materials
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

- [Microsoft Agent Framework agent types](https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/agent-types/?pivots=programming-language-python)