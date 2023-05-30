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
from controller.levelManager import levelManagerClass
from controller.logManager import logManagerClass
class submissionManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def checkSubmissionDone():
        # print("addingggg")
        # listSubmissionClass.getListSubmission()
        file_path = os.path.join('data/submissionList.json')
        with open(file_path) as json_file:
            originalSubmissionList = json.load(json_file)
        foundQuest ="0"
        #loop data in all json data
        # for submission in submissions:
                # print(f"Submitted :"
                #     f"{(submission.get('id'),submission.get('userId'), submission.get('state'))}")
            # courseworkId = submission.get('courseWorkId')
            # submissionId= submission.get('id')
            # state = submission.get('state')
        for data in originalSubmissionList:
            # if find courseworkId == courseworkId in json
            targetCourseworkId = data.get('courseworkId')

            # test submissions
            # submissions=[{'courseId': '578789685769', 
            #             'courseWorkId': '610606036549', 
            #             'id': 'Cg4I1pqKqZgBEMXs0tfiEQ', 
            #             'userId': '104862493983664211514', 
            #             'creationTime': '2023-05-19T13:05:25.455Z', 
            #             'updateTime': '2023-05-19T14:37:04.693Z', 
            #             'state': 'RETURNED',
            #             'draftGrade': 10, 
            #             'assignedGrade': 14, 
            #             },
            #             {'courseId': '578789685769', 
            #             'courseWorkId': '610606036549', 
            #             'id': 'Cg4I1pqKqZgBEMXs0tfiEy', 
            #             'userId': '104862493983664211514', 
            #             'creationTime': '2023-05-19T13:05:25.455Z', 
            #             'updateTime': '2023-05-19T14:37:04.693Z', 
            #             'state': 'RETURNED',
            #             'draftGrade': 10, 
            #             'assignedGrade': 30, 
                            
            #             }   
            #             ]
            submissions=listSubmissionClass.getListSubmission(578789685769, targetCourseworkId)
            for submission in submissions:
                courseworkId = submission.get('courseWorkId')
                submissionId= submission.get('id')
                state = submission.get('state')
                if data.get('courseworkId') == courseworkId:
                    #loop eachSubmissionID in allsubmissionList
                    for eachSubmissionID in data['submissionList']:
                        
                        if submissionId == eachSubmissionID['submissionId']:
                            if state == "RETURNED" and eachSubmissionID['state']!="RETURNED":
                                QuestID=data.get('QuestID') 
                                userId=submission.get('userId')
                                assignedGrade=submission.get('assignedGrade')
                                print(f"Need to grade :"
                                        f"{(QuestID,userId,assignedGrade)}")
                                levelManagerClass.addExpFromQuest(QuestID,userId,assignedGrade)
                                eachSubmissionID['state']= "RETURNED"
                                log=f"Received {assignedGrade} EXP from Quest {QuestID}"
                                logManagerClass.addToLog(userId,log)
                                # submissionManagerClass.submissionGrade(QuestID,userId,assignedGrade)
                                # levelManagerClass.addExpToPlayer(eachSubmissionID['userId'])
                            break  
        levelManagerClass.updateLevel()
        with open('data/submissionList.json', 'w') as json_file:
            json.dump(originalSubmissionList, json_file, indent=4)                
        return "",200
        # #if that quest didn't in payload then create new one
        # if foundQuest=="0":
        #     newjs={
        #             "QuestID": "new",
        #             "studentIds": [
        #             ]
        #         }
        #     newjs['QuestID']=jsdata['QuestID']
        #     newjs['studentIds']=[jsdata['studentId']]
        #     originalSubmissionList.append(newjs)
        # with open('Backend/data/submissionList.json', 'w') as json_file:
        #     json.dump(originalSubmissionList, json_file, indent=4)
        # # Return the data as a JSON response
        # return json.dumps(originalSubmissionList)
    def submissionGrade(jsdata):
        
        return
    def addCourseworkToList(courseworkId,QuestID):
        file_path = os.path.join('data/submissionList.json')
        with open(file_path) as json_file:
            originalSubmissionList = json.load(json_file)
        submissions=listSubmissionClass.getListSubmission(578789685769, courseworkId)
         
        newjs={
                    "courseworkId": "new",
                    "QuestID": "new",
                    "submissionList": [
                        ]
                }
        newjs['courseworkId']=courseworkId
        newjs['QuestID']=QuestID
        print(submissions)
        for submission in submissions:
                userId = submission.get('userId')
                submissionId= submission.get('id')
                state = submission.get('state')
                submissionjs={
                    "userId": "new",
                    "submissionId": "new",
                    "state": "new"
                }
                submissionjs["userId"]=userId
                submissionjs["submissionId"]=submissionId
                submissionjs["state"]=state
                newjs['submissionList'].append(submissionjs)
        originalSubmissionList.append(newjs)
        with open('data/submissionList.json', 'w') as json_file:
            json.dump(originalSubmissionList, json_file, indent=4)
        return
if __name__ == '__main__':
    submissionManagerClass.checkSubmissionDone()
    # submissionManagerClass.addCourseworkToList(611995258807,"008")