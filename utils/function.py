import re
from data.car import Car
from data.bike import Bike
from data.customer import Customer
from data.vehicle import Vehicle
from utils.display import display  

def add_vehicle(system):
    display("ADD VEHICLE")
    print("1. Car\n2. Bike")
    vtype = input("Enter vehicle type: ").strip()
    vid = input("Enter Vehicle ID: ").strip()
    brand = input("Enter Brand: ").strip()
    model = input("Enter Model: ").strip()
    year = input("Enter Year: ").strip()
    rate = float(input("Enter Rental Rate per Day: ").strip())

    if vtype == '1':  
        seats = input("Enter Number of Seats: ").strip()
        fuel = input("Enter Fuel Type: ").strip()
        car = Car(vid, brand, model, year, rate, seats, fuel)
        system.add_vehicle(car)
        print(f"Car '{brand} {model}' added successfully!")

    elif vtype == '2': 
        cc = input("Enter Engine Capacity (cc): ").strip()
        helmet = input("Is helmet required (yes/no): ").strip().lower() == 'yes'
        bike = Bike(vid, brand, model, year, rate, cc, helmet)
        system.add_vehicle(bike)
        print(f"Bike '{brand} {model}' added successfully!")

    else:
        print("Invalid vehicle type!")


def add_customer(system):
    display("ADD CUSTOMER")
    cid = input("Enter Customer ID: ").strip()
    name = input("Enter Name: ").strip()
    
   
    while True:
        email = input("Enter Email: ").strip()
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            break
        else:
            print("Invalid email format! Please enter a valid email.")

    customer = Customer(cid, name, email)
    system.add_customer(customer)
    print(f"Customer '{name}' added successfully!")


def rent_vehicle(system):
    display("RENT VEHICLE")
    cid = input("Enter Customer ID: ").strip()
    vid = input("Enter Vehicle ID to Rent: ").strip()
    system.rent_vehicle(cid, vid)

def return_vehicle(system):
    display("RETURN VEHICLE")
    cid = input("Enter Customer ID: ").strip()
    vid = input("Enter Vehicle ID to Return: ").strip()
    system.return_vehicle(cid, vid)

def calculate_cost(system):
    display("CALCULATE RENTAL COST")
    vid = input("Enter Vehicle ID: ").strip()
    days = int(input("Enter Number of Days: ").strip())
    vehicle = system.vehicles.get(vid)
    if vehicle:
        print(f"Total rental cost: ₹{vehicle.calculate_rental_cost(days)}")
    else:
        print("Vehicle not found!")


def show_available_vehicles(system):
    display("AVAILABLE VEHICLES")
    system.search_available_vehicles()

def show_all_rented_vehicles(system):
    display("RENTED VEHICLES")
    system.show_all_rented_vehicles()

def show_total_rentals(system):
    display("TOTAL RENTALS")
    print(f"Total Rentals: {system.get_total_rented()}")

