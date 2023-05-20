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

        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'students.json')
        userId = jsdata['userId']
        exp = jsdata['exp']
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
            with open('Backend/data/students.json', 'w') as json_file:
                json.dump(originalstudents, json_file, indent=4)
        return  json.dumps(originalstudents)
               