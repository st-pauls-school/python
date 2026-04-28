# cribbed from https://developers.google.com/sheets/api/quickstart/python 
# 
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 

# n.b. the script is expecting a local file called credentials.json, see the quickstart guide above, 
# https://developers.google.com/sheets/api/quickstart/python#authorize_credentials_for_a_desktop_application 

# after the first run temporary credentials are then stored in a local file token.json 

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1SUaLalDw-sTdSGXy7BF7LMDHADRQZBc4uT76YotZrJI'
SAMPLE_RANGE_NAME = 'Analysis!C1:J8'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
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

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        if len(values) != 8:
            print("incorrect #rows")

        houses = []
        thisterm = []
        for i in range(len(values[0])):
            houses.append((values[0][i], values[1][i], values[2][i], values[3][i], values[4][i]))            
            thisterm.append((values[0][i], values[7][i], values[6][i]))            

        houses = sorted(houses, key=lambda h: h[2], reverse = True)

        output = []
        output.append("<HouseTable>\n")      
        for house in houses: 
            output.append(f'\t<Results house="{house[0]}" position="{house[1]}" points="{house[2]}" noshows="{house[3]}" unresolved="{house[4]}" />\n')
        output.append("</HouseTable>\n")
        with open("house-scoreboard.xml", "w") as hs:
            hs.writelines(output)

        output = []
        output.append("<ThisTerm>\n")      
        for house in thisterm: 
            output.append(f'\t<Results house="{house[0]}" position="{house[1]}" points="{house[2]}" />\n')
        output.append("</ThisTerm>\n")
        with open("house-scoreboard-term.xml", "w") as hs:
            hs.writelines(output)



    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()

