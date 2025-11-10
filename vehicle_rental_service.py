from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, base_rate):
        self.__vehicle_id = vehicle_id       # encapsulation (private variable)
        self.__model = model
        self.__base_rate = base_rate
        self.__is_rented = False

    # Getters and setters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def is_rented(self):
        return self.__is_rented

    def rent(self):
        if self.__is_rented:
            raise Exception(f"{self.__model} is already rented!")
        self.__is_rented = True

    def return_vehicle(self):
        if not self.__is_rented:
            raise Exception(f"{self.__model} is not rented!")
        self.__is_rented = False

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    def __str__(self):
        status = "Rented" if self.__is_rented else "Available"
        return f"[{self.__class__.__name__}] ID: {self.__vehicle_id}, Model: {self.__model}, Rate: {self.__base_rate}/day, Status: {status}"



class Car(Vehicle):
    def calculate_rental_cost(self, days):
        return self._Vehicle__base_rate * days  # direct base rate usage


class Bike(Vehicle):
    def calculate_rental_cost(self, days):
        return (self._Vehicle__base_rate * 0.8) * days


class Truck(Vehicle):
    def calculate_rental_cost(self, days):
        return (self._Vehicle__base_rate * 1.5) * days



class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_vehicles = []  # list of Vehicle objects

    def rent_vehicle(self, vehicle, days):
        try:
            vehicle.rent()
            cost = vehicle.calculate_rental_cost(days)
            self.rented_vehicles.append((vehicle, days, cost))
            print(f"{self.name} rented {vehicle.get_model()} for {days} days. Total cost: ${cost}")
        except Exception as e:
            print("Error:", e)

    def return_vehicle(self, vehicle):
        try:
            vehicle.return_vehicle()
            self.rented_vehicles = [rv for rv in self.rented_vehicles if rv[0] != vehicle]
            print(f"{self.name} returned {vehicle.get_model()}.")
        except Exception as e:
            print("Error:", e)

    def show_rented_vehicles(self):
        if not self.rented_vehicles:
            print(f"{self.name} has no rented vehicles.")
        else:
            print(f"{self.name}'s rented vehicles:")
            for v, days, cost in self.rented_vehicles:
                print(f"  - {v.get_model()} for {days} days, cost ₹{cost}")


# Rental System
class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_customer(self, customer):
        self.customers.append(customer)

    
    def search_vehicle(self, key=None):
        results = []
        for v in self.vehicles:
            if key is None or str(key).lower() in v.get_model().lower() or str(key) == str(v.get_vehicle_id()):
                results.append(v)
        return results

    def show_all_vehicles(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles:
            print(v)
        print()



def main():
    # Create Rental System
    system = RentalSystem()

    # Add Vehicles
    system.add_vehicle(Car(101, "Honda City", 2000))
    system.add_vehicle(Bike(202, "Yamaha R15", 800))
    system.add_vehicle(Truck(303, "Tata Heavy", 5000))

    # Add Customer
    c1 = Customer("Nayeem")
    system.add_customer(c1)

    # Show all vehicles
    system.show_all_vehicles()

    # Customer rents a car
    c1.rent_vehicle(system.vehicles[0], 3)

    # Try renting same car again
    c1.rent_vehicle(system.vehicles[0], 2)

    # Return the car
    c1.return_vehicle(system.vehicles[0])

    # Show customer's rented vehicles
    c1.show_rented_vehicles()

    # Search for vehicles
    print("\nSearch result for 'Yamaha':")
    for v in system.search_vehicle("Yamaha"):
        print(v)


if __name__ == "__main__":
    main()
