from unittest import TestCase
import numpy as np
from unittest.mock import MagicMock

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

    def test_buid_random_office__has_correct_size(self):
        got = calculate.build_random_office(1)
        self.assertEqual((10, 10), got.desks.shape);

    def test_build_random_office__builds_empty_office_if_p_is_0(self):
        got = calculate.build_random_office(0)
        self.assertEqual(0, got.desks.sum())

    def test_build_random_office__builds_full_office_if_p_is_1(self):
        got = calculate.build_random_office(1)
        self.assertEqual(100, got.desks.sum())

    def test_build_random_office__has_some_offices_start_col_at_0(self):
        np.random.seed(1)

        starts = [calculate.build_random_office(0).start_col for i in range(1000)]

        self.assertEqual(0, min(starts))

    def test_build_random_office__has_some_offices_start_col_at_9(self):
        np.random.seed(1)

        starts = [calculate.build_random_office(0).start_col for i in range(1000)]

        self.assertEqual(9, max(starts))

    def test_office_generator__makes_n_items(self):
        offices = calculate.office_generator(13, 0);

        self.assertEqual(13, len(list(offices)))

    def test_office_generator__makes_offices(self):
        office_generator = calculate.office_generator(5, 0)

        office = next(office_generator)

        self.assertEqual('Office', type(office).__name__)

    def test_office_generator__passes_p_to_build_random_office(self):
        mock_build_random_office_fn = MagicMock()
        office_generator = calculate.office_generator(5, .34, build_random_office_fn=mock_build_random_office_fn)

        office = next(office_generator)

        mock_build_random_office_fn.assert_called_once_with(.34)

    def test_get_formatted_output(self):
        got = calculate.get_formatted_output(123, my_percentage_of_offices_with_a_path=lambda gen: 0.01)

        want = f"""Number of samples for each p: 123
1.0: 0.010
0.9: 0.010
0.8: 0.010
0.7: 0.010
0.6: 0.010
0.5: 0.010
0.4: 0.010
0.3: 0.010
0.2: 0.010
0.1: 0.010
0.0: 0.010
"""

        self.assertEqual(want, got)

    def test_get_results__first_row_is_correct(self):
        a_small_number_of_samples = 33
        results = list(calculate.get_results(a_small_number_of_samples))

        self.assertEqual((1, 0), results[0])

    def test_get_results__last_row_is_correct(self):
        a_small_number_of_samples = 33
        results = list(calculate.get_results(a_small_number_of_samples))

        self.assertEqual((0, 1), results[10])
