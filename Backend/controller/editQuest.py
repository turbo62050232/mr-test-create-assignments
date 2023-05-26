import os
import json
class editQuestClass:
    def editQuest():
        file_path = os.path.join('data/testData.json')
        
        # Open the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)

        # Find the object with id=2 and modify the name field
        for item in data:
            if item['QuestID'] == "001":
                item['Reward'] = '10xp'

        # Write the updated data back to the file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        with open(file_path) as json_file:
            data = json.load(json_file)
        filtered_data = [d for d in data if d['QuestID'] == "001"]   
        return json.dumps(filtered_data)