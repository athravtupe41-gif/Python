passenger_name = "Rahul Sharma"
ticket_status = "Confirmed"

if ticket_status == "Confirmed":
    print("Ticket is Confirmed")

waiting_status = 3
if waiting_status == 0:
    print("Ticket Confirmed")
else:
    print("Ticket is in Waiting List")

ticket_status = "RAC"
if ticket_status == "Confirmed":
    print("Seat Allocated Successfully")
elif ticket_status == "RAC":
    print("Partial Reservation Available")
else:
    print("Ticket is in Waiting List")

age = 65
if age >= 60:
    print("Passenger Eligible For Senior citizen Discount")

age = 65
is_ticket_confirmed = True

if age >=60 and is_ticket_confirmed == True:
    print("Passenger is Eligible for Senior citizen Benifits")

ticket_status = "Confiremd"
payment_status = "Paid"

if ticket_status == "Confiremd" and payment_status == "Paid":
    print("Ticket Booked Successfully")
elif ticket_status == "Rac":
    print("Partial Seat Reservation Available")
else:
 	print("Booking Pending")             