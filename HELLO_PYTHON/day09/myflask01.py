from flask import Flask, request

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
    a = request.form.get('a')
    return f'param = {a}'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)