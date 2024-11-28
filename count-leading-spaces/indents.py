def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    leading_spaces = 0
    for c in text:
        if c == " ":
            leading_spaces += 1
        else:
            break
    return leading_spaces
