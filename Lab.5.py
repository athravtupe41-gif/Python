passenger_age = 25
ticket_confirmed = True

if passenger_age >= 18 and ticket_confirmed:
    print("passenger is eligible for Travel")

confirmed_seat = False
rac_seat = True

if confirmed_seat or rac_seat:
    print("Reservation available")

ticket_cancel = False

if not ticket_cancel:
    print("Ticket Active")

passenger_age = 65
payment_complete = True

if passenger_age >= 65 and payment_complete:
    print("senior citizen reservation approved")

available_seats = 5
payment_status = True

if available_seats > 0 and payment_status:
    print("ticket confirmed sucessfully")
else:
    print("Reservation Failed")

vaild_id_proof = True
booking_time_valid = True

if vaild_id_proof and booking_time_valid:
    print("Tatkal Booking Allowed")
else:
    print("Tatkal Booking Denied")

passenger_name = "Rahul Sharma"
passenger_age = 30
available_seats = 2
payment_complete = True
ticket_cancel = False

if passenger_age >= 18 and available_seats > 0 and payment_complete and not ticket_cancel:
    print("---------------------------------------------")
    print("------Indian Railway Reservation Ticket------")
    print("---------------------------------------------")
    print("passenger Name    :", passenger_name)
    print("Reservation status  : confirmed")
    print("---------------------------------------------")
else:
    print("Reservation Failed")
