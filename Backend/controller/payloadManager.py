import os
import json
import datetime
# import sys module
import sys
# tell interpreter where to look
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from quickstart.classroom_create_coursework import CourseworkClass
from controller.submissionManager import submissionManagerClass
class payloadManagerClass:
    def hello_world(jsdata):
        file_path_testData = os.path.join('data/payloadtest.json')
        with open(file_path_testData) as json_file:
            testData = json.load(json_file)
        return json.dumps(testData)
    def addStudentToQuest(jsdata):
        # print("addingggg")
        # file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payloadtest.json')

        file_path = os.path.join('data/payloadtest.json')
    
        questId = jsdata['QuestID']
        studentId = jsdata['studentId']
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            originalpayload = json.load(json_file)
        foundQuest ="0"
        #loop data in all json data
        for data in originalpayload:
            # if find questId == QuestID in json
            if data.get('QuestID') == questId:
                foundQuest="1"
                foundId="0"
                #loop studentIds in data
                for id in data['studentIds']:
                    #if repeated id 
                    if studentId ==id:
                        foundId="1"
                        break
                #if not repeated
                if  foundId=="0":
                    data['studentIds']+=[studentId]
                break     
        #if that quest didn't in payload then create new one
        if foundQuest=="0":
            newjs={
                    "QuestID": "new",
                    "studentIds": [
                    ]
                }
            newjs['QuestID']=jsdata['QuestID']
            newjs['studentIds']=[jsdata['studentId']]
            originalpayload.append(newjs)
        with open('data/payloadtest.json', 'w') as json_file:
            json.dump(originalpayload, json_file, indent=4)
        # Return the data as a JSON response
        print(originalpayload) 
        return json.dumps(originalpayload)
    def unloadpayload():
        # print("doingggg")
        # file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payloadtest.json')
        file_path = os.path.join('data/payloadtest.json')
        # file_path_testData = os.path.join(os.path.dirname(__file__),'..', 'data', 'testData.json')  
        file_path_testData = os.path.join('data/testData.json')
        # questId = jsdata['QuestID']
        # studentId = jsdata['studentId']
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            payload = json.load(json_file)
        with open(file_path_testData) as json_file:
            testData = json.load(json_file)
        print("test")

        thst = datetime.timezone(datetime.timedelta(hours=7))
        dateNow = datetime.datetime.now(tz=thst)
        print("Current date and time:", dateNow)
        for targetQuest in payload:
            for detailsQuest in testData:
                if targetQuest['QuestID']==detailsQuest['QuestID']:
                    dateAfter = dateNow + datetime.timedelta(days=detailsQuest['Duration'])
                    coursework = {
                        "title": detailsQuest['QuestName'],
                        "description": detailsQuest['Description'],
                        "dueDate": {
                        "year": dateAfter.year,
                        "month": dateAfter.month,
                        "day": dateAfter.day,
                        },
                        "dueTime": {
                        "hours": dateAfter.hour,
                        "minutes": dateAfter.minute

                        },
                        "maxPoints": detailsQuest['Reward'],
                        "assigneeMode":"INDIVIDUAL_STUDENTS",
                        "individualStudentsOptions": {
                            "studentIds":targetQuest['studentIds']
                        },
                        "workType": "ASSIGNMENT",
                                'state': 'PUBLISHED',
                    }
                    courseworkId=CourseworkClass.classroom_create_coursework(coursework,578789685769)
                    submissionManagerClass.addCourseworkToList(courseworkId,detailsQuest['QuestID'])
                    break 
            print()
        return 

