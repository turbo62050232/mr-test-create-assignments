import os
import sys
# sys.path.append('/Backend')
# sys.path.insert(0,"..")
# from quickstart.listSubmission import listSubmissionClass
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from quickstart.listSubmission import listSubmissionClass
# from submissionManager import submissionManagerClass


print("testttt::::")
# submissionManagerClass.checkSubmissionDone()
# print(sys.path)
# E:\\GitHub\\mr-test-create-assignments\\Backend\\controller

[{'courseId': '578789685769', 
  'courseWorkId': '610606036549', 
  'id': 'Cg4I1pqKqZgBEMXs0tfiEQ', 
  'userId': '104862493983664211514', 
  'creationTime': '2023-05-19T13:05:25.455Z', 
  'updateTime': '2023-05-19T14:37:04.693Z', 
  'state': 'RETURNED',
  'draftGrade': 10, 
  'assignedGrade': 10, 
  },
  {'courseId': '578789685769', 
  'courseWorkId': '610606036549', 
  'id': 'Cg4I1pqKqZgBEMXs0tfiEy', 
  'userId': '104862493983664211514', 
  'creationTime': '2023-05-19T13:05:25.455Z', 
  'updateTime': '2023-05-19T14:37:04.693Z', 
  'state': 'RETURNED',
  'draftGrade': 10, 
  'assignedGrade': 10, 
      
  }   
]