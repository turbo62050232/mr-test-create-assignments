from flask import Flask, request
from controller.questBoard import questBoardClass
from controller.editQuest import editQuestClass
from controller.editQuestJson import editQuestJsonClass
from quickstart.classroom_create_coursework import CourseworkClass
app = Flask(__name__)

@app.route("/")
def index():
    # return "<p>XD</p>"
    res=questBoardClass.hello_world()
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
if __name__ == '__main__':
    app.run(host='192.168.1.41', port=80)