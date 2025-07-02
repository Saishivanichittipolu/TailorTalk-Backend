import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

# Setup credentials from environment variable
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_INFO = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT'])

credentials = service_account.Credentials.from_service_account_info(
    SERVICE_ACCOUNT_INFO, scopes=SCOPES
)

# Initialize calendar API
service = build('calendar', 'v3', credentials=credentials)
calendar_id = 'primary'

# Fetch upcoming calendar slots
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

# Create a new calendar event
def create_event(start_time, summary="Tailor Appointment"):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
    }
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return created_event
