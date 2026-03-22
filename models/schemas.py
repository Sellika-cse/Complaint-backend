from pydantic import BaseModel

class ComplaintRequest(BaseModel):
    complaint_text: str


class ComplaintCreate(BaseModel):
    complaint_text: str
    category: str
    location: str


class AnalysisResponse(BaseModel):
    complaint_text: str
    category: str
    sentiment: str
    urgency: str
    location: str
    message: str