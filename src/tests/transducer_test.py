import unittest
from src.structures.transducer import replace_name


class MyTestCase(unittest.TestCase):

    def test_short_name(self):
        name_1 = 'Pepe'
        name_2 = 'William'
        name_3 = 'Kenshi'
        name_4 = 'Takahashi'

        new_name_1 = replace_name(name_1, name_2)
        new_name_2 = replace_name(name_3, name_4)

        self.assertEqual(new_name_1, 'Pepe')
        self.assertEqual(new_name_2, 'Kenshi')

    def test_long_name(self):
        name_1 = 'Elizabeth'
        name_2 = 'Dina'
        name_3 = 'Jiraija'
        name_4 = 'Sasuke'

        new_name_1 = replace_name(name_1, name_2)
        new_name_2 = replace_name(name_3, name_4)

        self.assertEqual(new_name_1, 'Elizabeth')
        self.assertEqual(new_name_2, 'Jiraija')


if __name__ == '__main__':
    unittest.main()
