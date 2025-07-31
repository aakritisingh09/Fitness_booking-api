from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def get_upcoming_classes(db: Session):
    now = datetime.now()
    return db.query(models.FitnessClass).filter(models.FitnessClass.datetime >= now).all()

def create_booking(db: Session, booking_request: schemas.BookingRequest):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking_request.class_id).first()
    if not fitness_class:
        raise ValueError("Fitness class not found")

    if fitness_class.available_slots <= 0:
        raise ValueError("No available slots")

    # Reduce available slots
    fitness_class.available_slots -= 1
    db.add(fitness_class)

    booking = models.Booking(
        class_id=booking_request.class_id,
        client_name=booking_request.client_name,
        client_email=booking_request.client_email,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()
