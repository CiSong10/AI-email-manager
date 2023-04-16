from __future__ import print_function

import os.path
import os
import openai
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email import message_from_bytes

# for OpenAI API

openai.api_key = "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"
openai.Model.list()

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    emails = get_emails()
    answers = ai_classifier(emails)
    list_to_text(answers)


def get_emails(token_path='token.json', max_results=8, q='in:inbox'):
    """
    Use Gmail API to fetch the inbox emails
    :param token_path: the file path of the token
    :param max_results: how many emails to fetch
    :param q: which box of emails.
    :return: A list of dictionaries of which email subject and body are stored.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    emails = []
    try:
        # call the Gmail API to get the list of messages in the inbox
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', maxResults=max_results, q=q).execute()
        messages = results.get('messages', [])
        for message in messages:
            try:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()

                subject = 'Subject: {}'.format(
                    [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject'][0])

                # get the raw message data and decode it
                raw_data = msg['payload']['parts'][0]['body']['data']
                decoded_data = base64.urlsafe_b64decode(raw_data).decode('utf-8')
                # create an email object from the decoded data
                email = message_from_bytes(decoded_data.encode('utf-8'))
                # print the body of the email
                body = 'Body: {}'.format(email.get_payload())
                emails.append({'subject': subject, 'body': body})
            except:
                continue

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

    return emails


def ai_classifier(prompts: list):
    """
    Use ChatGPT to classify and summarize the email
    :param prompts: A list of dictionaries of which email subject and body are stored.
    :return: A list of ChatGPT answers
    """
    answers = []
    for prompt in prompts:
        answers.append(f"\n{prompt['subject']}")
        messages = [{"role": "system", "content": "I will provide you one email subject and body. Please try to "
                                                  "summarize the email and categorize it into one of the four "
                                                  "classes: \"To-Do\"s, \"Event\"s, \"Notification\"s, or \"Other\"s."},
                    {"role": "user", "content": f"{prompt['subject']} \n {prompt['body']}"}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        for choice in response['choices']:
            answer = choice['message']['content']
            answers.append(answer)

    return answers


def list_to_text(answers: list, file_path='email debrief.txt'):
    """
    Stores list into a text file
    :param answers: The list of ChatGPT answers
    :param file_path: The file of which the answers will be stored
    :return: None
    """
    with open(file_path, "w") as file:
        file.writelines([answer + "\n" for answer in answers])
    print("Success")


if __name__ == '__main__':
    main()
