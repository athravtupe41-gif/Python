def reservation_status(
   passenger_name,
   ticket_status="Confirmed"):
   print("Passenger Name :", passenger_name)
   print("Ticket Status :", ticket_status)

reservation_status("Rahul Sharma")
reservation_status("Amit Verma", "Waiting")

def passenger_booking(*passengers):
   print("Passenger List:")
   for name in passengers:
       print("Passenger :", name)

passenger_booking(
   "Rahul Sharma",
   "Priya Singh",
   "Amit Verma",
   "Neha Kapoor")

def ticket_details(**details):
   print("Ticket Information:")
   for key, value in details.items():
       print(key, ":", value)

ticket_details(
   passenger_name="Rahul Sharma",
   train_name="Rajdhani Express",
   seat_number="B1-21",
   fare=2500,
   status="Confirmed")

def seat_countdown(seats):
   if seats == 0:
       print("All Seats Booked")
       return
   print("Remaining Seats :", seats)
   seat_countdown(seats - 1)

print (seat_countdown(5))

def verify_passenger(passenger_number):
   if passenger_number == 0:
       print("Verification Completed")
       return
   print("Verifying Passenger :", passenger_number)
   verify_passenger(passenger_number - 1)

print(verify_passenger(3))

def final_booking(
   train_name="Rajdhani Express",
   *seat_numbers
):
   print("===================================")
   print(" Railway Reservation ")
   print("===================================")
   print("Train Name :", train_name)
   for seat in seat_numbers:
       print("Allocated Seat :", seat)

final_booking(
   "Rajdhani Express",
   "B1-21",
   "B1-22",
   "B1-23")


