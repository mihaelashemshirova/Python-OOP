from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        result = []

        if self.robots:
            for r in self.robots:
                result.append(r.name)
        else:
            result.append('none')

        return f'{self.name} Secondary Service:\n' \
               f'Robots: {" ".join(result)}'
