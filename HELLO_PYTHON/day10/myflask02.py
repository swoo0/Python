from flask import Flask
from flask.templating import render_template
from day10.daoemp import DaoEmp

app = Flask(__name__)

@app.route('/emplist')
def emplist():
    de = DaoEmp()
    mylist = de.myselect()
    return render_template("emplist.html", mylist=mylist)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)