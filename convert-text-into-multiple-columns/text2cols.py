import textwrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""
    columns = []
    for paragraph in text.split("\n\n"):
        columns.append(textwrap.wrap(paragraph, width=COL_WIDTH))

    return "\n".join(["".rjust(COL_WIDTH).join(column) for column in zip(*columns)])


if __name__ == "__main__":
    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""
    print(text_to_columns(text))
