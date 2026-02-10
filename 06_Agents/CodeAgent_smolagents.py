# CodeAgent() provides access to Hugging Face's severless inference API. It sets Qwen as the default model, which can be customed with any compatible models from the Hub.
# DuckDuckGoSearchTool is a tool capable of searching the web.



from huggingface_hub import login
from dotenv import load_dotenv
import os
from smolagents import tool, CodeAgent, DuckDuckGoSearchTool, InferenceClientModel


load_dotenv()
hf_token = os.getenv("hf_token")
login(token=hf_token)

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



agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(),suggest_menu],
    model=InferenceClientModel()
)

agent.run(
    "Search for the best music recommendations for a party."
    "Prepare me a menu for a party that is informal."
)