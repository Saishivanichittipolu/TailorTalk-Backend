from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'tailortalk-credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

calendar_id = 'primary'

def get_upcoming_slots():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        maxResults=5,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    return [event['start'].get('dateTime', 'No time') for event in events]

def create_event(start_time, summary="Tailor Appointment"):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
    }
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return created_event
