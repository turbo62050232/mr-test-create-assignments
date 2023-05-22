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
# from controller.levelManager import levelManagerClass
class submissionManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def checkSubmissionDone():
        # print("addingggg")
        # listSubmissionClass.getListSubmission()
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'submissionList.json')
    
        # courseworkId = jsdata['courseworkId']
        # submissionId=jsdata['submissionId']
        # state = jsdata['state']
        # Load the contents of the JSON file
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
            submissions=listSubmissionClass.getListSubmission(578789685769, targetCourseworkId)
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
            for submission in submissions:
                courseworkId = submission.get('courseWorkId')
                submissionId= submission.get('id')
                state = submission.get('state')
                if data.get('courseworkId') == courseworkId:
                    foundQuest="1"
                    foundId="0"
                    #loop states in data

                    for eachSubmissionID in data['submissionList']:
                        #if repeated id 
                        
                        if submissionId == eachSubmissionID['submissionId']:
                            if state == "RETURNED" and eachSubmissionID['state']=="TURNED_IN":
                                foundId="1"
                                QuestID=data.get('QuestID') 
                                userId=submission.get('userId')
                                assignedGrade=submission.get('assignedGrade')
                                print(f"Need to grade :"
                                        f"{(QuestID,userId,assignedGrade)}")
                                # submissionManagerClass.submissionGrade(QuestID,userId,assignedGrade)
                                # levelManagerClass.addExpToPlayer(eachSubmissionID['userId'])
                            break
                        
        return
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
if __name__ == '__main__':
    submissionManagerClass.checkSubmissionDone()