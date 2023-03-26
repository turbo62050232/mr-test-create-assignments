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
import datetime
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
    
    thst = datetime.timezone(datetime.timedelta(hours=7))

    # Set the due date to mouth 3 day 28, 2023 at 8:00 PM THST
    due_date = datetime.datetime(2023, 3, 28, 23, 59, 0, tzinfo=thst)
    #cvt = convert time to utc+0 timezone
    cvt = datetime.timezone(datetime.timedelta(hours=0))
    due_date = due_date.astimezone(cvt)

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # pylint: disable=maybe-no-member

    try:
        service = build('classroom', 'v1', credentials=creds)
        coursework = {
             "title": "time 2",
            "description": "This is an individual assignment for you to complete.",
            "dueDate": {
            "year": due_date.year,
            "month": due_date.month,
            "day": due_date.day,
            },
            "dueTime": {
            "hours": due_date.hour,
            "minutes": due_date.minute

            },
            "assigneeMode":"INDIVIDUAL_STUDENTS",
            "individualStudentsOptions": {
                "studentIds": [
                    # "111355848139463620207","104862493983664211514"
                    "104862493983664211514"
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
