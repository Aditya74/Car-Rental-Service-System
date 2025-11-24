class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.__email = email
        self.rented_vehicles = []

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
            print("Email updated successfully.")
        else:
            print("Invalid email format!")

    def rent(self, vehicle):
        if vehicle.is_available:
            vehicle.rent_vehicle()
            self.rented_vehicles.append(vehicle)
            print(f"{self.name} has rented {vehicle.brand} {vehicle.model}.")
        else:
            print(f"{vehicle.brand} {vehicle.model} is not available.")

    def return_vehicle(self, vehicle_id):
        for v in self.rented_vehicles:
            if v.vehicle_id == vehicle_id:
                v.return_vehicle()
                self.rented_vehicles.remove(v)
                print(f"{self.name} has returned {v.brand} {v.model}.")
                return
        print(f"No rented vehicle found with ID {vehicle_id}.")

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print("Rented Vehicles:")
        if self.rented_vehicles:
            for v in self.rented_vehicles:
                print(f" - {v.brand} {v.model} (ID: {v.vehicle_id})")
        else:
            print(" - None")
        print("-" * 40)
