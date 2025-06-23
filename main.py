import requests
import datetime as dt

ENDPOINT_URL = "https://pixe.la/v1/users"
username = ""
TOKEN = ""
header = {
    "X-USER-TOKEN": TOKEN
}
# ---------------------- Create a User---------------------------------
create_user_params = {
    "token": TOKEN,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# create_user = requests.post(url=ENDPOINT_URL,
#                             json=create_user_params)
# create_user.raise_for_status()
# print(create_user)

# ----------------------Create a Graph---------------------------------
graph_ID = "python-bootcamp"
create_graph_params = {
    "id": graph_ID,
    "name": "100 days of Python",
    "unit": "section",
    "type": "int",
    "color": "ajisai",
}
# create_graph = requests.post(url=ENDPOINT_URL+f"/{username}/graphs",
#                              json=create_graph_params,
#                              headers=header)
# print(create_graph)

# ----------------------Create a Pixel---------------------------------
create_pixel_params = {
    "date": "20240729",
    "quantity": "2"
}
# create_pixel = requests.post(url=ENDPOINT_URL + f"/{username}/graphs/{graph_ID}",
#                              json=create_pixel_params,
#                              headers=header)

today = dt.datetime.now().date()
yesterday = today - dt.timedelta(1)

create_pixel2_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "1"
}
create_pixel2 = requests.post(url=ENDPOINT_URL + f"/{username}/graphs/{graph_ID}",
                              json=create_pixel2_params,
                              headers=header)

# ----------------------Update a Pixel---------------------------------
update_pixel2_params = {
    "quantity": "2"
}

# update_pixel2 = requests.put(url=ENDPOINT_URL + f"/{username}/graphs/{graph_ID}/{yesterday.strftime('%Y%m%d')}",
#                              json=update_pixel2_params,
#                              headers=header)
# print(update_pixel2)

# ----------------------Delete a Pixel---------------------------------

delete_pixel2 = requests.delete(url=ENDPOINT_URL + f"/{username}/graphs/{graph_ID}/{yesterday.strftime('%Y%m%d')}",
                             headers=header)
print(delete_pixel2)
