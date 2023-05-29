# ----------------------Library-------------------------------------------
from flask import Flask, request, make_response
from flask_apscheduler import APScheduler
from flask_cors import CORS
import logging

# ----------------------Class Fucntion-----------------------------------
from controller.questBoard import questBoardClass
from controller.editQuest import editQuestClass
from controller.editQuestJson import editQuestJsonClass
from controller.login import loginClass
from controller.payloadManager import payloadManagerClass
from controller.leaderBoard import leaderBoardClass
from controller.levelManager import levelManagerClass
from controller.logManager import logManagerClass
from controller.jwtManager import jwtManagerClass
from quickstart.classroom_create_coursework import CourseworkClass

# ----------------------------------------------------------------------
import os
import json

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
CORS(app)
logging.getLogger("flask_cors").level = logging.DEBUG
sched = APScheduler()
current_date = 0


# Middleware function
# @app.before_request
# def middleware():
#     print("testttt")
#     if request.path == "/login" or request.path == "/":
#         # Redirect to secure login page if the request is not secure and not for the login route
#         return None
#     # Perform middleware logic here
#     # For example, you can access the request object and perform checks
#     auth_header = ""
#     try:
#         auth_header = request.headers.get("Authorization")
#         substring = auth_header.split(" ")[1]
#     except Exception as error:
#         return "", 401
#     res = jwtManagerClass.decodeJWT(auth_header, "role")
#     print(res["status"])
#     if res["status"] > 200:
#         return "", res["status"]
#     print("passss")
#     return None


# @app.after_request
# def handle_options(response):
#     # if request.method == 'OPTIONS':
#     # response = make_response()
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
#     print(response)
#     return response
#     # return None


@app.route("/")
def index():
    # return "<p>XD</p>"
    res = questBoardClass.hello_world()
    return res


@app.route("/health")
def health():
    return "", 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print(data)
    res = loginClass.login(data)
    return res


@app.route("/role", methods=["POST"])
def role():
    data = request.get_json()
    print("this is json data")
    print(data)
    # res=loginClass.login(data)
    # auth_header = request.headers.get("Authorization")
    # substring = auth_header.split(" ")[1]
    # encoded_jwt = data["encoded_jwt"]
    # role = jwtManagerClass.decodeJWT(encoded_jwt, "role")
    role={"role":"student"}
    print("test")
    print(role)
    return role, 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    res = loginClass.register(data)
    return res


@app.route("/payloadAdd", methods=["POST"])
def payloadAdd():
    data = request.get_json()
    global current_date
    current_date = 1
    # print("now current_date =",current_date)
    print(data)
    res = payloadManagerClass.addStudentToQuest(data)
    # res=payloadManagerClass.hello_world(data)
    return res


@app.route("/questboard", methods=["POST"])
def questboard():
    print("start")
    data = request.get_json()
    # auth_header = request.headers.get("Authorization")
    # substring = auth_header.split(" ")[1]
    encoded_jwt = data["encoded_jwt"]
    data = jwtManagerClass.decodeJWT(encoded_jwt, "userId")
    print("niceee")
    print(data)
    res = questBoardClass.getAllQuest(data)
    return res


@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    data = request.get_json()
    res = leaderBoardClass.getLeaderBoard(data)
    return res


@app.route("/log", methods=["GET"])
def log():
    data = request.get_json()
    res = logManagerClass.getAllLog()
    return res


@app.route("/editquest", methods=["POST"])
def editquestjson():
    data = request.get_json()
    print(data)
    res = editQuestJsonClass.editQuestJson(data)
    return json.dumps(res)


@app.route("/dayset")
def dayset():
    global current_date
    current_date = 1
    res = "this day...."
    return res


@app.route("/addExpToPlayer", methods=["POST"])
def addExpToPlayer():
    data = request.get_json()
    print(data)
    res = levelManagerClass.addExpToPlayer(data)
    return res


def job():
    global current_date
    payloadManagerClass.unloadpayload() if current_date == 1 else print("noo")
    current_date = 0


if __name__ == "__main__":
    # create Scheduler to run every 5 seconds
    sched.add_job(id="job1", func=job, trigger="interval", seconds=10)
    # create Scheduler to run every day at 23:59
    # sched.add_job(id='job1',func=job, trigger= 'cron',hour=23,minute=40)
    # sched.start()

    # app.run(host='192.168.1.41', port=80,use_reloader=False)
    app.run(host="0.0.0.0", port=10000, use_reloader=False)
