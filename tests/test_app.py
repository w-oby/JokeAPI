# USED SOURCES:
# https://docs.pytest.org/en/stable/index.html
# https://realpython.com/pytest-python-testing/
# https://www.freecodecamp.org/news/how-to-use-pytest-a-guide-to-testing-in-python/#heading-how-to-write-your-first-tests-with-pytest
# https://www.geeksforgeeks.org/python/getting-started-with-pytest/
# https://www.youtube.com/watch?v=EgpLj86ZHFQ
# https://dev.to/mwong068/testing-in-python-with-pytest-4aph
# https://www.youtube.com/watch?v=YbpKMIUjvK8
# https://www.datacamp.com/tutorial/pytest-mock
# https://pytest-mock.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/69811358/how-to-test-a-console-print-with-pytest-and-python
# https://stackoverflow.com/questions/20507601/writing-a-pytest-function-for-checking-the-output-on-console-stdout
# https://pavolkutaj.medium.com/how-to-test-printed-output-in-python-with-pytest-and-its-capsys-fixture-161010cfc5ad
# https://www.lenovo.com/us/en/glossary/stdout/ (why does Lenovo have a page on this??? lmao)
# https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html
# https://www.w3schools.com/python/python_args_kwargs.asp
# https://realpython.com/python-kwargs-and-args/
# https://medium.com/@odidaodida/python-overwrite-environment-variable-for-testing-56b3ce7ce1f2
# https://stackoverflow.com/questions/71825373/how-do-i-modify-environment-variables-between-tests-at-runtime-with-pytest
# https://docs.pytest.org/en/stable/how-to/monkeypatch.html
# https://www.datacamp.com/tutorial/pytest-mock

import pytest
import json
import requests

# Import specific methods to test
from api.app import app as flask_app, load_jokes
from user import fetch_joke

@pytest.fixture
def app():

    yield flask_app

@pytest.fixture
def client(app):

    return app.test_client()

# TEST 1
def test_get_random_joke_is_a_success(client):

    response = client.get('/api/jokes/random')

    assert response.status_code == 200

    # Check whether 'joke' is present in response
    assert 'joke' in json.loads(response.data)

# TEST 2
def test_get_random_joke_when_no_jokes_loaded(client, monkeypatch):

    from api import app as flask_app_module

    monkeypatch.setattr(flask_app_module, 'jokes', [])

    response = client.get('/api/jokes/random')

    # Check whether status raises the correct code when jokes list is empty
    assert response.status_code == 500

    # Same as above but checks for similar message contents
    assert 'error_message' in json.loads(response.data)

# TEST 3
def test_load_jokes_when_invalid_json(monkeypatch):

    # Unknown amount of arguments and keyvalue pairs
    def mock_json_load(*args, **kwargs):

        # Create a fake JSON error for testing purposes
        raise json.JSONDecodeError("JSON error sim", "doc", 0)
    
    # Replace real method with a fake test method
    monkeypatch.setattr("json.load", mock_json_load)

    jokes = load_jokes()

    # This checks whether an error gets raised when the original method gets replaced by a fake testing one. Purpose is to see if error handling is functioning correctly.
    assert jokes == []

# TEST 4
def test_mock_fetch_joke_handling_when_request_exception(mocker, capsys):

    # Replace real requests with a fake exception
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException)
    
    # Try except block will try to handle the different situation than expected.
    fetch_joke()
    
    # This right here is black magic. The kind that I thought I would only see in C programming. It captures all output and errors caused by the code.
    captured = capsys.readouterr()
    
    # Message has to be super specific, so don't change this unless source error message is the same. 
    expected_error_msg = "Error: Failed to fetch a joke."

    # Captured output is then checked against same contents of error message. 
    assert expected_error_msg in captured.out