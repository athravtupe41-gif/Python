train = {"Train_Number" : 12951,
         "Train_Name" : "Mumbai Rajdhani Express",
         "Source" : "Mumbai",
         "Destination" : "Delhi",
         "Available Seats" : 120}

print("Train Information : ")
print(train)

print("\nTrain Number          : ", train["Train_Number"])
print("Train Name            : ", train["Train_Name"])
print("Source Station        : ", train["Source"])
print("Destination Station   : ", train["Destination"])
print("Available Seats       : ", train["Available Seats"])


print("Train Name            : ", train["Train_Name"])
print("Available Seats       : ", train["Available Seats"])

train['Available Seats'] = 95
print(train['Available Seats'])

train.update({"platform No. ": 4})
print(train)

train.pop("platform No. ")
print(train)

print("Updated Train Records : ")
print(train)

