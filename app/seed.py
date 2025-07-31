from app.database import SessionLocal, engine
from app import models
from datetime import datetime
import pytz


models.Base.metadata.create_all(bind=engine)


db = SessionLocal()


ist = pytz.timezone("Asia/Kolkata")


classes = [
    models.FitnessClass(
        name="Yoga",
        instructor="Alice",
        datetime=ist.localize(datetime(2025, 8, 1, 7, 0)),
        total_slots=20,
        available_slots=20,
    ),
    models.FitnessClass(
        name="Zumba",
        instructor="Bob",
        datetime=ist.localize(datetime(2025, 8, 1, 9, 0)),
        total_slots=15,
        available_slots=15,
    ),
    models.FitnessClass(
        name="HIIT",
        instructor="Carol",
        datetime=ist.localize(datetime(2025, 8, 1, 18, 0)),
        total_slots=25,
        available_slots=25,
    ),
]


db.add_all(classes)


db.commit()


db.close()

print("Seed data added successfully.")
