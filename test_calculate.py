from unittest import TestCase
import calculate


class Test(TestCase):
    def test_percentage_of_offices_with_a_path__when_there_are_always_paths_should_return_1(self):
        office_generator = range(2)
        office_has_path_fn = lambda x: True
        got = calculate.percentage_of_offices_with_a_path(office_generator, office_has_path_fn)
        self.assertEqual(1, got)

    def test_percentage_of_offices_with_a_path__when_there_are_no_paths_should_return_0(self):
        office_generator = range(2)
        office_has_path_fn = lambda x: False
        got = calculate.percentage_of_offices_with_a_path(office_generator, office_has_path_fn)
        self.assertEqual(0, got)
