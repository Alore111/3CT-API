import hashlib
import time
import requests
import json

# BASE_URL = "https://3ct-api.2ndtool.top/v4/"
BASE_URL = "http://127.0.0.1:8951/v4/"


def calculate_signature(token, request_id, params, ts):
    sign_string = token + "params" + str(json.dumps(params).replace("'", "\"")) + "ts" + str(ts) + "request_id" + str(request_id)
    # 计算MD5哈希值
    signature = hashlib.md5(sign_string.encode()).hexdigest()

    return signature


def ct_post(params):
    # 示例参数
    request_id = "yht5SxlIFp45NYgEiQl0YXq3Je7fhXtqBsfaULw2sZpQOY0MLlc4ywMuaMc"
    token = "d051efd49980b2f05f0f5ad13c4d1119906426ad82bd12dda1c9633d1e7e84f5"
    ts = int(time.time())

    # 计算签名
    signature = calculate_signature(token, request_id, params, ts)

    # 构造请求参数
    request_data = {
        "request_id": request_id,
        "params": json.dumps(params),  # 将params转换为JSON字符串
        "ts": ts,
        "sign": signature
    }
    print()
    print("↓↓↓↓↓ POST请求体 ↓↓↓↓↓")
    print(request_data)
    print("↑↑↑↑↑↑ POST请求体 ↑↑↑↑↑")
    print()

    # 发送POST请求
    url = BASE_URL + "postReq"
    response = requests.post(url, json=request_data)

    # 解析响应
    response_data = response.json()
    return response_data

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
    post_params = {
        "type": "login",
        "data": {
            "username": "test",
            "password": "test"
        }
    }
    print(ct_post(post_params))


    get_params = {
        "type": "getEkActByKeys",
        # "ActivityName": "天文",
        "ActivityType": "讲座",
        "PageIndex": 3
    }
    print()
    # print(ct_get(get_params))
