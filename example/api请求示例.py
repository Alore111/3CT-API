import hashlib
import time
import requests
import json

from oauthlib.oauth2.rfc6749.utils import params_from_uri

BASE_URL = "https://3ct-api.2ndtool.top/v4/"

def ct_get(params):
    url = BASE_URL + "getReq"

    print()
    print("↓↓↓↓↓ GET请求URL ↓↓↓↓↓")
    full_url = url + "?" + "&".join([f"{key}={value}" for key, value in params.items()])
    print(full_url)
    print("↑↑↑↑↑↑ GET请求URL ↑↑↑↑↑")
    print()

    response = requests.get(url, params=params)
    response_data = response.json()
    return response_data




if __name__ == "__main__":


    get_params = {
        "type": "getEkActByKeys",
        # "ActivityName": "天文",
        "ActivityType": "讲座",
        "PageIndex": 3
    }
    print()
    print(ct_get(get_params))
