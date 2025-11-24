class Vehicle:
    total_rented_count = 0  

    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, is_available=True):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_rate_per_day = rental_rate_per_day
        self.is_available = is_available

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rate per Day: ₹{self.rental_rate_per_day}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
            Vehicle.total_rented_count += 1
        else:
            print(f"{self.brand} {self.model} is already rented!")

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return self.rental_rate_per_day * days

    @classmethod
    def get_total_rented(cls):
        return cls.total_rented_count