from unittest import TestCase, main
from mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Cat', 'Cats', 'Meow')

    def test_correct_initializing(self):
        self.assertEqual('Cat', self.mammal.name)
        self.assertEqual('Cats', self.mammal.type)
        self.assertEqual('Meow', self.mammal.sound)

    def test_if_sound_returns_correct_message(self):
        self.assertEqual('Cat makes Meow', self.mammal.make_sound())

    def test_if_get_kingdom_returns_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_if_info_returns_correct_message(self):
        self.assertEqual('Cat is of type Cats', self.mammal.info())


if __name__ == '__main__':
    main()
