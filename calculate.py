import numpy as np
from collections import namedtuple
from skimage.morphology import flood_fill

DESKROW_EXIT = 0

DESK_EMPTY = 0
DESK_FULL = 1
DESK_PATH = 2

OFFICE_SIDE_LENGTH = 10

Office = namedtuple('Office', 'start_col desks')

# p is probably a desk is occupied
def build_random_office(p):
    return Office(1, np.ones([OFFICE_SIDE_LENGTH, OFFICE_SIDE_LENGTH]))



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
def percentage_of_offices_with_a_path(office_generator, office_has_path_fn):
    return np.mean([1 if office_has_path_fn(office) else 0 for office in office_generator])
