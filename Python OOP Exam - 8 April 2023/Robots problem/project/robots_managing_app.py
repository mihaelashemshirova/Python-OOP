from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[object] = []
        self.services: List[object] = []

    def add_service(self, service_type: str, name: str):
        if service_type == 'MainService':
            new_service = MainService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        elif service_type == 'SecondaryService':
            new_service = SecondaryService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        else:
            raise Exception('Invalid service type!')

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == 'FemaleRobot':
            new_service = FemaleRobot(name, kind, price)
            self.robots.append(new_service)
            return f"{robot_type} is successfully added."
        elif robot_type == 'MaleRobot':
            new_robot = MaleRobot(name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."
        else:
            raise Exception('Invalid robot type!')

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name]
        service = [s for s in self.services if s.name == service_name]
        if robot[0].__class__.__name__ == 'FemaleRobot' and service[0].__class__.__name__ == 'SecondaryService':
            service = service[0]
        elif robot[0].__class__.__name__ == 'MaleRobot' and service[0].__class__.__name__ == 'MainService':
            service = service[0]
        else:
            return 'Unsuitable service.'
        if len(service.robots) >= service.capacity:
            raise Exception('Not enough capacity for this robot!')
        self.robots.remove(robot[0])
        service.robots.append(robot[0])
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception('No such robot in this service!')

        self.robots.append(robot)
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        fed = 0
        for r in service.robots:
            r.eating()
            fed += 1
        return f"Robots fed: {fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name]
        result = 0
        for r in service[0].robots:
            result += r.price
        return f"The value of service {service_name} is {result:.2f}."

    def __str__(self):
        result = []
        for s in self.services:
            result.append(s.details())
        return '\n'.join(result)
