class RailwayReservation:
    def __init__(self, passenger_name, train_name, seat_number):
        self.passenger_name = passenger_name
        self.train_name = train_name
        self.seat_number = seat_number

ticket1 = RailwayReservation("Rahul Sharma", "Rajdhani Express", "A1-21")

print(ticket1.passenger_name)
print(ticket1.train_name)
print(ticket1.seat_number)

class Reservation:
    def __init__(self, passenger_name, seat_number):

        self.passenger_name = passenger_name
        self.seat_number = seat_number

    def display_ticket(self):
        print("Passenger Name :", self.passenger_name)
        print("Seat Number    :", self.seat_number)
        print("---------------------------------")

ticket1 = Reservation("Rahul Sharma", "B1-21")
ticket2 = Reservation("Priya Singh", "B1-22")
ticket3 = Reservation("Amit Verma", "B1-23")

ticket1.display_ticket()
ticket2.display_ticket()
ticket3.display_ticket()

class RailwayReservation:

    def __init__(self, passenger_name, train_name, seat_nummber, ticket_price):

        self.passenger_name = passenger_name
        self.train_name = train_name
        self.seat_number = seat_nummber
        self.ticket_price = ticket_price
        print("Reservation Created Succesfully.")

    def display_ticket(self):
        print("------------------------------------")
        print("-----Railway Reservation Ticket-----")
        print("------------------------------------")
        print("Passenger Name :", self.passenger_name)
        print("Train_name     :", self.train_name)
        print("Seat Number    :", self.seat_number)
        print("Ticket Price   :", self.ticket_price)

    def __del__(self):
        print("Reservation Cancelled")

ticket1 = RailwayReservation("Neha Kapoor", "Rajdhani Expreess", "A1-25", 2450)
ticket1.display_ticket()
del ticket1

class car:
    def __init__(self):
        self.brand = "BMW"
        self._model = "XL"
        self.__price = "5000000"

c = car()

print(c.brand)
print(c._model) 
print(c._car__price)




