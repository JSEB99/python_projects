import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "USER"
TOKEN = "TOKEN"
GRAPH_ID = "GRAPH_NAME"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# CREATE A USER
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"studying graph",
    "unit":"hours",
    "type":"float",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# CREAR GRÁFICA
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

graph_info = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
date = today.strftime('%Y/%m/%d')
time = today.strftime('%H:%M:%S')

print(date,time)
params_info = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"6.5",

}

# SUBIR INFO A LA GRÁFICA
# response = requests.post(url=graph_info,json=params_info,headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity':"5.6"
}

# ACTUALIZAR INFO GRÁFICA
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# ELIMINAR INFO
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)