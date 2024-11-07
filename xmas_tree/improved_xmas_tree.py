STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows: int = 10) -> None:
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
    for given rows of leafs (default 10).
    For more information see the test and the bite description
    """
    max_width = rows * 2 - 1
    tree = f"{STAR:^{max_width}}\n"
    for row in range(rows):
        tree += f"{LEAF * ((row + 1) * 2 - 1):^{max_width}}\n"
    if rows % 2 == 0:
        tree += f"{TRUNK * (rows + 1):^{max_width}}\n"
        tree += f"{TRUNK * (rows + 1):^{max_width}}\n"
    else:
        tree += f"{TRUNK * (rows):^{max_width}}\n"
        tree += f"{TRUNK * (rows):^{max_width}}\n"
    return tree
