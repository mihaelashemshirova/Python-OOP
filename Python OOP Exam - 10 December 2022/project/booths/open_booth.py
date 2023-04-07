from project.booths.booth import Booth


class OpenBooth(Booth):

    PRICE_FOR_RESERVE = 2.50

    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.PRICE_FOR_RESERVE * number_of_people
        self.is_reserved = True
