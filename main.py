import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "abdelrahman"
TOKEN = "a5d32h58j34jej3"
GRAPH_ID = "graph1"
user_parameters = {

    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {

    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km do yoy run today? ")

}

response = requests.post(url=pixel_creation_endpoint, json=post_parameters, headers=headers)
print(response.text)

updated_parameter = {
    "color": "shibafu",

}
# response = requests.put(url=pixel_creation_endpoint, json=updated_parameter, headers=headers)
# print(response.text)
