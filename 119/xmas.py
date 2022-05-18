def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
    Each row has row_number*2-1 stars, simple example: for rows=3 the
    output would be like this (ignore docstring's indentation):
      *
     ***
    *****"""
    final_row_length = rows * 2 - 1
    tree = ""
    for row in range(1, rows + 1):
        row = "*" * (row * 2 - 1)
        tree += f"{row: ^{final_row_length}}\n"
    return tree.strip("\n")
