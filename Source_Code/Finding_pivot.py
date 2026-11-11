import numpy as np

import pandas as pd

def get_index_first_non_zero_value(M, column, starting_row):
    # So this function is for changing our rows of our matrices but when the
    # pivot is zero it looks for first nonzero value to change

    # Get the column array starting from the specified row

    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.

        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        # because our pivot can be 0,000000000005 we count it as zero :)

        if not np.isclose(val, 0, atol=1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row

            return index

    # If no non-zero value is found below it, return -1
    return -1