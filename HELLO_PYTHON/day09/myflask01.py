from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

# @app.route('/para')
# def para():
#     a = request.args.get('a')
#     return 'param = ' + a

@app.route('/param', methods=['post'])
def para():
    a = request.form['a']
    return f'param = {a}'
    # return 'param = ' + a


@app.route('/view')
def view():
    a = "999"
    b = ["홍길동", "전우치", "이순신"]
    c = {'e_id':1, 'e_name':1, 'sex':1, 'age':1}
    d = [
            {'e_id':2, 'e_name':2, 'sex':2, 'age':2},
            {'e_id':3, 'e_name':3, 'sex':3, 'age':3}
        ]    
    return render_template("view.html", a=a, b=b, c=c, d=d)








if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)