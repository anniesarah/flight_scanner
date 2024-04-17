from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = YOUR ORIGIN CITY IATA GOES HERE

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    if flight is None:
        continue

    try:
        if flight.price < destination["lowestPrice"]:
            users = data_manager.get_customer_emails()
            user_emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            msg = (f"Subject: {names}, There is a low price alert!\n\n"
                   f"Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                   f"to {flight.destination_city}-{flight.destination_airport}, "
                   f"from {flight.out_date} to {flight.return_date}."
                   )
            if flight.stop_overs > 0:
                msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification_manager.send_email(user_email=user_emails, msg=msg)

    except AttributeError:
        pass
