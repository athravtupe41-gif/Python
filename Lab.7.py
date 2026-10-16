passenger_name = " Rahul Sharma "
train_name = "rajdhani express"

print("Original Passenger Name:", passenger_name)

print("Uppercase Name:", passenger_name.upper())

print("Formatted Name:", passenger_name.strip().title())

print("Train Name:", train_name.upper())

updated_train = train_name.replace("rajdhani", "Vande Bharat")

print("updated Train Name:", updated_train)


passenger_name = "Priya Patel"
train_number = 12951
seat_number = "B2-45"
fare = 1250

print(f"Passenger Name : {passenger_name}")
print(f"Train Number   : {train_number}")
print(f"Seat Number    : {seat_number}")
print(f"Ticket Fare    :  ₹{fare}")

ticket_id = "WRB24567"

zone = ticket_id[0:2]

coach = ticket_id[2:4]

ticket_number = ticket_id[4:]

print("Ticket ID:", ticket_id)

print("Railway Zone:", zone)

print("Coach Number:", coach)

print("Ticket NUmber:", ticket_number)


