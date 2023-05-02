#----------------------Library-------------------------------------------
from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_cors import CORS
#----------------------Class Fucntion-----------------------------------
from controller.questBoard import questBoardClass
from controller.editQuest import editQuestClass
from controller.editQuestJson import editQuestJsonClass
from controller.login import loginClass
from controller.playloadManager import playloadManagerClass
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
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    res=loginClass.login(data)
    return res
@app.route('/playloadAdd', methods=['POST'])
def playloadAdd():
    data = request.get_json()
    print(data)
    res=playloadManagerClass.addStudentToQuest(data)
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


def job():
    global current_date
    print("I'm working...")if current_date==1 else print("noo")
    current_date = 0

if __name__ == '__main__':

    # create Scheduler to run every 5 seconds
    sched.add_job(id='job1',func=job, trigger= 'interval',seconds=5)
    # create Scheduler to run every day at 23:59 
    # sched.add_job(id='job1',func=job, trigger= 'cron',hour=23,minute=59)
    sched.start()
    
    app.run(host='192.168.1.41', port=80,use_reloader=False)