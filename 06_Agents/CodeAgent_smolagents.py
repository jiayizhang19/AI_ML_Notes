# CodeAgent() provides access to Hugging Face's severless inference API. It sets Qwen as the default model, which can be customed with any compatible models from the Hub.
# Use DuckDuckGoSearchTool to search the web.
# Use @tool to create custom tools with specific business logic
# Use additional_authorized_import to allow code generation using other libraries.



from huggingface_hub import login
from dotenv import load_dotenv
import os
from smolagents import tool, CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
import time
import datetime

load_dotenv()
hf_token = os.getenv("hf_token")
login(token=hf_token)

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

# Using web search and custom tools
web_and_tools_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(),suggest_menu],
    model=InferenceClientModel()
)

web_and_tools_agent.run(
    "Search for the best music recommendations for a party."
    "Prepare me a menu for a party that is informal."
)

# Using Python imports inside the agent (agent generation code)
python_imports_agent = CodeAgent(
    tools=[],
    model=InferenceClientModel(),
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