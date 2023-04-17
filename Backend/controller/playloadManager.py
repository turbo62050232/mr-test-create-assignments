import os
import json
class playloadManagerClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def addStudentToQuest(questId,studentId):
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payload.json')
        questId
        studentId
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            originalPlayload = json.load(json_file)

        for data in originalPlayload:
            if data.get('QuestID') == questId:
                data['studentIds']+=[studentId]
                break
        print(originalPlayload)
        # with open('Backend/data/payload.json', 'w') as f:
        #     json.dump(playload_file, f, indent=4)
        #     #     for key in modification_data:
        #     #         data[key] = modification_data[key]
        #     #     break
        #     # else: 
        #     # # if didn't find then create new one
        #     #     playload_file.append(modification_data) 
        #     #     break
        # dump this data to json file
        with open('Backend/data/payload.json', 'w') as json_file:
            json.dump(originalPlayload, json_file, indent=4)

        # Filter the data by visible=1 using list comprehension
        filtered_data = [d for d in data if d['visible'] == 1]
        # Return the data as a JSON response
        return json.dumps(filtered_data)
