# cribbed from https://developers.google.com/sheets/api/quickstart/python
#
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# n.b. the script is expecting a local file called credentials.json, see the quickstart guide above,
# https://developers.google.com/sheets/api/quickstart/python#authorize_credentials_for_a_desktop_application

# after the first run temporary credentials are then stored in a local file token.json

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SPREADSHEET_ID = '1SUaLalDw-sTdSGXy7BF7LMDHADRQZBc4uT76YotZrJI'
DATA_RANGE = 'Analysis!C1:J8'

# Row indices within the spreadsheet range
ROW_NAME       = 0
ROW_POSITION   = 1
ROW_POINTS     = 2
ROW_NOSHOWS    = 3
ROW_UNRESOLVED = 4
ROW_TERM_POINTS   = 6
ROW_TERM_POSITION = 7


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID, range=DATA_RANGE
        ).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        if len(values) != 8:
            print("incorrect #rows")
            return

        houses = []
        thisterm = []
        for i in range(len(values[0])):
            houses.append((
                values[ROW_NAME][i], values[ROW_POSITION][i], values[ROW_POINTS][i],
                values[ROW_NOSHOWS][i], values[ROW_UNRESOLVED][i]
            ))
            thisterm.append((
                values[ROW_NAME][i], values[ROW_TERM_POSITION][i], values[ROW_TERM_POINTS][i]
            ))

        houses   = sorted(houses,   key=lambda h: h[2], reverse=True)
        thisterm = sorted(thisterm, key=lambda h: h[2], reverse=True)

        output = ["<HouseTable>\n"]
        for house in houses:
            output.append(f'\t<Results house="{house[0]}" position="{house[1]}" points="{house[2]}" noshows="{house[3]}" unresolved="{house[4]}" />\n')
        output.append("</HouseTable>\n")
        with open("house-scoreboard.xml", "w") as hs:
            hs.writelines(output)

        output = ["<ThisTerm>\n"]
        for house in thisterm:
            output.append(f'\t<Results house="{house[0]}" position="{house[1]}" points="{house[2]}" />\n')
        output.append("</ThisTerm>\n")
        with open("house-scoreboard-term.xml", "w") as hs:
            hs.writelines(output)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
