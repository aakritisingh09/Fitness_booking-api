from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/classes", response_model=list[schemas.ClassOut])
def get_classes(db: Session = Depends(get_db)):
    return crud.get_upcoming_classes(db)

@app.post("/book", response_model=schemas.BookingOut)
def book_class(request: schemas.BookingRequest, db: Session = Depends(get_db)):
    return crud.create_booking(db, request)

@app.get("/bookings", response_model=list[schemas.BookingOut])
def get_bookings(email: str, db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
