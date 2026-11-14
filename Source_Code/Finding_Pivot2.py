def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    # Find the index of the first non-zero value in the specified row of the given matrix

    # Parameters the input matrix to search for non-zero values
    # the index of the row to search.
    # the augmented (Pass this True if you are dealing with an augmented matrix)

    # Create a copy to avoid modifying the original matrix
    M = M.copy()
    if augmented == True:
        # Isolating the coefficient matrix
        M = M[:, :-1]

    # Get the row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns -1
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1