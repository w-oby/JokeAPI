# 🤡 JokeAPI

This project is a Python application that sets up a local API to serve random jokes to a CLI (Command Line Interface) window. The user can setup and launch the application with only two clicks.

The project utilizes a Flask server, a CLI window, automated setup and startup procedures, and a Pytest testsuite.

## Features
- Local API: Uses Flask to run an API that fetches jokes from a .JSON file.
- CLI Window: User friendly terminal where the user can request new jokes with the spacebar key and exit the client with ESC key.
- Automated setup & startup: Two batch files are utilized to automate the setup of the server and the startup of the client. The user only gets to see the client window, because the setup happens in the background and completely hidden from the users' eyes. 
- Clean & Fast: The application cleans up after itself. The server process is automatically terminated upon exit. The files required for the operation of the server are removed after usage.
- Professional setup: A batch script creates an isolated Python virtual environment (venv) and installs all packages and dependencies automatically.
- Styling: Uses colorama for a clear and aesthetic terminal output. No more boring white lines!
- Pytest Test Suite: The testsuite includes 4 tests written with Pytest to ensure the reliability of the API and its error handling.

## Technologies & Packages
- Backend: Python, Flask
- Frontend: Python
- Testing: Pytest, pytest-mock
- Automation: Batch and VBScript

# ⚙️ Getting Started
1. __Clone or download the repository__

      Copy the following line and paste it into Git:

      ```
      git clone https://github.com/w-oby/JokeAPI.git
      ```

      Alternatively, download the files as a ZIP archive and extract them. Open the extracted folder. You are now in the root of the project and can start the setup process.

2. __Run the setup__

      Double click the <ins>setup.bat</ins> file.

      This script will automatically create a virtual environment named <ins>jokeapi_venv</ins> and install all the required packages from the file requirements.txt.
   
3. __Launch the application__

      After the setup is complete, you can start the application.

      Double click the <ins>start.bat</ins> file.

      A single window will open, and you will immediately be presented with a joke. Press the spacebar for a new joke. Press ESC to exit the application and shut down the server.
   
## ✔️ Testing the code with Pytest
The testsuite tests and validates the functionality of the API and its error handling. To run the tests, follow these steps:

1. Open a CLI terminal and navigate your terminal to the project's root directory.

2. Activate the virtual environment with the following command:
```
.\jokeapi_venv\Scripts\activate
```
Your terminal will now show (jokeapi_venv).

3. Run the tests. Ensure that you are at the root directory of the repository. To run the tests, use the following command:
```
pytest
```

If the command returns an error, try the alternative command:
```
python -m pytest
```

You should see the output of the testsuite, ending with a green message showing that all four tests have passed.

4. When you are finished testing, you can leave the virtual environment with the command:
```
deactivate
```
