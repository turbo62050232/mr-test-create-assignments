import os
import json
import datetime
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
file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payloadtest.json')
file_path_testData = os.path.join(os.path.dirname(__file__),'..', 'data', 'testData.json')   
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
                "assigneeMode":"INDIVIDUAL_STUDENTS",
                "individualStudentsOptions": {
                    "studentIds":targetQuest['studentIds']
                },
                "workType": "ASSIGNMENT",
                        'state': 'PUBLISHED',
            }
            CourseworkClass.classroom_create_coursework(coursework,578789685769)
            break 
        



# thst = datetime.timezone(datetime.timedelta(hours=7))
# dateNow = datetime.datetime.now(tz=thst)
# print("Current date and time:", dateNow)

# # Add 3 days to the current date
# dateAfter = dateNow + datetime.timedelta(days=3)
# print("Date and time 3 days later year:", dateAfter.year," month:", dateAfter.month," day:", dateAfter.day," hour:", dateAfter.hour," minute:",dateAfter.minute)


# CourseworkClass.classroom_create_coursework()
print(coursework)

{'title': 'QR and AR',
    'description': 'Will QR and AR relate to each other?', 
    'dueDate': {
    'year': 2023, 
    'month': 5, 
    'day': 16
    }, 
    'dueTime': {
    'hours': 23, 
    'minutes': 37
    
    }, 
    'assigneeMode': 'INDIVIDUAL_STUDENTS', 
    'individualStudentsOptions': {
        'studentIds': [
            '106904108283114831151', '104862493983664211514'
        ]
    }, 
    'workType': 'ASSIGNMENT', 
    'state': 'PUBLISHED'
    }