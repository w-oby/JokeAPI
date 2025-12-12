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