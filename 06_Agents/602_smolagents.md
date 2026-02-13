### Workflows V.S. Agents
An agentic framework is not always needed when building an application around LLMs. Sometimes, predefined **workflows** are sufficient to fulfill user requests. However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.
- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. (Choose the right framework for your needs.)

### Agentic Framework 
#### Smolagents
- A simple yet powerful framework for building AI agents.
  (Check more resources at the end of the blog https://huggingface.co/learn/agents-course/unit2/smolagents/introduction)
- Primary Advantages: It supports a code-first approach with minimal abstractions, letting agents interact directly via Python function calls.
- Available Tools:
  - Use DuckDuckGoSearchTool when you need to search on the web.
  - Use automatic code generation with additional_authorized_imports without explicitly specified any tools (available for CodeAgent while not for ToolCallingAgent), when:
    - The task is purely computational;
    - You trust the LLM to write correct logic;
    - No external systems are involved;
    - Failure has low consequences.
  - Use custom tools, when:
    - You need to interact with external systems, for example, query DB or send email ant etc..;
    - Business logic is complex / important;
    - Security / safety is a concern.
- Model Selection: 
  - Using default InferenceClientModel(), the HF inference providers router, burns credits.
    ```
    model=InferenceClientModel()
    ```
  - Alternatively, using a provider's free tier via LiteLLMModel can bypass HF billing with gemini model. (Setting up a Gemini API Key via Google AI Stuido https://aistudio.google.com/ and check out available model https://ai.google.dev/gemini-api/docs)
    ```
    gemini_model = LiteLLMModel(
      model_id="gemini/gemini-2.5-flash",
      api_key=os.getenv("GEMINI_API_KEY")
    )
    ```
- Agent Types:
  1. **Code Agents**: Code generation paradigm and the default agent type in smolagents. It writes actions in code rather than JSON. However, research shows that **tool-calling LLMs work more effectively with code directly.**
    - Example of agent's trace:
      ```
      Executing parsed code:
      music_recommendations = web_search(query="best music recommendations for a party")       
      print("Music recommendations:"music_recommendations)   
      ```
    - Running a Code Agent inside smolagents:
      ```
      web_and_tools_agent = CodeAgent(
      tools=[DuckDuckGoSearchTool(),suggest_menu],
      model=gemini_model,
      # model=InferenceClientModel(), # It needs credits
      )
      web_and_tools_agent.run(
          "Search for the best music recommendations for a party."
          "Prepare me a menu for a party that is informal."
      )
      ```
  2. **Tool Calling Agents**: Structured tool-calling paradigm. These agents use the built-in tool-calling capabilities of LLM providers to generate tool calls as JSON structures. This is the standard approach used by OpenAI, Anthropic, and many other providers.
    - Example of agent's trace, instead of seeing Executing parsed code, you'll see something like:
      ```
      Calling tool: 'web_search' with arguments: {'query': 'best music recommendations for a party'}   
      ```
    - Running a Tool Calling Agent inside smolagents
      ```
      from smolagents import ToolCallingAgent, WebSearchTool, LiteLLMModel

      tool_calling_agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool(),suggest_menu],
        model=gemini_model,
      )

      tool_calling_agent.run(
        "Search for the best music recommendations for a party."
        "Prepare me a menu for a party that is informal."
      )
      ```
  
