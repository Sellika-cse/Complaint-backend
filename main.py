from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import ComplaintRequest, ComplaintCreate, AnalysisResponse
from services.nlp_service import classify_complaint, analyze_sentiment, extract_location
from database.supabase_client import supabase

app = FastAPI(
    title="Complaint Analytics API",
    description="NLP-based analytics for municipal complaints",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Complaint Analytics API is running!"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_complaint(request: ComplaintRequest):
    text = request.complaint_text

    if not text.strip():
        raise HTTPException(status_code=400, detail="Complaint text cannot be empty")

    # NLP Processing
    category = classify_complaint(text)
    sentiment, urgency = analyze_sentiment(text)
    location = extract_location(text)

    # Save to Supabase
    try:
        supabase.table('complaints').insert({
            "complaint_text": text,
            "category": category,
            "sentiment": sentiment,
            "urgency": urgency,
            "location": location,
        }).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return AnalysisResponse(
        complaint_text=text,
        category=category,
        sentiment=sentiment,
        urgency=urgency,
        location=location,
        message="Complaint analyzed and stored successfully"
    )


@app.post("/complaints")
def create_complaint(payload: ComplaintCreate):
    if not payload.complaint_text.strip():
        raise HTTPException(status_code=400, detail="Complaint text cannot be empty")

    try:
        supabase.table("complaints").insert(
            {
                "complaint_text": payload.complaint_text.strip(),
                "category": payload.category,
                "location": payload.location or "",
                "sentiment": "pending",
                "urgency": "pending",
            }
        ).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return {"message": "Complaint submitted successfully"}


@app.get("/complaints")
def get_complaints():
    try:
        result = supabase.table('complaints').select('*').execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")