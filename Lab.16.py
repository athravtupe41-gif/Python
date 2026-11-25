import re 

def validate_pnr(pnr):
    pattern = r'^\d{8}$'
    if re.fullmatch(pattern, pnr):
        print("Valid PNR :", pnr)
    else:
        print("Invalid PNR :", pnr)

validate_pnr("43821756")
validate_pnr("6793452")
validate_pnr("8120AB63")
validate_pnr("81204763")

import re

def validate_seat(seat):
    pattern = r'^[A-Z][0-9]{1,2}$'
    if re.fullmatch(pattern, seat):
        print("Valid Seat Number :", seat)
    else:
        print("Invalid Seat Number :", seat)

validate_seat("B4")
validate_seat("A12")
validate_seat("D23")
validate_seat("b4")
validate_seat("23B")
validate_seat("A")

import re

def extract_train_numbers(text):
    pattern = r'\b[0-9]{4,5}\b'
    results = re.findall(pattern, text)
    print("Train Numbers Found :", results)
    return results

text = """
Booking confirmed for train 12951 Mumbai Rajdhani Express.
Passenger on train 12301 from Howrah to Delhi.
Train 12657 Bangalore Mail is on waitlist.
Coach number 4 berth 21 is assigned.
Train 19019 Dehradun Express departs at 06:20.
"""

extract_train_numbers(text)

import re

class Ticketvalidator:

    def  __init__(self, pnr, train_no, seat, fare):
        self.pnr = pnr
        self.train_no = train_no
        self.seat = seat
        self.fare = fare

    def validate(self):
        print("=" * 40)
        print("    Indrail Ticket Validation Report")
        print("=" * 40)

        if re.fullmatch(r'[0-9]{8}', self.pnr):
            print("pnr      :", self.pnr, "-> VALID")
        else:
            print("PNR      :", self.pnr, "-> INALID")


        if re.fullmatch(r'[0-9]{4,5}', self.train_no):
            print("Train No :", self.train_no,"-> VALID")
        else:
            print("Train No :", self.train_no, "-> INVALID")

        if re.fullmatch(r'[A-Z][0-9]{1,2}', self.seat):
            print("Seat :", self.seat, "-> Valid")
        else:
            print("Seat :", self.seat, "-> INVALID")

        if re.fullmatch(r'[0-9]{2,4}', self.fare):
            print("fare :", self.fare, "-> VALID")
        else:
            print("fare :", self.fare,"-> INVALID")

        print("=" * 40)

ticket1 = Ticketvalidator("43821756" , "12951" , "B4" , "880")
ticket2 = Ticketvalidator("6793452" , "1230x" , "b12" , "xx")

ticket1.validate()
ticket2.validate()

try:
    fare_amount = int(ticket1.fare)
    print("Ticket 1 Fare Conversion : SUCCESS")
except ValueError:
    print("Ticket 1 Fare Conversion : FAILED")

try:
    fare_amount = int(ticket2.fare)
    print("Ticket 2 Fare Conversion : SUCCESS")
except ValueError:
    print("Ticket 2 Fare Conversion : FAILED")
    