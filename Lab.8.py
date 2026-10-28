passengers = ["Rahul Sharma", "Priya Patel", "Amit Varma"]

print("Passenger Reservation List: ")
print(passengers)

print("\nFirst Passengers: ", passengers[0])

print("Second Passengers: ", passengers[1])

print("Third Passengers: ", passengers[2])

passengers.append("Sneha Joshi")
print(passengers)

passengers.remove("Amit Varma")
print(passengers)

passengers.insert(1, "Rohan Mehta")
print(passengers)

removed_passenger = passengers.pop(2)
print(passengers)

print("Updated Reservation List: ")
print(passengers)


