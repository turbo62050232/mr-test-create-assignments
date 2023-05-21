from __future__ import print_function

import os.path
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students']


def classroom_list_submissions(course_id, coursework_id):
    """
    Creates the courses the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    if os.path.exists('Backend/quickstart/token.json'):
            creds = Credentials.from_authorized_user_file('Backend/quickstart/token.json', SCOPES)
    # pylint: disable=maybe-no-member
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
        for submission in submissions:
            print(f"Submitted at:"
                  f"{(submission.get('id'), submission.get('creationTime'))}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        submissions = None
    return submissions

def classroom_list_comment (course_id, coursework_id,submission_id):
    if os.path.exists('Backend/quickstart/token.json'):
            creds = Credentials.from_authorized_user_file('Backend/quickstart/token.json', SCOPES)
    # pylint: disable=maybe-no-member

    try:
        service = build('classroom', 'v1', credentials=creds)
        while True:
            commentsxd = service.courses().courseWork().studentSubmissions().comments().list(
                courseId=course_id,
                courseWorkId=coursework_id,
                submissionId=submission_id,
                includeDeleted=False,  # Set to True if you also want to include deleted comments
            ).execute()
            for comment in commentsxd['comments']:
                # Access the properties of each comment
                comment_id = comment['id']
                text = comment['text']
                # Process the comment as needed
                print(f"Comment ID: {comment_id}")
                print(f"Text: {text}")
    except HttpError as error:
        print(f"An error occurred: {error}")
    return 

if __name__ == '__main__':
    # Put the course_id and coursework_id of course whose list needs to be
    # submitted.
    # classroom_list_submissions(578789685769, 610606036549)
    classroom_list_comment(578789685769,610606036549,'Cg4I1pqKqZgBEMXs0tfiEQ')