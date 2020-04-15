from unittest import TestCase
import numpy as np
import calculate


class Test(TestCase):
    def test_percentage_of_offices_with_a_path__when_there_are_always_paths_should_return_1(self):
        office_generator = range(2)
        def office_has_path_fn(x): return True

        got = calculate.percentage_of_offices_with_a_path(office_generator, office_has_path_fn)

        self.assertEqual(1, got)

    def test_percentage_of_offices_with_a_path__when_there_are_no_paths_should_return_0(self):
        office_generator = range(2)
        def office_has_path_fn(x): return False

        got = calculate.percentage_of_offices_with_a_path(office_generator, office_has_path_fn)

        self.assertEqual(0, got)

    def test_office_has_path__should_find_a_path_in_an_empty_office(self):
        empty_desks = np.full([2, 2], calculate.DESK_EMPTY)
        office = calculate.Office(0, empty_desks)

        got = calculate.office_has_path(office)

        self.assertEqual(True, got)

    def test_office_has_path__should_not_find_a_path_in_a_full_office(self):
        full_desks = np.full([2, 2], calculate.DESK_FULL)
        office = calculate.Office(0, full_desks)

        got = calculate.office_has_path(office)

        self.assertEqual(False, got)


