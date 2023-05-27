import os
import json
class questBoardClass:
    def hello_world():
        print(os.listdir())
        return "<p>Hello,XD World! XD</p>"
    def getAllQuest(jsdata):
        userId = jsdata['userId']
        file_path = os.path.join('data/testData.json')
        file_path_students = os.path.join('data/students.json')
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        with open(file_path_students) as json_file:
            studens = json.load(json_file)
        # get level of student
        for s in studens :
            if s['userId'] == userId:
                level=s['level']
                break
        print("level")
        print(level)
        # level=3
        # Filter the data by visible=1 and check level requirement using list comprehension
        filtered_data = [d for d in data if d['visible'] == 1 and d['Requirement']<=level]
        # Return the data as a JSON response
        return json.dumps(filtered_data)