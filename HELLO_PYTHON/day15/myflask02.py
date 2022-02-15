from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__,static_url_path='',static_folder="static")

@app.route('/')
def janggi():
    return render_template("janggi4.html")
    
@app.route('/tween')
def tween():
    return render_template("tween.html")
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)