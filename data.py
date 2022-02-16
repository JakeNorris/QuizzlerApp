import requests

# Dict of parameters to pass into the website.
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Use Open Trivia Database website to grab true/false questions.
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
