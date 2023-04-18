from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    TYPE_OF_VEHICLES = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan,
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = [u for u in self.users if u.driving_license_number == driving_license_number]

        if user:
            return f"{driving_license_number} has already been registered to our platform."
        else:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.TYPE_OF_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.TYPE_OF_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        trip = [t for t in self.routes
                if t.start_point == start_point and t.end_point == end_point and t.length == length]

        if trip:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        trip = [t for t in self.routes if
                t.start_point == start_point and t.end_point == end_point and t.length < length]

        if trip:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        trip = [t for t in self.routes if
                t.start_point == start_point and t.end_point == end_point and t.length > length]

        if trip:
            trip[0].is_locked = True

        new_trip = Route(start_point, end_point, length, route_id)
        self.routes.append(new_trip)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        trip = [t for t in self.routes if route_id == t.route_id]

        if user[0].is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle[0].is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if trip[0].is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle[0].drive(trip[0].length)

        if is_accident_happened:
            vehicle[0].is_damaged = True
            user[0].decrease_rating()
        else:
            user[0].increase_rating()

        return vehicle[0].__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]
        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***", ]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        result.append(('\n'.join(str(user) for user in sorted_users)))
        return '\n'.join(result)


app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
