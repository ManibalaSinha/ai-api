import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API keys from environment variable (comma-separated for multiple keys)
API_KEYS = os.getenv("API_KEYS", "").split(",")

if not API_KEYS or API_KEYS == [""]:
    raise ValueError("API_KEYS environment variable not set")

# Dependency to verify API key
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key
