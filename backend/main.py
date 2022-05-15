import requests
import csv
import json
import pandas as pd
import io
from flask import Flask, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "Test Flask"


@app.route("/getRapidTestKits")
def get_data():
    url = "https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D03001-001&l=https://data.nhi.gov.tw/resource/Nhi_Fst/Fstdata.csv"
    r = requests.post(url, {"nid": 152408}).content
    df = pd.read_csv(io.StringIO(r.decode('utf-8')))

    # # Convert to iterator by splitting on \n chars
    # lines = r.text.splitlines()
    # # Parse as CSV object
    # reader = csv.reader(lines)
    # print(df.to_json(orient='index', force_ascii=False))
    # response = jsonify({'msg': df.to_json(orient='records', force_ascii=False)})
    response = json.dumps(json.loads(df.to_json(orient='records', force_ascii=False)), indent=2)
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
