
import requests, json
from requests import request
from sqlalchemy import JSON

userSelection = ['clubs', 'park', ' bar']

select1 = userSelection[0]
select2 = userSelection[1]
select3 = userSelection[2]
userLocation = "stamford"

url = requests.get("http://10.194.208.158:8080/?select1="+ select1 + "&select2=" + select2 + "&select3="+ select3 + "&location=" + userLocation)
text = url.text

data = json.loads(text)

user = data["data"][0]['address']
print(user)

# address = user['address']
# print(address)

# def hello_world(request):
#     """Responds to any HTTP request.
#     Args:
#         request (flask.Request): HTTP request object.
#     Returns:
#         The response text or any set of values that can be turned into a
#         Response object using
#         `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
#     """
#     request_json = request.get_json()
#     if request.args and 'message' in request.args:
#         return request.args.get('message')
#     elif request_json and 'message' in request_json:
#         return request_json['message']
#     else:
#         return f'Hello World!'
