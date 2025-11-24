from data.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, seats, fuel_type, is_available=True):
        super().__init__(vehicle_id, brand, model, year, rental_rate_per_day, is_available)
        self.seats = seats
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rate per Day: ₹{self.rental_rate_per_day}")
        print(f"Seats: {self.seats}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
        print("-" * 30)