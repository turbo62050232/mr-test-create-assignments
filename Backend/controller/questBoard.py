import os
import json
import datetime
class questBoardClass:
    def hello_world():
        print(os.listdir())
        return "<p>Hello,XD World! XD</p>"
    def getAllQuest(userId):
        # userId = jsdata['userId']
        # thst = datetime.timezone(datetime.timedelta(hours=7))
        # dateNow = datetime.datetime.now(tz=thst)
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
        filtered_data = [d for d in data if d['visible'] == 1 and d['Requirement']<=level and questBoardClass.checkQuestExpire(d['QuestExpire'])=="before"]
        # Return the data as a JSON response
        # print(filtered_data)
        return json.dumps(filtered_data)
    def checkQuestExpire(QuestExpire):
        thst = datetime.timezone(datetime.timedelta(hours=7))
        dateNow = datetime.datetime.now(tz=thst)
        # print(dateNow.day)
        # print(dateNow.month)
        # print(dateNow.year)
        # print(QuestExpire) 
        if QuestExpire =="N/A":
            return "before"
        string_datetime = datetime.datetime.strptime(QuestExpire, "%d/%m/%Y").replace(tzinfo=thst)
        if dateNow<string_datetime:
            return "before"
        else :return "after"
        
if __name__ == '__main__': 
    # questBoardClass.checkQuestExpire()
    questBoardClass.getAllQuest("106904108283114831151")