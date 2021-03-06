import sys
from io import BytesIO
import requests
from PIL import Image
from file2 import params

toponym_to_find = ' '.join(sys.argv[1:])
print(toponym_to_find)
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"
}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
json_response = response.json()
map_params = params(json_response)
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()