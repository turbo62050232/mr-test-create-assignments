import os
import json
file_path = os.path.join(os.path.dirname(__file__),'..', 'data', 'payload.json')
questId ='009'
studentId = "1430"
# Load the contents of the JSON file
with open(file_path) as playload_file:
    originalPlayload = json.load(playload_file)
print(originalPlayload)
for data in originalPlayload:
    if data.get('QuestID') == questId:
        data['studentIds']+=[studentId]
        break
print("after = ")
print(originalPlayload)