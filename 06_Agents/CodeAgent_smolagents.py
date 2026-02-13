# CodeAgent() provides access to Hugging Face's severless inference API. 
# Use DuckDuckGoSearchTool to search the web.
# Use @tool to create custom tools with specific business logic
# Use additional_authorized_import to allow code generation using other libraries.



from huggingface_hub import login
from dotenv import load_dotenv
import os
from smolagents import tool, CodeAgent,ToolCallingAgent, DuckDuckGoSearchTool, InferenceClientModel, LiteLLMModel
import time
import datetime

load_dotenv()
# Switching from HF inference model to free tier gemini model
# HF_TOKEN = os.getenv("HF_TOKEN")
# login(token=HF_TOKEN)
gemini_model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Custom new tools
@tool
def suggest_menu(occasion: str) -> str:
    # Keep an eye on this docstring written, it needs to have description for all arguments (with the same upper or lower case).
    # Otherwise, the tool is not going to work.
    """
    Suggests a menu based on the occasion.
    Args:
        occasion(str): The type of occasion for the party. Allowed values are:
            - "causal": Menu for causal party.
            - "formal": Menu for formal party.
            - "superhero": Menu for superhero party.
            - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks"
    if occasion == "formal":
        return "3-course dinner with wine and dessert"
    if occasion == "superhero":
        return "Buffet with high-energy and healthy food"
    else:
        return "Custome menu for the butler"
    

# ============================================= #
# 1. Code Agent: Using web search and custom tools
# ============================================= #
web_and_tools_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(),suggest_menu],
    model=gemini_model,
    # model=InferenceClientModel(), # It needs credits
)

web_and_tools_agent.run(
    "Search for the best music recommendations for a party."
    "Prepare me a menu for a party that is informal."
)


# ====================================================================== #
# 1. Code Agent: Using Python imports inside the agent (agent generation code)
# ====================================================================== #
python_imports_agent = CodeAgent(
    tools=[],
    # model=InferenceClientModel(),
    model=gemini_model,
    additional_authorized_imports=["datetime"]
)

python_imports_agent.run(
    """
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)

# ======================================================== #
# 2. Tool Calling Agent: Using web search and custom tools
# ======================================================== #
tool_calling_agent = ToolCallingAgent(
    model=gemini_model,
    tools=[DuckDuckGoSearchTool(),suggest_menu],
)

tool_calling_agent.run(
    "Search for the best music recommendations for a party."
    "Prepare me a menu for a party that is informal."
)
