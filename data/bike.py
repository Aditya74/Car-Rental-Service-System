from data.vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, cc, helmet_required, is_available=True):
        super().__init__(vehicle_id, brand, model, year, rental_rate_per_day, is_available)
        self.cc = cc
        self.helmet_required = helmet_required

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rate per Day: ₹{self.rental_rate_per_day}")
        print(f"Engine Capacity: {self.cc}cc")
        print(f"Helmet Required: {'Yes' if self.helmet_required else 'No'}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
        print("-" * 30)