# VSCode-Foundry Project Visual Code Map

## Project Structure
```
vscode-foundry/
├── agent.py                 (Azure AI Agent Management CLI)
├── agent-framework.py       (Weather Agent with Streaming/Non-streaming)
├── .env                     (Environment Configuration)
├── .gitignore
├── README.md
├── INSTRUCTIONS.md
├── .agentframework
├── .venv/
└── __pycache__/
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      vscode-foundry Project                      │
└─────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
    ┌───────────────────────┐       ┌──────────────────────────┐
    │   agent.py            │       │  agent-framework.py      │
    │   (Management CLI)    │       │  (Agent Framework Demo)  │
    └───────────────────────┘       └──────────────────────────┘
                │                               │
                │                               │
                ▼                               ▼
    ┌───────────────────────┐       ┌──────────────────────────┐
    │  AIProjectClient      │       │ AzureAIProjectAgent      │
    │  (Azure AI Projects)  │       │ Provider                 │
    └───────────────────────┘       └──────────────────────────┘
                │                               │
                │                               │
                └───────────┬───────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Azure AI Services   │
                │   - Model Deployment  │
                │   - Agent Runtime     │
                └───────────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   .env Configuration  │
                │   - PROJECT_ENDPOINT  │
                │   - MODEL_DEPLOYMENT  │
                │   - AGENT_NAME        │
                └───────────────────────┘
```

---

## agent.py - Code Flow

```
┌──────────────────────────────────────────────────────────────┐
│                        agent.py                               │
│                    Command Line Interface                     │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   main()      │
                    │   (ArgParser) │
                    └───────────────┘
                            │
        ┌───────────────────┼──────────────────┬────────────────┐
        │                   │                  │                │
        ▼                   ▼                  ▼                ▼
┌──────────────┐   ┌──────────────┐   ┌─────────────┐  ┌─────────────┐
│create_agent()│   │delete_agent()│   │list_agents()│  │list_deploy  │
│              │   │              │   │             │  │ments()      │
└──────────────┘   └──────────────┘   └─────────────┘  └─────────────┘
        │                   │                  │                │
        └───────────────────┴──────────────────┴────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │  AIProjectClient      │
                │  - create_agent()     │
                │  - delete_agent()     │
                │  - list_agents()      │
                │  - list_deployments() │
                └───────────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │ chat_with_agent()     │
                │ (OpenAI Client)       │
                │ - Chat Completion API │
                └───────────────────────┘
```

### agent.py - Commands Available
```
┌─────────────────────────────────────────────────────────┐
│ Command              │ Action                           │
├─────────────────────────────────────────────────────────┤
│ create_agent         │ Creates new AI agent             │
│ delete_agent <id>    │ Deletes agent by ID              │
│ list_agents          │ Lists all agents                 │
│ list_deployments     │ Lists all model deployments      │
│ chat_with_agent      │ Sends chat completion request    │
└─────────────────────────────────────────────────────────┘
```

---

## agent-framework.py - Code Flow

```
┌──────────────────────────────────────────────────────────────┐
│                   agent-framework.py                          │
│              Azure AI Agent Framework Demo                    │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   main()      │
                    │   (async)     │
                    └───────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
        ▼                                       ▼
┌─────────────────────┐              ┌─────────────────────┐
│non_streaming_       │              │streaming_example()  │
│example()            │              │                     │
└─────────────────────┘              └─────────────────────┘
        │                                       │
        │                                       │
        └───────────────┬───────────────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │ AzureAIProjectAgent   │
            │ Provider              │
            │                       │
            │ - create_agent()      │
            │ - agent.run()         │
            │ - agent.run_stream()  │
            └───────────────────────┘
                        │
                        │ uses
                        ▼
            ┌───────────────────────┐
            │ @tool                 │
            │ get_weather()         │
            │                       │
            │ - location param      │
            │ - returns weather     │
            │   conditions          │
            └───────────────────────┘
```

### agent-framework.py - Response Modes
```
┌─────────────────────────────────────────────────────────────┐
│               Response Mode Comparison                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  NON-STREAMING              │  STREAMING                    │
│  ════════════               │  ═════════                    │
│  agent.run(query)           │  agent.run_stream(query)      │
│      │                      │      │                        │
│      ▼                      │      ▼                        │
│  [Wait for complete]        │  [Chunks arrive]              │
│      │                      │      │                        │
│      ▼                      │      ▼                        │
│  Display full result        │  async for chunk in stream:   │
│                             │      print(chunk.text)        │
│                             │                               │
│  Use Case:                  │  Use Case:                    │
│  - Simple queries           │  - Real-time feedback         │
│  - Batch processing         │  - Long responses             │
│                             │  - Better UX                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌──────────────┐
│ User/CLI     │
│ Command      │
└──────┬───────┘
       │
       │ python agent.py create_agent
       ▼
┌──────────────────┐
│ argparse         │
│ (Command Router) │
└──────┬───────────┘
       │
       ▼
┌──────────────────────────┐
│ load_dotenv()            │
│ Load .env file           │
│ - PROJECT_ENDPOINT       │
│ - MODEL_DEPLOYMENT_NAME  │
│ - AGENT_NAME             │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ DefaultAzureCredential() │
│ Authentication           │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ AIProjectClient          │
│ Initialize connection    │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Execute Command          │
│ - create_agent()         │
│ - delete_agent()         │
│ - list_agents()          │
│ - list_deployments()     │
│ - chat_with_agent()      │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Azure AI Services        │
│ Process Request          │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Return Response          │
│ Display to User          │
└──────────────────────────┘
```

