import os
import json
import datetime
# import sys module
import sys
# tell interpreter where to look
sys.path.insert(0,"..")
from quickstart.classroom_create_coursework import CourseworkClass
class levelManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def addExpToPlayer(jsdata):
        userId = jsdata['userId']
        exp = jsdata['exp']
        file_path = os.path.join('data/students.json')
        with open(file_path) as json_file:
            originalstudents = json.load(json_file)
        # foundStudentId ="0"
        for data in originalstudents:
            # if find questId == QuestID in json
            if data.get('userId') == userId:
                # foundStudentId="1"
                # foundId="0"
                data['exp']+=exp
                # addLevel if exp >=50
                if data['exp']>=50:data['level']+=(data['exp']//50);data['level'];data['exp']=(data['exp']%50)
                # removeLvel if exp <0
                if data['exp']<0:data['level']+=(data['exp']//50);data['level'];data['exp']=(data['exp']%50)
            with open('data/students.json', 'w') as json_file:
                json.dump(originalstudents, json_file, indent=4)
        return  json.dumps(originalstudents)
    def addExpFromQuest(QuestID,userId,assignedGrade):
        file_path = os.path.join('data/students.json')
        with open(file_path) as json_file:
            originalstudents = json.load(json_file)
        for data in originalstudents:
            # if find questId == QuestID in json
            if data.get('userId') == userId:
                for quest in data["questList"]:
                    if quest.get('QuestID') == QuestID:
                        quest['expGained']=assignedGrade
                        quest['state']="done"
        with open('data/students.json', 'w') as json_file:
                json.dump(originalstudents, json_file, indent=4)

        return
if __name__ == '__main__':
    levelManagerClass.addExpFromQuest("008","106904108283114831151",1430)     