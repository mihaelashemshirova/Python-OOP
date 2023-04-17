from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.avatar = Movie('Avatar', 2022, 7.8)
        self.joker = Movie('Joker', 2019, 8.4)

    def test_correct_initializing(self):
        self.assertEqual('Avatar', self.avatar.name)
        self.assertEqual(2022, self.avatar.year)
        self.assertEqual(7.8, self.avatar.rating)
        self.assertEqual([], self.avatar.actors)

    def test_name_props_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.avatar.name = ''
        self.assertEqual('Name cannot be an empty string!', str(ve.exception))

    def test_year_props_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.avatar.year = 1880
        self.assertEqual('Year is not valid!', str(ve.exception))

    def test_add_actor_if_name_not_in_list(self):
        self.avatar.add_actor('Asta')
        self.assertEqual(['Asta'], self.avatar.actors)

    def test_add_actor_if_name_in_list(self):
        self.avatar.add_actor('Asta')
        self.assertEqual('Asta is already added in the list of actors!', self.avatar.add_actor('Asta'))

    def test_gt_with_avatar(self):
        self.assertEqual('"Joker" is better than "Avatar"', self.avatar.__gt__(self.joker))

    def test_gt_with_joker(self):
        self.avatar.rating = 9.8
        self.assertEqual('"Avatar" is better than "Joker"', self.avatar.__gt__(self.joker))

    def test_repr_avatar(self):
        self.avatar.add_actor('Asta')
        self.avatar.add_actor('Rom')
        self.assertEqual('Name: Avatar\n'
                         'Year of Release: 2022\n'
                         'Rating: 7.80\n'
                         'Cast: Asta, Rom', self.avatar.__repr__())


if __name__ == '__main__':
    main()
