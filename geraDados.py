from datetime import datetime
import json
import time
import random
while True:
    # Generate a random date between today and 30 days ago
    random_date = {
        "data_hora": datetime.strftime(datetime.utcnow(), "%Y-%m-%d, %H:%M:%S%Z"),
        "data": datetime.strftime(datetime.utcnow(), "%Y-%m-%d"),
        "hora": datetime.strftime(datetime.utcnow(), "%H:%M:%S"),
        "hora_h": datetime.strftime(datetime.utcnow(), "%H"),
        "evento": "in"
    }
    # Load the existing dates from the JSON file
    try:
        with open("dates.json", "r") as f:
            dates = json.load(f)
    except (json.decoder.JSONDecodeError, KeyError):
            dates = []
    # Append the new date to the array
    dates.append(random_date)
    # Save the updated array to the JSON file
    with open("dates.json", "w") as f:
            json.dump(dates, f)
    # Wait a random amount of time between 0 and 10 seconds
    time.sleep(7*random.random())
    print(random_date)
