import os
import json
import requests
import jwt
class loginClass:
    def login(jsdata):
        file_path = os.path.join('data/students.json')
        accessToken= jsdata['accessToken']
        
        # Open the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        # Replace ACCESS_TOKEN with the access token you have
        # ACCESS_TOKEN = 'ya29.a0AWY7CkkR1TUSb2UdY4vexoozDXQCOTr8UQ6G-I_qvtwWxVTaPQ_Xlj3j9-PD9-GlhTdk9FXHzApP9vr17Iu0_RXzGWZWq5X10Dhxhe-ia3SANBhl9Si0x4a07pmJujbkTVYo3hultv30dE2orl-SbadhO099C84aCgYKAYUSARISFQG1tDrpIT-b8XqwSk2dyxnCqQzu4g0166'
        # accessToken = ACCESS_TOKEN
        # Make a request to the userinfo endpoint to get the user's email address
        response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo',
                                headers={'Authorization': f'Bearer {accessToken}'})
        print(response.json())
        # Check if the request was successful
        if response.status_code == 200:
            # Print the user's email address
            email = response.json()['email']
            print(email)
        else:
            # Print an error message
            print(f'Error: {response.status_code} - {response.reason}')

        # # Search for the student with the specified email
        # traget = ACCESS_TOKEN['email']
        # email_to_find = traget
        # email_to_find = "62050232@kmitl.ac.th"
        
        email_to_find=email
        # email_to_find=ACCESS_TOKEN['accessToken']
        for student in data:
            if student["email"] == email_to_find and student["studentName"]!="N/A":
                # print("Found student:", student)
                # studentFound=student
                # create jwt token
                encoded_jwt = jwt.encode({
                                    'studentName': student["studentName"],
                                    'role': student["role"],
                                    'userId': student["userId"],
                                    'studentId': student["studentId"]
                                  }, 
                                  'secret', algorithm='HS256')
                # print(encoded_jwt)
                # create json for return
                statusjs={
                    "status": "OK",
                    "encoded_jwt": encoded_jwt,
                    "role":student["role"]
                }
                break
            elif student["email"] == email_to_find and student["studentName"]=="N/A":
                statusjs={
                    "status": "Register",
                    "encoded_jwt": ""
                }
                return json.dumps(statusjs)
        else:
            studentId = email.split("@")[0]
            newStudentjs={
                    "studentId": studentId,
                    "userId": response.json()['id'],
                    "studentName": "N/A",
                    "email": response.json()['email'],
                    "role": "student",
                    "level": 0,
                    "exp": 0,
                    "questList": [
                        ]
                }
            data.append(newStudentjs)
            with open('data/students.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            statusjs={
                    "status": "Register",
                    "encoded_jwt": ""
                }
            # print("Student with email", email_to_find, "not found")
        print(statusjs)
        return json.dumps(statusjs)
    def emailLogin(email_to_find):
        file_path = os.path.join('data/students.json')
        # Open the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        for student in data:
            if student["email"] == email_to_find:
                # print("Found student:", student)
                # studentFound=student
                # create jwt token
                encoded_jwt = jwt.encode({
                                    'studentName': student["studentName"],
                                    'role': student["role"],
                                    'userId': student["userId"],
                                    'studentId': student["studentId"]
                                  }, 
                                  'secret', algorithm='HS256')
                # print(encoded_jwt)
                # create json for return
                statusjs={
                    "status": "OK",
                    "encoded_jwt": encoded_jwt
                }
                break
        else:
            statusjs={
                    "status": "Register",
                    "encoded_jwt": ""
                }
            # print("Student with email", email_to_find, "not found")
        print(statusjs)
        return json.dumps(statusjs)
    def decodeJWT(encoded_jwt):
        # saving the header claims into a variable
        # header_data = jwt.get_unverified_header(token)
        # using that variable in the decode method
        try:
            decode_jwt=jwt.decode(
                encoded_jwt,
                key='secret',
                algorithms=['HS256']
            )
            print(decode_jwt)
        except Exception as error:
            print(f"An error occurred:{error}")
            return error,403

        return
    def register(jsdata):
        studentName=jsdata["AvatarName"]
        userId="111355848139463620207"
        file_path_students = os.path.join('data/students.json')
        with open(file_path_students) as json_file:
            students = json.load(json_file)
        for student in students:
            if student["userId"]==userId and student["studentName"]=="N/A":
                student["studentName"]=studentName
                break
        with open('data/students.json', 'w') as json_file:
                json.dump(students, json_file, indent=4)

        return
if __name__ == '__main__':
    loginClass.emailLogin("turbo14301828@gmail.com")
    # loginClass.decodeJWT("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50TmFtZSI6InR1cmJvIHRlbWUiLCJyb2xlIjoidGVhY2hlciIsInVzZXJJZCI6IjEwNDg2MjQ5Mzk4MzY2NDIxMTUxNCIsInN0dWRlbnRJZCI6IjYyMDUwMjMyeGQifQ.kTY4yOuexIxFuRVodhrOXZJh0HEjP_AqsBl73nIucm8")
    # loginClass.login()
    # loginClass.register()