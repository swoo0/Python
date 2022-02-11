from flask import Flask, request
from flask.templating import render_template
from day13.daostock import DaoStock

app = Flask(__name__, static_url_path='', static_folder="static")
ds = DaoStock()

@app.route('/')
def stock():
    name = []
    price = []
    
    ds = DaoStock()
    mylist = ds.mys_names()
    for n in mylist:
        s_name = n['s_name']
        prices = ds.myprices(s_name)
        print(s_name,prices)
        name.append(s_name)
        price.append(prices)

    return render_template("line-charts.html", name=name,price=price)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)