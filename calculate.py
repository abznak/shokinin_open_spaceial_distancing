import numpy as np
from collections import namedtuple
from skimage.morphology import flood_fill

SAMPLES = 10000

DESKROW_EXIT = 0

DESK_EMPTY = 0
DESK_FULL = 1
DESK_PATH = 2

OFFICE_SIDE_LENGTH = 10
OFFICE_DIMENSIONS = [OFFICE_SIDE_LENGTH, OFFICE_SIDE_LENGTH]

Office = namedtuple('Office', 'start_col desks')

# p is probably a desk is occupied
def build_random_office(p):
    desks_rolls = np.random.rand(*OFFICE_DIMENSIONS)
    convert_rolls_to_desk_state = np.vectorize(lambda roll: DESK_FULL if roll <= p else DESK_EMPTY)
    desks = convert_rolls_to_desk_state(desks_rolls)
    start_col = np.random.randint(0, OFFICE_SIDE_LENGTH)
    return Office(start_col, desks)

def office_generator(n, p, build_random_office_fn = build_random_office):
    return (build_random_office_fn(p) for x in range(n))

def office_has_path(office):
    desks = np.copy(office.desks)
    start_col = office.start_col
    start_row = desks.shape[0] - 1

    # When you stand up, your desk becomes empty
    desks[start_row, start_col] = DESK_EMPTY

    # draw a path everywhere you can reach
    desks_with_path = flood_fill(desks, (start_row, start_col), DESK_PATH)

    # look for a path to any desk in the exit row
    path_found = any(DESK_PATH == desk for desk in desks_with_path[DESKROW_EXIT])

    return path_found


# Return the proportion of offices that had a path
#
# Why is it called percentage when it's a fraction?  Because that's the language the problem used.
def percentage_of_offices_with_a_path(my_office_generator, office_has_path_fn = office_has_path):
    return np.mean([1 if office_has_path_fn(office) else 0 for office in my_office_generator])

def get_results(my_percentage_of_offices_with_a_path = percentage_of_offices_with_a_path):
    empty_ps =  np.linspace(1, 0, 11)

    def calculate_percentage(empty_p):
        generator = office_generator(SAMPLES, empty_p)
        return my_percentage_of_offices_with_a_path(generator)

    results = ((empty_p, calculate_percentage(empty_p)) for empty_p in empty_ps)
    return results

def format_output(results):
    lines = [f'{res[0]:.1f}: {res[1]:.3f}' for res in results]

    return f"Number of samples for each p: {SAMPLES}\n" + ("\n".join(lines)) + "\n"


def get_formatted_output(my_percentage_of_offices_with_a_path = percentage_of_offices_with_a_path):
    results = get_results(my_percentage_of_offices_with_a_path)
    return format_output(results)

def main():
    print(get_formatted_output())

if __name__ == "__main__":
    main()