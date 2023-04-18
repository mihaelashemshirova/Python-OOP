from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team('Top')
        self.site = Team('Hop')

    def test_correct_initialization(self):
        self.assertEqual('Top', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = '123'
        self.assertEqual('Team Name can contain only letters!', str(ve.exception))

    def test_add_member_if_name_not_in_dict(self):
        self.assertEqual("Successfully added: Ani, Mimi", self.team.add_member(Ani=20, Mimi=17))
        self.assertEqual({'Ani': 20, 'Mimi': 17}, self.team.members)

    def test_add_member_if_name_in_dict(self):
        self.team.add_member(Ani=20)
        self.assertEqual('Successfully added: Magi', self.team.add_member(Ani=20, Magi=10))
        self.assertEqual({'Ani': 20, 'Magi': 10}, self.team.members)

    def test_remove_member_if_name_in_members(self):
        self.team.add_member(Ani=20)
        self.assertEqual('Member Ani removed', self.team.remove_member('Ani'))
        self.assertEqual({}, self.team.members)

    def test_remove_member_if_name_not_in_members(self):
        self.assertEqual('Member with name Ani does not exist', self.team.remove_member('Ani'))

    def test_gt_members(self):
        self.team.add_member(Ani=20, Mimi=17)
        self.site.add_member(Rumi=29, Zlati=34, Megan=23)
        self.assertEqual(True, self.site.__gt__(self.team))

    def test_gt_members_false(self):
        self.team.add_member(Ani=20, Mimi=17)
        self.site.add_member(Rumi=29, Zlati=34, Megan=23)
        self.assertEqual(False, self.team.__gt__(self.site))

    def test_len_members(self):
        self.site.add_member(Rumi=29, Zlati=34, Megan=23)
        self.assertEqual(3, self.site.__len__())

    def test_add_site_and_team(self):
        self.team.add_member(Ani=20, Mimi=17)
        self.site.add_member(Rumi=29, Zlati=34, Megan=23)
        new_team = self.team.__add__(self.site)
        self.assertEqual('TopHop', new_team.name)
        self.assertEqual({'Ani': 20, 'Mimi': 17, 'Rumi': 29, 'Zlati': 34, 'Megan': 23}, new_team.members)

    def test_str_(self):
        self.team.add_member(Ani=20, Mimi=17)
        self.assertEqual('Team name: Top\n'
                         'Member: Ani - 20-years old\n'
                         'Member: Mimi - 17-years old', self.team.__str__())


if __name__ == '__main__':
    main()