---

## Function Tool Integration

```
┌─────────────────────────────────────────────────────────────┐
│              @tool Decorator Pattern                         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │ @tool(approval_mode="...")    │
            │ def get_weather(location):    │
            └───────────────────────────────┘
                            │
        ┌───────────────────┼──────────────────┐
        │                   │                  │
        ▼                   ▼                  ▼
┌─────────────┐    ┌──────────────┐   ┌──────────────┐
│ Type        │    │ Validation   │   │ Description  │
│ Annotations │    │ via Pydantic │   │ for Agent    │
│             │    │ Field        │   │              │
└─────────────┘    └──────────────┘   └──────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │ Agent can call function       │
            │ automatically when needed     │
            │ during conversation           │
            └───────────────────────────────┘
```

---

## Dependencies & Imports

```
┌─────────────────────────────────────────────────────────────┐
│                    agent.py Dependencies                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐    ┌──────────────────┐             │
│  │ azure.ai.projects│    │ azure.identity   │             │
│  │ AIProjectClient  │    │ DefaultAzure     │             │
│  │                  │    │ Credential       │             │
│  └──────────────────┘    └──────────────────┘             │
│           │                       │                         │
│           └───────────┬───────────┘                         │
│                       │                                     │
│  ┌──────────────────┐ │  ┌──────────────────┐             │
│  │ azure.ai.agents  │ │  │ python-dotenv    │             │
│  │ Models, Tools    │ │  │ load_dotenv()    │             │
│  └──────────────────┘ │  └──────────────────┘             │
│                       │                                     │
│  ┌──────────────────┐ │  ┌──────────────────┐             │
│  │ Standard Library │ │  │ argparse         │             │
│  │ os, time, asyncio│ │  │ CLI parsing      │             │
│  └──────────────────┘ │  └──────────────────┘             │
└───────────────────────┴─────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              agent-framework.py Dependencies                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │ agent_framework.azure│  │ azure.identity.aio   │        │
│  │ AzureAIProjectAgent  │  │ AzureCliCredential   │        │
│  │ Provider             │  │ (async)              │        │
│  └──────────────────────┘  └──────────────────────┘        │
│           │                         │                       │
│           └────────────┬────────────┘                       │
│                        │                                    │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │ agent_framework      │  │ pydantic             │        │
│  │ @tool decorator      │  │ Field, Annotated     │        │
│  └──────────────────────┘  └──────────────────────┘        │
│           │                         │                       │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │ asyncio              │  │ python-dotenv        │        │
│  │ async/await support  │  │ load_dotenv()        │        │
│  └──────────────────────┘  └──────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Differences Between Files

```
╔═══════════════════════════════════════════════════════════════╗
║                    agent.py vs agent-framework.py             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  agent.py                    │  agent-framework.py           ║
║  ════════                    │  ══════════════════           ║
║                              │                               ║
║  • CLI Management Tool       │  • Demo/Example Application   ║
║  • CRUD operations           │  • Weather agent example      ║
║  • Synchronous operations    │  • Async/await pattern        ║
║  • argparse for CLI          │  • Agent framework tools      ║
║  • Direct AIProjectClient    │  • AzureAIProjectAgentProvider║
║  • OpenAI chat completions   │  • Streaming & non-streaming  ║
║  • Agent lifecycle mgmt      │  • Function tool decoration   ║
║  • Production-focused        │  • Learning/demo-focused      ║
║                              │                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Execution Flow Summary

### agent.py Execution Path
```
CLI Input → argparse → Command Function → AIProjectClient → Azure AI → Result
```

### agent-framework.py Execution Path
```
main() → Example Function → AzureAIProjectAgentProvider → 
create_agent() → run/run_stream() → @tool Functions → 
Stream/Complete Result
```

---

## Environment Configuration Flow

```
┌─────────────┐
│   .env      │
│   File      │
└──────┬──────┘
       │
       │ load_dotenv()
       ▼
┌─────────────────────────────┐
│ Environment Variables       │
│ ┌─────────────────────────┐ │
│ │ PROJECT_ENDPOINT        │ │
│ │ MODEL_DEPLOYMENT_NAME   │ │
│ │ AGENT_NAME              │ │
│ └─────────────────────────┘ │
└──────┬──────────────────────┘
       │
       │ os.environ["KEY"]
       ▼
┌─────────────────────────────┐
│ Used by both files:         │
│ - agent.py                  │
│ - agent-framework.py        │
└─────────────────────────────┘
```

