import os
import json
from classroom_create_coursework import CourseworkClass
# class testpayloadManagerClass:
#     def unloadpayload():
#         file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payload.json')
    
#         # questId = jsdata['QuestID']
#         # studentId = jsdata['studentId']
#         # Load the contents of the JSON file
#         with open(file_path) as json_file:
#             payload = json.load(json_file)
#         print("test")
#         for quest in payload:
#             print(quest['QuestID'])


#         # CourseworkClass.classroom_create_coursework()
#         print()
file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payload.json')
file_path_testData = os.path.join(os.path.dirname(__file__),'..', 'data', 'testData.json')   
# questId = jsdata['QuestID']
# studentId = jsdata['studentId']
# Load the contents of the JSON file
with open(file_path) as json_file:
    payload = json.load(json_file)
with open(file_path_testData) as json_file:
    testData = json.load(json_file)
print("test")
for quest in payload:
    for findQuest in testData:
        if quest['QuestID']==findQuest['QuestID']:
            print(quest['QuestID'])
            print(findQuest['QuestName'])
            print(quest['studentIds'])



# CourseworkClass.classroom_create_coursework()
print()