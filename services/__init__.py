from sqlalchemy.orm import Session
from models import Complaint
from database import SessionLocal

class ComplaintService:
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all_complaints(self):
        return self.db.query(Complaint).all()

    def get_complaint_by_id(self, complaint_id: int):
        return self.db.query(Complaint).filter(Complaint.id == complaint_id).first()

    def create_complaint(self, title: str, description: str):
        complaint = Complaint(title=title, description=description)
        self.db.add(complaint)
        self.db.commit()
        self.db.refresh(complaint)
        return complaint

    def update_complaint_status(self, complaint_id: int, status: str):
        complaint = self.get_complaint_by_id(complaint_id)
        if complaint:
            complaint.status = status
            self.db.commit()
            self.db.refresh(complaint)
        return complaint

    def delete_complaint(self, complaint_id: int):
        complaint = self.get_complaint_by_id(complaint_id)
        if complaint:
            self.db.delete(complaint)
            self.db.commit()
        return complaint
