
def swap_rows(M, row_index_1, row_index_2):
    # M is our matrix ,row index 1 is first row of our matrix that needs to be swapped

    """
        Swap two rows in a given matrix.
        M: Input matrix
        row_index_1: First row to be swapped
        row_index_2: Second row to be swapped
        """

    # and row index 2 is second row our matrix that needs to be swapped
    M = M.copy()
    # Copy matrix M so the changes do not affect the original matrix

    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    # Swap indexes
    return M