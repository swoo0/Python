from flask import Flask, request
from flask.json import jsonify
from day12.daostock import DaoStock

app = Flask(__name__, static_url_path='')
ds = DaoStock()

def myinsert():
    data = request.get_json()
    s_code = data['s_code']
    s_name = data['s_name']
    price = data['price']
    ymd_hm = data['ymd_hm']

    cnt = ds.myinsert(s_code, s_name, price, ymd_hm)

    result = "fail"
    if cnt == 1:
        result = "success"
        
    return jsonify(result = result)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)