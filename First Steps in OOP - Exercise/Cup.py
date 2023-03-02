class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def status(self):
        free_space = self.size - self.quantity
        return abs(free_space)

    def fill(self, quantity: int):
        if self.size - self.quantity >= quantity:
            self.quantity += quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
