from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_add_toy_if_shelf_not_in_toy_keys(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('K', 'Kitty')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_is_already_in_shelf(self):
        self.toy.add_toy('A', 'Abc')
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'Abc')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_already_taken(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'Abc')
            self.toy.add_toy('A', 'Art')
        self.assertEqual('Shelf is already taken!', str(ex.exception))

    def test_add_toy_placed_successfully(self):
        self.assertEqual('Toy:Abc placed successfully!', self.toy.add_toy('A', 'Abc'))

    def test_remove_toy_raise_ex_shelf_not_in_keys(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('K', 'Kitty')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('A', 'Ani')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correct_data(self):
        self.toy.add_toy('A', 'Abc')
        self.assertEqual('Remove toy:Abc successfully!', self.toy.remove_toy('A', 'Abc'))
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)


if __name__ == '__main__':
    main()
