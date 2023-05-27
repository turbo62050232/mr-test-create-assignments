import os
import json
class leaderBoardClass:
    def hello_world():
        print(os.listdir())
        return "<p>Hello,XD World! XD</p>"
    def getLeaderBoard():
        file_path_students = os.path.join('data/students.json')
        # Load the contents of the JSON file
        # with open(file_path) as json_file:
        #     data = json.load(json_file)
        with open(file_path_students) as json_file:
            studens = json.load(json_file)
        leaderBoardjs='[]'
        leaderBoardjs = json.loads(leaderBoardjs)
        # getDataEachStudent
        for s in studens :
            studentjs={
                    "AvatarName": "new",
                    "CurrentLevel": "new",
                    "CurrentEXP": "new",
                    "NextLevelEXPNeeded": "new"
                }
            studentjs["AvatarName"]=s['studentName']
            studentjs["CurrentLevel"]=s['level']
            studentjs["CurrentEXP"]=s['exp']
            NextLevelEXPNeeded=50-s['exp']
            studentjs["NextLevelEXPNeeded"]=NextLevelEXPNeeded
            # append to leaderBoardjs
            leaderBoardjs.append(studentjs)
        print(leaderBoardjs)
        return json.dumps(leaderBoardjs)

if __name__ == '__main__':
    leaderBoardClass.getLeaderBoard()