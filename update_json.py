import requests
import json
import os

# Source and Destination
SOURCE_URL = "https://streamed.pk/api/matches/all-today/popular"
DEST_FILE = "bintvjson/index.json"

def sync_api():
    try:
        print(f"Connecting to {SOURCE_URL}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(SOURCE_URL, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Ensure directory exists
        os.makedirs(os.path.dirname(DEST_FILE), exist_ok=True)

        # Save the fresh data
        with open(DEST_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print("Successfully updated index.json with latest matches.")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    sync_api()
