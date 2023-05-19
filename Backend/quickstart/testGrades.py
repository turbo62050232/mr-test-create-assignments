from __future__ import print_function
import os.path
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
def classroom_add_attachment(course_id, coursework_id, submission_id):
    """
    Adds attachment to existing course with specific course_id.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()
    # # pylint: disable=maybe-no-member
    # request = {
    #     'addAttachments': [
    #         {'link': {'url': 'http://example.com/quiz-results'}},
    #         {'link': {'url': 'http://example.com/quiz-reading'}}
    #     ]
    # }
    if os.path.exists('Backend/quickstart/token.json'):
            creds = Credentials.from_authorized_user_file('Backend/quickstart/token.json')
    try:
        service = build('classroom', 'v1', credentials=creds)
        # while True:
        #     coursework = service.courses().courseWork()
            # coursework.studentSubmissions().modifyAttachments(
            #     courseId=course_id,
            #     courseWorkId=coursework_id,
            #     id=submission_id).execute()
        studentSubmission = {
            'assignedGrade': 11
            # ,
            # 'draftGrade': 9
        }
        print("start")
        service.courses().courseWork().studentSubmissions().patch(
            courseId=course_id,
            courseWorkId=coursework_id,
            id=submission_id,
            updateMask='assignedGrade,draftGrade',
            body=studentSubmission).execute()
        print("end")
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
    # Put the course_id, coursework_id and submission_id of course in which
    # attachment needs to be added.
    #                         course_id,   coursework_id ,submission_id
    classroom_add_attachment(578789685769, 610606036549, 'Cg4I1pqKqZgBEMXs0tfiEQ')
    