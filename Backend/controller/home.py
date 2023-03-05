import os
import json
class homeClass:
    def hello_world():
        return "<p>Hello,XD World! XD</p>"
    def getAllQuest():
        file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'Testdata.json')
        
        # Load the contents of the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        
        # Return the data as a JSON response
        return json.dumps(data)
