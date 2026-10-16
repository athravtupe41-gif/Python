total_seats = 5

while total_seats > 0:
    print("Seat booked succesfully")
    print("Remaining seats are :", total_seats - 1)

    total_seats -= 1
print("All seats are filled")


print("Available seat numbers : ")
for seat in range(1,11):
    print("seat number : ", seat)


total_seats = 5

for booking in range(1, 10):

    if booking > total_seats:
        print("No seats available")
        break

    if booking == 3:
        print("Checking special reservation")
        continue

    pass

    print("Seat", booking, "booked succesfully")
    