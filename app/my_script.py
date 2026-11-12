import os
from dotenv import load_dotenv

load_dotenv()

player_name = os.getenv("PLAYER_NAME", "Player One")
print(f"Hello, {player_name}! My script is running.")