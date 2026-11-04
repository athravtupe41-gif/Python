seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_seats = [seat for seat in seats if seat % 2 == 0]

print("Available Seats : ")
print(seats)

print("\nEven Numbered Seats : ")
print(even_seats)

trains = {"Rajdhani" : 120, "Duronto" : 95, "Garib Rath" : 40, "Shatabdi" : 60}

available_trains = {train: seats for train, seats in trains.items() if seats > 50}

print("Trains With More Than 50 Seats : ")
print(available_trains)

