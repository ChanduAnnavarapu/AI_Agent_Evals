from langchain.tools import Tool
from dotenv import load_dotenv
from datetime import datetime
import os
from objects import PurchaseItem
from data import users_data
import json
import logging

load_dotenv()

@tool
def get_user_purchase_history(user_id: str) -> list[PurchaseItem]:
    """
    Get the purchase history of a user by their user ID.
    Args:
        user_id (str): The ID of the user.
    Returns:
        list[PurchaseItem]: A list of PurchaseItem objects representing the user's purchase history.
    """
    try:
        # Fetch the user's purchase history from the users_data dictionary
        purchase_history = users_data.get(user_id, [])
        
        # Convert the purchase history to a list of PurchaseItem objects
        purchase_items = [PurchaseItem(name=item['name']) for item in purchase_history]
        
        return purchase_items
    except Exception as e:
        logging.error(f"Error fetching purchase history for user {user_id}: {e}")
        return []

@tool
def get_current_time() -> str:
    """
    Get the current date and time.
    Returns:
        str: The current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time
    except Exception as e:
        logging.error(f"Error fetching current time: {e}")
        return "Error fetching current time"
    
@tool
def get_user_purchase_history_json(user_id: str) -> str:
    """
    Get the purchase history of a user by their user ID in JSON format.
    Args:
        user_id (str): The ID of the user.
    Returns:
        str: A JSON string representing the user's purchase history.
    """
    try:
        # Fetch the user's purchase history from the users_data dictionary
        purchase_history = users_data.get(user_id, [])
        
        # Convert the purchase history to a JSON string
        purchase_history_json = json.dumps(purchase_history, indent=4)
        
        return purchase_history_json
    except Exception as e:
        logging.error(f"Error fetching purchase history for user {user_id}: {e}")
        return "Error fetching purchase history"