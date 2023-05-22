from __future__ import print_function
import os.path
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
class listSubmissionClass:
    def getListSubmission(course_id, coursework_id):
        """
        Adds attachment to existing course with specific course_id.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
        """
        # creds, _ = google.auth.default()
        # pylint: disable=maybe-no-member
        # request = {
        #     'addAttachments': [
        #         {'link': {'url': 'http://example.com/quiz-results'}},
        #         {'link': {'url': 'http://example.com/quiz-reading'}}
        #     ]
        # }
        if os.path.exists('Backend/quickstart/token.json'):
                creds = Credentials.from_authorized_user_file('Backend/quickstart/token.json')
        submissions = []
        page_token = None
        try:
            service = build('classroom', 'v1', credentials=creds)
            while True:
                coursework = service.courses().courseWork()
                response = coursework.studentSubmissions().list(
                    pageToken=page_token,
                    courseId=course_id,
                    courseWorkId=coursework_id,
                    pageSize=10).execute()
                submissions.extend(response.get('studentSubmissions', []))
                page_token = response.get('nextPageToken', None)
                if not page_token:
                    break

            if not submissions:
                print('No student submissions found.')

            print('Student Submissions:')
            # print(submission)
            for submission in submissions:
                print(f"Submitted :"
                    f"{(submission.get('courseWorkId'),submission.get('id'),submission.get('userId'), submission.get('state'))}")
            return submissions

        except HttpError as error:
            print(f"An error occurred: {error}")


if __name__ == '__main__':
    # Put the course_id, coursework_id and submission_id of course in which
    # attachment needs to be added.
    # classroom_add_attachment(578789685769, 610422162098)
    #Cg4I1pqKqZgBELKF_P_hEQ    "submitId"
    # classroom_add_attachment(578789685769, 610453515530)
    #Cg4I1pqKqZgBEIra9Y7iEQ    "submitId"
    # classroom_add_attachment(578789685769, 610459297953)
    #Cg4I1pqKqZgBEKHR1pHiEQ    "submitId"
    # classroom_add_attachment(578789685769, 610606036549)
    #Cg4I1pqKqZgBEMXs0tfiEQ    "submitId"
    listSubmissionClass.getListSubmission(578789685769, 610818485767)
    #Cg4I1pqKqZgBEMXs0tfiEQ    "submitId"
    