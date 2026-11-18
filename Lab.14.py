#Class
class Car:

#Method
    def show_details(self):
        print("Company :", self.company) 
        print("Color   :", self.color)
        print("Speed   :", self.speed)
#Objects
car1 = Car()

#Attributes
car1.company = "BMW"
car1.color = "Red"
car1.speed = 180

#Calling Method
print("Car 1 Details")
car1.show_details()

class Car:
    car1.show_details()
    car1 = Car()
    car1 = Car()
    car1.color = "Red"

class Car:
    speed = 120

    def show_speed(self):
        print("Speed :", self.speed)

car1 = Car()
car1.show_speed()
    
class Car:

    def start(self):
        print("Car Started")

car1 = Car()
car1.start()

class Car:

    def move(self):
        print("Car is moving")

class BMW(Car):
    pass

car1 = BMW()
car1.move()

class Car:
    
    def sound(self):
        print("Car makes sound")

class Bike:

    def sound(self):
        print("Bike makes sound")

c = Car()
b = Bike()

c.sound()
b.sound()

class Train:

   train_name = "Rajdhani Express"
   source_station = "Mumbai"
   destination_station = "Delhi"

train1 = Train()

print("Train Name :", train1.train_name)
print("Source Station :", train1.source_station)
print("Destination Station :", train1.destination_station)

class Passenger:

    passenger_name = "Rahul Sharma"
    seat_number = "B1-21"

    def display_ticket(self):

        print("Passenger Name :", self.passenger_name)
        print("Seat Number :", self.seat_number)
        print("Reservation Confirmed")

passenger1 = Passenger()

passenger1.display_ticket()

class Reservation:

   train_name = "Shatabdi Express"

   def reservation_status(self):
       print("Reservation Confirmed")


ticket1 = Reservation()
ticket2 = Reservation()

print(ticket1.train_name)
ticket1.reservation_status()

print(ticket2.train_name)
ticket2.reservation_status()


class RailwayReservation:

   train_name = "Rajdhani Express"
   passenger_name = "Priya Singh"
   seat_number = "A1-21"
   ticket_price = 2450

   def display_ticket(self):

       print("===================================")
       print(" Railway Reservation Ticket ")
       print("===================================")
       print("Passenger Name :", self.passenger_name)
       print("Train Name :", self.train_name)
       print("Seat Number :", self.seat_number)
       print("Ticket Price :", self.ticket_price)
       print("Reservation Status : Confirmed")

ticket = RailwayReservation()

ticket.display_ticket()
