# USED SOURCES:
# https://docs.python.org/3/library/functions.html#open
# https://www.w3schools.com/python/python_try_except.asp
# https://realpython.com/python-exceptions
# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
# https://www.datacamp.com/tutorial/making-http-requests-in-python
# https://flask.palletsprojects.com/en/stable/api/
# https://flask.palletsprojects.com/en/stable/tutorial/factory/
# https://stackoverflow.com/questions/29882642/how-to-run-a-flask-application
# https://www.geeksforgeeks.org/python/how-to-run-a-flask-application/
# https://flask.palletsprojects.com/en/stable/server/

import json
import random

from flask import Flask, jsonify

app = Flask(__name__)

# Pull up joke data
def load_jokes():

    try:

        with open('api/jokes.json', 'r') as file:

            data = json.load(file)

            return data['jokes']
        
    except FileNotFoundError:

        print("Could not find specified file.\n")

        return []
    
    except (json.JSONDecodeError):

        print("JSON is invalid.\n")

        return []

jokes = load_jokes()

@app.route('/api/jokes', methods=['GET'])

# Readying the jokes for use with API
def get_jokes():
    
    return jsonify(jokes)

@app.route('/api/jokes/random', methods=['GET'])

# Pulling a random joke from the list
def get_random_joke():

    if not jokes:
        
        error_msg = { "error_message": "Error. Could not load contents from file." }

        return jsonify(error_msg), 500
    
    random_joke = random.choice(jokes)

    return jsonify(random_joke)

# In-code starting of server - saves you from hassle :)
if __name__ == '__main__':

    app.run()