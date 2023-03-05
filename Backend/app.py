from flask import Flask
from controller.home import homeClass
app = Flask(__name__)

@app.route("/")
def index():
    # return "<p>XD</p>"
    res=homeClass.hello_world()
    return res
@app.route('/questboard')
def questboard():
    res=homeClass.getAllQuest()
    return res