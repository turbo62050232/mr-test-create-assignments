"""
Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
# [START classroom_create_coursework]
from __future__ import print_function
import os.path
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students']
def classroom_create_coursework(course_id):

    """
    Creates the coursework the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # pylint: disable=maybe-no-member

    try:
        service = build('classroom', 'v1', credentials=creds)
        coursework = {
             "title": "Individual Assignment test",
            "description": "This is an individual assignment for you to complete.",
            "dueDate": {
            "year": 2022,
            "month": 12,
            "day": 19
            },
            "dueTime": {
            "hours": 20,
            "minutes": 0
            },
            "assigneeMode":"INDIVIDUAL_STUDENTS",
            "individualStudentsOptions": {
                "studentIds": [
                    "111355848139463620207"
                ]
            },
            
            "workType": "ASSIGNMENT",
                    'state': 'PUBLISHED',
        }
        coursework = service.courses().courseWork().create(
            courseId=course_id, body=coursework).execute()
        print(f"Assignment created with ID {coursework.get('id')}")
        return coursework

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    # Put the course_id of course whose coursework needs to be created,
    # the user has access to.
    classroom_create_coursework(578789685769)
# [END classroom_create_coursework]
