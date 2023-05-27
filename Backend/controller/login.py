import os
import json
import requests
import jwt
class loginClass:
    def login(ACCESS_TOKEN):
        file_path = os.path.join('data/students.json')
        accessToken= ACCESS_TOKEN['accessToken']
        # Open the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)
        # Replace ACCESS_TOKEN with the access token you have
        # ACCESS_TOKEN = 'ya29.a0AVvZVsrE8K-6VSMciWEgDK68UbKPqpvg-ehMJKM7IPvS3w4qaG58t6SReLL1n4A7hLsBipxFZTekLj105jTgnKYLWYJTNzRXd8iXkdB7Fa2YARatv5pKuvoXHHOES3F0kt06zbD3m1rNRNfxbqoRRtfRKXXmbTcaCgYKAeASARISFQGbdwaIAAB3O-quQcOiVSnouCKRjQ0166'

        # Make a request to the userinfo endpoint to get the user's email address
        response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo',
                                headers={'Authorization': f'Bearer {accessToken}'})
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
if __name__ == '__main__':
    loginClass.emailLogin("turbo14301828@gmail.com")