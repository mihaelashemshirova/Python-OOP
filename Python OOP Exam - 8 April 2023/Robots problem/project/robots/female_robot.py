from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    KILOGRAMS_WEIGHT_INITIALLY = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.KILOGRAMS_WEIGHT_INITIALLY)

    def eating(self):
        self.weight += 1
