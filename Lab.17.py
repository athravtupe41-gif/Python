import requests
from bs4 import BeautifulSoup

class RailwayScraper:

    def __init__(self):
        self.base_url = "https://contentitvedant.github.io/Railway_Booking/"

    def get_soup(self, page):
        url      = self.base_url + page
        response = requests.get(url)
        soup     = BeautifulSoup(response.text, "html.parser")
        print("Fetched :", url, "| Status :", response.status_code)
        return soup

    def get_train_schedule(self):
        soup   = self.get_soup("trains.html")
        table  = soup.find(id="train-schedule-table")
        rows   = table.find("tbody").find_all("tr")
        trains = []
        for row in rows:
            cells = row.find_all("td")
            trains.append({
                "train_no"   : cells[0].get_text(),
                "train_name" : cells[1].get_text(),
                "from"       : cells[2].get_text(),
                "to"         : cells[3].get_text(),
                "departure"  : cells[4].get_text(),
                "arrival"    : cells[5].get_text(),
                "duration"   : cells[6].get_text(),
            })
        return trains

    def get_passengers(self):
        soup       = self.get_soup("passengers.html")
        table      = soup.find(id="passenger-records-table")
        rows       = table.find("tbody").find_all("tr")
        passengers = []
        for row in rows:
            passengers.append({
                "pnr"  : row["data-pnr"],
                "name" : row.find(class_="passenger-name").get_text(),
                "date" : row.find(class_="journey-date").get_text(),
                "class": row.find(class_="travel-class").get_text(),
                "seat" : row.find(class_="seat-number").get_text(),
                "fare" : row.find(class_="fare").get_text(),
            })
        return passengers

    def get_seat_availability(self):
        soup      = self.get_soup("seat-availability.html")
        table     = soup.find(id="seat-availability-table")
        rows      = table.find("tbody").find_all("tr")
        available = []
        for row in rows:
            available.append({
                "train_no"   : row["data-train"],
                "train_name" : row.find(class_="train-name").get_text(),
                "seats_sl"   : row.find(class_="seats-sl").get_text(),
                "seats_3a"   : row.find(class_="seats-3a").get_text(),
                "seats_2a"   : row.find(class_="seats-2a").get_text(),
                "seats_1a"   : row.find(class_="seats-1a").get_text(),
            })
        return available

scraper = RailwayScraper()

print("\n--- TRAIN SCHEDULE ---")
trains = scraper.get_train_schedule()
for t in trains:
    print(t["train_no"], "|", t["train_name"], "|", t["from"], "->", t["to"], "|", t["duration"])

print("\n--- PASSENGER RECORDS ---")
passengers = scraper.get_passengers()
for p in passengers:
    print("PNR:", p["pnr"], "| Name:", p["name"], "| Class:", p["class"], "| Seat:", p["seat"])

print("\n--- SEAT AVAILABILITY ---")
seats = scraper.get_seat_availability()
for s in seats:
    print("Train", s["train_no"], "-", s["train_name"], "| SL:", s["seats_sl"], "| 3A:", s["seats_3a"], "| 2A:", s["seats_2a"])
