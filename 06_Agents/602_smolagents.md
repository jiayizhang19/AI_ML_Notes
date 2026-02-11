### Workflows V.S. Agents
An agentic framework is not always needed when building an application around LLMs. Sometimes, predefined **workflows** are sufficient to fulfill user requests. However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.
- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. (Choose the right framework for your needs.)

### Agentic Framework 
1. **smolagents**: A simple yet powerful framework for building AI agents.
  (Check more resources at the end of the blog https://huggingface.co/learn/agents-course/unit2/smolagents/introduction)
    - Primary Advantages: It supports a code-first approach with minimal abstractions, letting agents interact directly via Python function calls.
    - Code Agents: Tradtional approaches use a JSON format to specify tool names and arguments as strings, which the system must **parse to determine which tool to execute.** However, research shows that **tool-calling LLMs work more effectively with code directly.**
      - Use DuckDuckGoSearchTool when you need to search on the web.
      - Use automatica code generation with additional_authorized_imports (without explicitly specified any tools) when:
        - The task is purely computational;
        - You trust the LLM to write correct logic;
        - No external systems are involved;
        - Failure has low consequences.
      - Write custom tools when:
        - You need to interact with external systems, for example, query DB or send email ant etc..;
        - Business logic is complex / important;
        - Security / safety is a concern.
