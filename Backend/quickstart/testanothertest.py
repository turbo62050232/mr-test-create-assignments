import requests
import json

# Replace ACCESS_TOKEN with the access token you have
ACCESS_TOKEN = 'ya29.a0AVvZVsrE8K-6VSMciWEgDK68UbKPqpvg-ehMJKM7IPvS3w4qaG58t6SReLL1n4A7hLsBipxFZTekLj105jTgnKYLWYJTNzRXd8iXkdB7Fa2YARatv5pKuvoXHHOES3F0kt06zbD3m1rNRNfxbqoRRtfRKXXmbTcaCgYKAeASARISFQGbdwaIAAB3O-quQcOiVSnouCKRjQ0166'

# Make a request to the userinfo endpoint to get the user's email address
response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo',
                        headers={'Authorization': f'Bearer {ACCESS_TOKEN}'})

# Check if the request was successful
if response.status_code == 200:
    # Print the user's email address
    email = response.json()['email']
    print(email)
else:
    # Print an error message
    print(f'Error: {response.status_code} - {response.reason}')
# Open the JSON file
with open('./data/students.json') as f:
    data = json.load(f)

# Search for the student with the specified email
email_to_find = email
for student in data:
    if student["Email"] == email_to_find:
        print("Found student:", student)
        break
else:
    print("Student with email", email_to_find, "not found")
