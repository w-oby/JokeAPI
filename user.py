# USED SOURCES:
# https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
# https://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes

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
        
        print("\n" + "="*100 + "\n" + "="*100 + "\n")

        # Get joke, otherwise print message "No joke found".
        print(f"{data.get('joke', 'No joke found.')}")

        print("\n" + "="*100 + "\n" + "="*100 + "\n")

    # Generic catch-all exception, instead of anything specific
    except requests.exceptions.RequestException:
        
        print("\nError: Failed to fetch a joke. Please make sure the API server is set up and running.")

if __name__ == "__main__":

    fetch_joke()