import requests
import json

token = "BQBarK39QZxrvNDfJl7fZzm4b-Omedv6PIP8FokGLouNpWJlBLh1sEXkNBvw5Ew1DAj6fJHNh-O5ZQfOTJw3EvAbNddmtwdI21VnlHsOppSYXp38JrC4"
playlist = "4FX8NNJiLVSi62YDDwd61O"
#call the spotify api using access token and get the response
response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist}/tracks",
                        headers={"Authorization": "Bearer " + token})
#convert the response to json format

response_json = response.json()
total = response_json["total"]

def getTrackName(response_json, ids=[]):
    total = response_json["total"]
    for i in range(total):
        id = response_json["items"][i]["track"]["id"]
        ids.append(id)
        print(response_json["items"][i]["track"]["name"])
        if (i == len(response_json['items'])-1):
            if (response_json["next"] == None):
                return ids 
            response_json = requests.get(response_json["next"], headers={
                                        "Authorization": "Bearer " + token}).json()
            getTrackName(response_json, ids)
            return ids 
    a=0

print(response_json)

getTrackName(response_json)



# https://open.spotify.com/playlist/4FX8NNJiLVSi62YDDwd61O?si=83d2399daa10413b
# https: // open.spotify.com/album/7txGsnDSqVMoRl6RQ9XyZP?si = 0ec00afbe37a4c62
