from data.vehicle import Vehicle

class RentalSystem:
    def __init__(self):
        self.vehicles = {}
        self.customers = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def search_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles.values():
            if v.is_available:
                v.display_info()

    def show_all_rented_vehicles(self):
        print("\nRented Vehicles:")
        for v in self.vehicles.values():
            if not v.is_available:
                v.display_info()

    def rent_vehicle(self, customer_id, vehicle_id):
        customer = self.customers.get(customer_id)
        vehicle = self.vehicles.get(vehicle_id)
        if not customer or not vehicle:
            print("Invalid Customer ID or Vehicle ID!")
            return
        if not vehicle.is_available:
            print("Vehicle already rented!")
            return
        customer.rent(vehicle)
        print(f"{customer.name} has rented {vehicle.brand} {vehicle.model}.")

    def return_vehicle(self, customer_id, vehicle_id):
        customer = self.customers.get(customer_id)
        if not customer:
            print("Invalid Customer ID!")
            return
        customer.return_vehicle(vehicle_id)
        print("Vehicle returned successfully!")

    @staticmethod
    def get_total_rented():
        return Vehicle.total_rented_count
    