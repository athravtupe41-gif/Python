def welcome__message ():
    print("=========================")
    print(" Indian Railway Reservation ")
    print("=========================")
    print(" Welcome to Railway Reservation System")

welcome__message ()

def book_ticket(passenger_name, train_name):
   print("Passenger Name     :", passenger_name)
   print("Train Name         :", train_name)
   print("Reservation Status : Confirmed")

book_ticket("Rahul Sharma", "Rajdhani Express")

def calculate_fare(ticket_price, passengers):
    total_amount = ticket_price * passengers
    return total_amount

final_fare = calculate_fare(2450, 2)
print("Final Fare :", final_fare)

def verify_passenger(age):
   if age >= 18:
       return "Eligible for Reservation"
   else:
       return "Not Eligible"

result = verify_passenger(25)
print(result)

def generate_ticket(
   passenger_name,
   train_name,
   seat_number):
   print("===================================")
   print(" Railway Reservation Ticket ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Train Name :", train_name)
   print("Seat Number :", seat_number)

generate_ticket(
   "Priya Singh",
   "Shatabdi Express",
   "B2-21")

def final_booking_system():

   passenger_name = "Rahul Sharma"
   train_name = "Rajdhani Express"
   seat_number = "A1-12"
   ticket_price = 2450

   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Passenger Name :", passenger_name)
   print("Train Name :", train_name)
   print("Seat Number :", seat_number)
   print("Ticket Price :", ticket_price)
   print("Reservation Confirmed")

final_booking_system()




