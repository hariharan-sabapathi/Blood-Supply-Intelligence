import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

blood_banks = [
    "Buffalo Blood Center",
    "NY Regional Blood Bank",
    "American Red Cross"
]

hospitals = [
    "Buffalo General",
    "Mercy Hospital",
    "Roswell Park",
    "Kenmore Mercy"
]

blood_types = [
    "A+","A-",
    "B+","B-",
    "AB+","AB-",
    "O+","O-"
]

while True:

    units_received = random.randint(0,20)
    units_used = random.randint(0,15)

    event = {
        "event_id": fake.uuid4(),
        "timestamp": datetime.utcnow().isoformat(),
        "blood_bank": random.choice(blood_banks),
        "hospital": random.choice(hospitals),
        "blood_type": random.choice(blood_types),
        "units_received": units_received,
        "units_used": units_used,
        "current_inventory": random.randint(20,500),
        "emergency_request": random.choice([True,False]),
        "city": "Buffalo",
        "state": "NY"
    }

    producer.send(
        "blood-events",
        value=event
    )

    print(event)

    time.sleep(2)