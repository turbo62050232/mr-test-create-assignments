import os
import json
class questBoardClass:
    def hello_world():
        print(os.listdir())
        return "<p>Hello,XD World! XD</p>"
    def getAllQuest():
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'testData.json')
        
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        # Filter the data by visible=1 using list comprehension
        filtered_data = [d for d in data if d['visible'] == 1]
        # Return the data as a JSON response
        return json.dumps(filtered_data)
