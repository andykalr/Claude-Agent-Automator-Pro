import os
from dotenv import load_dotenv

load_dotenv()

def helper_print(message: str):
    print(f"[Helper] {message}")

def get_claude_key() -> str:
    """Fetch the Claude API key from .env safely."""
    key = os.getenv("CLAUDE_API_KEY")
    if not key:
        raise ValueError("CLAUDE_API_KEY not found in .env")
    return key