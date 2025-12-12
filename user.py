import requests

# Localhosting a server
API_URL = "http://127.0.0.1:5000/api/jokes/random"

# Fetching a joke
def fetch_joke():

    print("Fetching a random joke from the API...")
    
    try:

        response = requests.get(API_URL)
        
        # Except if error (4xx/5xx code). Continue if OK (200).
        response.raise_for_status()
        
        data = response.json()
        
        print("\n" + "//"*20)

        # Get joke, otherwise print message "No joke found".
        print(f"{data.get('joke', 'No joke found.')}")

        print("//"*20 + "\n")

    # Generic catch-all exception, instead of anything specific
    except requests.exceptions.RequestException:
        
        print("\nError: Failed to fetch a joke. Please make sure the API server is set up and running.")

if __name__ == "__main__":

    fetch_joke()