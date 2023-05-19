import requests
import json

url = "https://classroom.googleapis.com/v1/courses/578789685769/courseWork/610422162098/studentSubmissions/Cg4I1pqKqZgBELKF_P_hEQ"

payload = json.dumps({
  "state": "RETURNED"
})
headers = {
  'Authorization': 'Bearer ya29.a0AWY7CknLWNyKtBPFxTetJIlf2PKqy4BP6DbnL1sdTl0ANJKwvy2FCOfQNz4B2AGOud2iTXC5a_vMpHO4a0eL6biGfbcyxj4yZLlDe4QmWVta7KkG49UIokrP0A8tuEE2iKkH792zJ46xJ-RmSiC7Wan-dlAU31IkOQaCgYKATASARMSFQG1tDrpKV5UTj43ZeqExsk2meOt8g0169',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
