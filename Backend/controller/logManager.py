import os
import json
import datetime
# import sys module
import sys
# tell interpreter where to look
# sys.path.insert(0,"..")
# from quickstart.classroom_create_coursework import CourseworkClass
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from quickstart.listSubmission import listSubmissionClass
class logManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def addToLog(userId,log):
        # studentName,log
        file_path_student = os.path.join('data/students.json')
        with open(file_path_student) as json_file:
            studentsjson = json.load(json_file)
        for student in studentsjson:
            if student["userId"]==userId:
                studentName=student["studentName"]
        file_path = os.path.join('data/log.json')
        with open(file_path) as json_file:
            originalLog = json.load(json_file)
        thst = datetime.timezone(datetime.timedelta(hours=7))
        dateNow = datetime.datetime.now(tz=thst)
        dateOfLog = dateNow.strftime("%d/%m/%Y")
        # print(dateOfLog)
        # print(studentName)
        logNotFound=True
        for logEachDay in originalLog:
            if logEachDay["dateOfLog"]==dateOfLog:
                logjs={
                    "studentName": "new",
                    "log": "new"
                }
                logjs["studentName"]=studentName
                logjs["log"]=log
                logEachDay['logDetail'].append(logjs)
                logNotFound=False
                # print("same day")
                # print(originalLog)
                break
        if logNotFound:
            # print("not same day")
            newLog={
                    "dateOfLog": "new",
                    "logDetail": [ ]
                    }
            newLog["dateOfLog"]=dateOfLog
            logDetailjs={
                    "studentName": "new",
                    "log": "new"
                }
            logDetailjs["studentName"]=studentName
            logDetailjs["log"]=log
            newLog['logDetail'].append(logDetailjs)
            originalLog.append(newLog)
            # print("test")
            # print(originalLog)
        with open('data/log.json', 'w') as json_file:
            json.dump(originalLog, json_file, indent=4)
        return
    def test():
        exp=5
        quest="001"
        questdone=f"Received {exp} EXP from Quest {quest}"
        print(questdone)

        return "<p>Hello,XD World! XD</p>"
    def getAllLog():
        file_path = os.path.join('data/log.json')
        with open(file_path) as json_file:
            originalLog = json.load(json_file)
        return json.dumps(originalLog)
if __name__ == '__main__':
    # logManagerClass.addToLog("106904108283114831151","done 002")
    logManagerClass.test()