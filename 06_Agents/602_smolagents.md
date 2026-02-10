### Workflows V.S. Agents
An agentic framework is not always needed when building an application around LLMs. Sometimes, predefined **workflows** are sufficient to fulfill user requests. However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.
- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. (Choose the right framework for your needs.)

### Agentic Framework 
1. **smolagents**: A simple yet powerful framework for building AI agents.
  (Check more resources at the end of the blog https://huggingface.co/learn/agents-course/unit2/smolagents/introduction)
  - Primary advantages: It supports a code-first approach with minimal abstractions, letting agents interact directly via Python function calls.
