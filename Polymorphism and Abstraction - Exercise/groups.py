from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List):
        self.name = name
        self.people: List[Person] = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {str(self.people[item])}"
