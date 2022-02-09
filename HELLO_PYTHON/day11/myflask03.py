from flask import Flask, request
from flask.templating import render_template
from day11.daomember import DaoMember
from flask.json import jsonify

app = Flask(__name__, static_url_path='')
dm = DaoMember()

@app.route('/memlist')
def memberlist():
    mylist = dm.myselect()
    return render_template("memberlist.html", mylist=mylist)

# def myinsert():
#     data = request.get.json()
    
    
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)