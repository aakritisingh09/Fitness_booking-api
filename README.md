<<<<<<< HEAD
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
uvicorn app.main:app --reload

# 4. API Docs
Visit http://127.0.0.1:8000/docs
# Get classes
curl http://127.0.0.1:8000/classes

# Book a class
curl -X POST http://127.0.0.1:8000/book -H "Content-Type: application/json" \
     -d '{"class_id": 1, "client_name": "John Doe", "client_email": "john@example.com"}'

# Get bookings
curl http://127.0.0.1:8000/bookings?email=john@example.com
=======
# Fitness_booking-api
>>>>>>> f40221b11729deb0e21fe7959e0866c602499632
