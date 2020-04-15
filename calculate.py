import numpy as np
from collections import namedtuple

Office = namedtuple('Office', 'start_col desks')

def office_has_path(office):
    return False

# Return the proportion of offices that had a path
#
# Why is it called percentage when it's a fraction?  Because that's the language the problem used.
def percentage_of_offices_with_a_path(office_generator, office_has_path_fn):
    return np.mean([1 if office_has_path_fn(office) else 0 for office in office_generator])
