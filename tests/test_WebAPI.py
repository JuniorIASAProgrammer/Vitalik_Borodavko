import requests
import json

url_upload = "https://content.dropboxapi.com/2/files/upload"
url_metadata = "https://api.dropboxapi.com/2/files/get_metadata"
url_delete = "https://api.dropboxapi.com/2/files/delete_v2"
token = 'sl.BH-5ipD3M4oOZnH2jHIKfQ_gx9q1QF5aA_hQW4u_4iygsxugX9KMj_8meJXMEE79u5-0KJ6iEREPUYPy5WyatGpL2fQQYWDrY83Vx6IbKtnuTNC-NkN7LMWYzS2t6_ZB2dejpnDq'
auth = "Bearer " + token
path = "/WebApi/text.txt"


def test_upload():
    headers = {
        "Authorization": auth,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": "{\"path\":\"/WebApi/text.txt\"}"
    }
    data = open("uploadFile.txt", "rb").read()
    response = requests.post(url_upload, headers=headers, data=data)
    assert response.status_code == 200


def test_getFileMetaData():
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }
    data = {
        "path": path
    }
    response = requests.post(url_metadata, headers=headers, data=json.dumps(data))
    assert response.status_code == 200


def test_deleteFile():
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }
    data = {
        "path": path
    }
    response = requests.post(url_delete, headers=headers, data=json.dumps(data))
    assert response.status_code == 200
