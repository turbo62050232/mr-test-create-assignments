import os
import json
class payloadManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def addStudentToQuest(jsdata):
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payload.json')
    
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
        with open('Backend/data/payload.json', 'w') as json_file:
            json.dump(originalpayload, json_file, indent=4)
        # Return the data as a JSON response
        return json.dumps(originalpayload)
    def unloadpayload():
        print()
