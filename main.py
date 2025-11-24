from utils.function import add_vehicle, add_customer, rent_vehicle, return_vehicle, calculate_cost, show_available_vehicles, show_all_rented_vehicles, show_total_rentals
from data.rentalsystem import RentalSystem
def main():
    system = RentalSystem()
    while True:
        print("\n1. Add Vehicle\n2. Add Customer\n3. Show Available Vehicles\n4. Rent a Vehicle")
        print("5. Return a Vehicle\n6. Show All Rented Vehicles\n7. Show Total Rentals\n8. Calculate Rental Cost\n9. Exit")
        
        choice = input("Enter your choice (1-9): ").strip()
        if choice == '1':
            add_vehicle(system)
        elif choice == '2':
            add_customer(system)
        elif choice == '3':
            show_available_vehicles(system)
        elif choice == '4':
            rent_vehicle(system)
        elif choice == '5':
            return_vehicle(system)
        elif choice == '6':
            show_all_rented_vehicles(system)
        elif choice == '7':
            show_total_rentals(system)
        elif choice == '8':
            calculate_cost(system)
        elif choice == '9':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
