import os
import json
class editQuestJsonClass:
    def editQuestJson(modification_data):
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'testData.json')
        traget = modification_data['QuestID']
        # Open the JSON file
        with open(file_path) as json_file:
            original_data = json.load(json_file)

        # # Find the object with id=2 and modify the name field
        # for item in data:
        #     if item['QuestID'] == "001":
        #         item['Reward'] = '10xp'
        
        # Modify the original JSON data with the modification data
        for data in original_data:
            if data.get('QuestID') == traget:
                for key in modification_data:
                    data[key] = modification_data[key]

        with open('Backend/data/testedit.json', 'w') as f:
            json.dump(original_data, f, indent=4)
        with open('Backend/data/testedit.json') as json_file:
            redata = json.load(json_file)
        filtered_data = [d for d in redata if d['QuestID'] == traget] 
        return  json.dumps(filtered_data)
# ------------------------------------------------------------------
        # # Write the updated data back to the file
        # with open(file_path, 'w') as json_file:
        #     json.dump(data, json_file, indent=4)
        # with open(file_path) as json_file:
        #     data = json.load(json_file)
        # filtered_data = [d for d in data if d['QuestID'] == "001"]   
        # return json.dumps(filtered_data)