STAR = "*"


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
    by row. So if width = 5 it should generate the following
    rows one by one:

    gen = gen_rhombus(5)
    for row in gen:
        print(row)

     output:
       *
      ***
     *****
      ***
       *
    """
    top_half = [num for num in range(1, width + 2, 2)]
    rows = top_half + top_half[-2::-1]
    for row in rows:
        yield f"{row*STAR: ^{width}}"


if __name__ == "__main__":
    print(gen_rhombus(width=7))
