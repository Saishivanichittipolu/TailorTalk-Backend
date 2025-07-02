from fastapi import FastAPI
from pydantic import BaseModel
from utils import get_upcoming_slots, create_event

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
def chat(data: ChatInput):
    user_msg = data.message.lower()

    if "available" in user_msg or "free slots" in user_msg:
        slots = get_upcoming_slots()
        return {"response": f"Here are upcoming slots: {slots}"}
    
    elif "book" in user_msg:
        # You can improve this to extract dynamic time later
        start_time = "2025-07-03T10:00:00+05:30"
        create_event(start_time)
        return {"response": f"✅ Appointment booked at {start_time}"}
    
    else:
        return {"response": "I can help book appointments! Try: 'Show available slots' or 'Book an appointment at 10 AM tomorrow'."}
