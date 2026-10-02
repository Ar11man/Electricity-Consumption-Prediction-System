import csv
from database import connect_database

file_path = "dataset/household_power_consumption.txt"

daily_consumption = {}

with open(file_path, "r", encoding="latin1") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        date = row["Date"]
        power = row["Global_active_power"]

        if power == "?":
            continue

        power = float(power)

        # Convert one-minute power from kW to kWh
        energy = power / 60

        if date not in daily_consumption:
            daily_consumption[date] = 0

        daily_consumption[date] += energy

        if len(daily_consumption) == 15:
            break

connection = connect_database()
cursor = connection.cursor()

for date, units in daily_consumption.items():
    query = """
    INSERT INTO consumption
    (consumer_name, date, units_consumed)
    VALUES (%s, STR_TO_DATE(%s, '%d/%m/%Y'), %s)
    """

    cursor.execute(
        query,
        ("Household", date, units)
    )

connection.commit()

cursor.close()
connection.close()

print("15 Kaggle dataset records imported successfully.")