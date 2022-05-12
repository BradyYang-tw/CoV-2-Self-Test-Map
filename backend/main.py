import requests
from flask import Flask, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "Test Flask"


@app.route("/getData")
def get_data():
    url = "https://quality.data.gov.tw/dq_download_json.php?nid=152408&md5_url=8699cd0ecbfcc5b30a577b53026fe02b"
    r = requests.post(url, {"nid": 152408})
    response = jsonify({'msg': r.json()})
    return response


# from urllib import request, parse
# import json
# data = parse.urlencode({"nid": 152408}).encode()
# req = request.Request(url, data=data)
# with request.urlopen(req) as res:
#     page_data = json.load(res)    # 以 JSON 格式，讀取「網站伺服器的回應」
#     print(page_data)


if __name__ == '__main__':
    app.run()
