# Use an API call to get some questions and answers

import requests

# Goto https://opentdb.com/api_config.php to see more parameters etc

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 15,  # optional. 15 is video games
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
