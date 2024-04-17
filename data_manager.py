import requests
from pprint import pprint

# Sheety config
SHEETY_URL = "https://api.sheety.co"
USERNAME = YOUR USERNAME GOES HERE
PROJECT_NAME = "flightDeals"
PRICE_SHEET_NAME = "prices"
USER_SHEET_NAME = "users"
headers = YOUR AUTH TOKEN GOES HERE

SHEETY_ENDPOINT = f"{SHEETY_URL}/{USERNAME}/{PROJECT_NAME}"


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        sheet_response.raise_for_status()
        data = sheet_response.json()
        # data = sheet_data
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{PRICE_SHEET_NAME}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = f"{SHEETY_ENDPOINT}/{USER_SHEET_NAME}"
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data


