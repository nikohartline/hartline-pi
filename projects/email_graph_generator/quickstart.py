from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import sys

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.compose'

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    sys.path.insert(0,'/home/pi/credentials')
    store = file.Storage('pi_token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('raspberrypi_gmail.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    main()