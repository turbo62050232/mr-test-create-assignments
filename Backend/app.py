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
from controller.levelManager import levelManagerClass
from quickstart.classroom_create_coursework import CourseworkClass
# ----------------------------------------------------------------------
app = Flask(__name__)
CORS(app)
sched=APScheduler()
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
@app.route('/questboard')
def questboard():
    res=questBoardClass.getAllQuest()
    return res
@app.route('/createcoursework')
def createcoursework():
    res=CourseworkClass.classroom_create_coursework(578789685769)
    return res
@app.route('/editquest')
def editquest():
    res=editQuestClass.editQuest()
    return res
@app.route('/editquestjson', methods=['POST'])
def editquestjson():
    data = request.get_json()
    print(data)
    res=editQuestJsonClass.editQuestJson(data)
    return res
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
    # sched.add_job(id='job1',func=job, trigger= 'interval',seconds=5)
    # create Scheduler to run every day at 23:59 
    sched.add_job(id='job1',func=job, trigger= 'cron',hour=23,minute=21)
    sched.start()

    # app.run(host='192.168.1.41', port=80,use_reloader=False)
    app.run(host='0.0.0.0', port=10000,use_reloader=False)