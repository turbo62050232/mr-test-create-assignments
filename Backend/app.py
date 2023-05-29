#----------------------Library-------------------------------------------
from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_cors import CORS
#----------------------Class Fucntion-----------------------------------
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
# CORS(app)
sched=APScheduler()
# Middleware function
@app.before_request
def middleware():
    print("testttt")
    if request.path == '/login' or request.path == '/':
        # Redirect to secure login page if the request is not secure and not for the login route
        return None
    # Perform middleware logic here
    # For example, you can access the request object and perform checks
    print(request.headers)
    substring = ""
    try:
        # if request.headers.get('Authorization')!="Bearer ":
        #     return "",401
        auth_header = request.headers.get('Authorization')
        substring = auth_header.split(" ")[1]
    except Exception as error:
        return "",401
    res=jwtManagerClass.decodeJWT(substring,"role")
    print(res["status"])
    if res["status"]>200:
        return  "",res["status"]
    print("passss")
    return None
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response
@app.route("/")
def index():
    # return "<p>XD</p>"
    res=questBoardClass.hello_world()
    return res
@app.route('/health')
def health():
  return '', 200
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    res=loginClass.login(data)
    return res
# Handle OPTIONS request explicitly
# @app.route('/', methods=['OPTIONS'])
# def handle_options():
#     response = jsonify({'message': 'success'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
#     return response
@app.route('/role', methods=['GET'])
def role():
    # data = request.get_json()
    # print(data)
    # res=loginClass.login(data)
    auth_header = request.headers.get('Authorization')
    substring = auth_header.split(" ")[1]
    role = jwtManagerClass.decodeJWT(substring,"role")
    print("test")
    print(role)
    return role,200
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    res=loginClass.register(data)
    return res
@app.route('/payloadAdd', methods=['POST'])
def payloadAdd():
    data = request.get_json()
    global current_date
    current_date = 1
    # print("now current_date =",current_date)
    print(data)
    res=payloadManagerClass.addStudentToQuest(data)
    # res=payloadManagerClass.hello_world(data)
    return res
@app.route('/questboard', methods=['GET'])
def questboard():
    print("start")
    # data = request.get_json()
    auth_header = request.headers.get('Authorization')
    substring = auth_header.split(" ")[1]
    data = jwtManagerClass.decodeJWT(substring,"userId")
    print("niceee")
    print(data)
    res=questBoardClass.getAllQuest(data)
    return res
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    data = request.get_json()
    res=leaderBoardClass.getLeaderBoard(data)
    return res
@app.route('/log', methods=['GET'])
def log():
    data = request.get_json()
    res=logManagerClass.getAllLog()
    return res
@app.route('/editquest', methods=['POST'])
def editquestjson():
    data = request.get_json()
    print(data)
    res=editQuestJsonClass.editQuestJson(data)
    return json.dumps(res)
current_date=0
@app.route('/dayset')
def dayset():
    global current_date
    current_date = 1
    res="this day...."
    return res
@app.route('/addExpToPlayer', methods=['POST'])
def addExpToPlayer():
    data = request.get_json()
    print(data)
    res=levelManagerClass.addExpToPlayer(data)
    return res



def job():
    global current_date
    # print("yessss") if current_date==1 else print("noo")
    payloadManagerClass.unloadpayload() if current_date==1 else print("noo")
    current_date = 0

if __name__ == '__main__':

    # create Scheduler to run every 5 seconds
    sched.add_job(id='job1',func=job, trigger= 'interval',seconds=10)
    # create Scheduler to run every day at 23:59 
    # sched.add_job(id='job1',func=job, trigger= 'cron',hour=23,minute=40)
    # sched.start()

    # app.run(host='192.168.1.41', port=80,use_reloader=False)
    app.run(host='0.0.0.0', port=10000,use_reloader=False)
# @app.route('/createcoursework')
# def createcoursework():
#     res=CourseworkClass.classroom_create_coursework(578789685769)
#     return res
# @app.route('/editquest')
# def editquest():
#     res=editQuestClass.editQuest()
#     return res