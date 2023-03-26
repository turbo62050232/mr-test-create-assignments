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
if __name__ == '__main__':
    app.run(host='192.168.1.41', port=80)