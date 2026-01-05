# USED SOURCES:
# https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
# https://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes
# https://docs.python.org/3/library/msvcrt.html
# https://www.w3schools.com/python/ref_module_msvcrt.asp
# https://docs.python.org/3/library/subprocess.html
# https://www.geeksforgeeks.org/python/python-subprocess-module/
# https://www.datacamp.com/tutorial/python-subprocess

import requests
import msvcrt # Better than pynput or keyboard library for detection of keypresses without additional steps needed. It's also cleaner and less code to deal with.
import os
import subprocess # Handling processes which allows me to manipulate (run, edit, delete) them
import sys
from colorama import init, Fore, Style

init()

# Localhosting a server
API_URL = "http://127.0.0.1:5000/api/jokes/random"

# New file to store PID number in
PID = "jokeapi_server.pid"

# Fetching a joke
def fetch_joke():

    print(Style.NORMAL+ Fore.YELLOW + "Fetching a random joke from the API...")
    
    try:

        response = requests.get(API_URL)
        
        # Except if error (4xx/5xx code). Continue if OK (200).
        response.raise_for_status()
        
        data = response.json()
        
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +"\n" + "="*100 + "\n" + "="*100 + "\n")

        # Get joke, otherwise print message "No joke found".
        print(Style.BRIGHT + Fore.CYAN + f"{data.get('joke', 'No joke found.')}")

        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\n" + "="*100 + "\n" + "="*100 + "\n")

    # Generic catch-all exception, instead of anything specific
    except requests.exceptions.RequestException:
        
        print(Style.NORMAL + Fore.RED + "\nError: Failed to fetch a joke. Please make sure the API server is set up and running.")

def kill_jokeapi_server():

    try:

        if os.path.exists(PID):

            with open(PID, 'r') as file:

                # Contents of file is to be read and stripped to prevent escaping of characters that might have been caused by Windows' CRLF behavior
                pid = file.read().strip()

            print(Style.NORMAL+ Fore.YELLOW + f"Shutting down JokeAPI server")

            # Command to kill a specifically targeted PID by force. Capture_output is a bit weird, seeing as I would have expected capture_output=True to start logging and printing output, but guess that's not the case for this library.
            subprocess.run(["taskkill", "/F", "/PID", pid], capture_output=True, text=True)

            # Once task kill has commenced, delete PID file for clean execution and exit
            os.remove(PID)

    except (FileNotFoundError, ValueError):

        print(Style.NORMAL + Fore.RED + "Could not find PID file. Try manually closing it in Task Manager.")

    except Exception as e:

        print(Style.NORMAL + Fore.RED + f"Could not stop the server. See error: {e}")

def main_code():
    
    fetch_joke()

    while True:

        print(Style.NORMAL + Fore.GREEN + "Press SPACEBAR for a new joke, or ESC to exit." + "\n")

        # getch() looks for any keypress input and then assigns that to variable key. We can then manipulate the variable.
        key = msvcrt.getch()

        # ESC key leads to break, which exits the program.
        if key == b'\x1b':

            break

        # Spacebar key leads to call of method, which requests a new joke
        elif key == b' ':

            fetch_joke()

# This is when all the code above gets executed.
if __name__ == "__main__":
    
    # When app starts, execute the try and finally block
    try:

        # Once code in func main_code() finishes or a break occurs the try block is concluded, and the flow will continue to the finally block.
        main_code()

    finally:

        # Self-explanatory
        kill_jokeapi_server()

        print(Fore.GREEN + "Closing application...")

        # True exit
        sys.exit(0)