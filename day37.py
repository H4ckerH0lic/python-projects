#Advanced Authentication and POST/PUT/DELETE requests
import requests
from datetime import datetime

current_date = datetime.now().strftime("%Y%m%d")
print(current_date)

TOKEN = "surprisemother"
USERNAME = "dextermfs"

pixela_endpoint = "https://pixe.la/v1/users"


user_param ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint,json=user_param)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

graph_config = {
    "id" : "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(graph_endpoint, json=graph_config,headers=headers)
#print(response.text)

pixel_data = {
    "date" : current_date,
    "quantity" : "5",
}

# response = requests.post(pixel_post_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{current_date}"

new_pixel_data = {
    "quantity" : "4.5"
}

response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)