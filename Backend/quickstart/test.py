from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Build the Classroom API client using the user's credentials

# oauth2_credentials='eyJhbGciOiJSUzI1NiIsImtpZCI6IjI1NWNjYTZlYzI4MTA2MDJkODBiZWM4OWU0NTZjNDQ5NWQ3NDE4YmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2Nzg0MzUwODEsImF1ZCI6IjQ1MDM4ODk4MDg3Ny1lYjlwZWdscGtrZG4zdjQ4dmQ0MGtmZGhqZDEyc3Q1YS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExMTM1NTg0ODEzOTQ2MzYyMDIwNyIsImhkIjoia21pdGwuYWMudGgiLCJlbWFpbCI6IjYyMDUwMjAwQGttaXRsLmFjLnRoIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjQ1MDM4ODk4MDg3Ny1lYjlwZWdscGtrZG4zdjQ4dmQ0MGtmZGhqZDEyc3Q1YS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiIwMjAwIFBPU1NBVEhPUk4gVEVFUkFOQVRFS1VMQ0hBSSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BR05teXhhRlJleDk0YXk0Tmt0UERqTkI0RmtZNkVVMWVUU2hGclllS2V1V1BBPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IjAyMDAiLCJmYW1pbHlfbmFtZSI6IlBPU1NBVEhPUk4gVEVFUkFOQVRFS1VMQ0hBSSIsImlhdCI6MTY3ODQzNTM4MSwiZXhwIjoxNjc4NDM4OTgxLCJqdGkiOiI4YjliZTJmOGFlNGY3N2VkOTgyMTM4NTk3YTJkOWYyOTIwNWE1YTBjIn0.apEeGN190MPKMll8xTEJ7orqNPKqRruU2rJG8nLigdq2by_P773is0AK-tbo4au8gaeksRGi4z2f4BQOGjpX7ovhULXm56UorknfR-GMzKSAjpEysPnnlV7-v3fn0Y4Z68Df2IDgeuSU8BLuvIGL9VRiFokSpuOHFTXnX_ZyLmWlMgVIH8ib__IngzVz8MLCVOSfMx7BrtUfl1_Eo-ZBoQbU23GQi-8fdvbwkZTGSYXIe3uombZ4idBciHWeZj36CWPtMSE37bYKgqeAbkZ-l0cPNHrksgcVrLqZIpnrg_sxIr2QIBfndC2XXBxTs_xe6W9atW-W0kDoZBoSBjJlxQ'
creds = Credentials.from_authorized_user_info(info=oauth2_credentials, scopes=['https://www.googleapis.com/auth/classroom.courses.readonly'])
# creds = oauth2_credentials
classroom = build('classroom', 'v1', credentials=creds)

# Call the courses.list endpoint to retrieve a list of courses for the user
results = classroom.courses().list().execute()

# Loop through the courses to find the one you're interested in
for course in results.get('courses', []):
    if course['id'] == '578789685769':
        # Call the courses.students.list endpoint to retrieve a list of students in the course
        students = classroom.courses().students().list(courseId=course['id']).execute()
        print("i'm in here!!!!")
        # Loop through the students to find the one with the matching email address
        # for student in students.get('students', []):
        #     if student['profile']['emailAddress'] == 'student@example.com':
        #         # Print the name of the matching student
        #         print(f'Student name: {student["profile"]["name"]["fullName"]}')
        #         break
        break
