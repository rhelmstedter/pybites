# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


def _make_translation_table(str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a table string that defines valid (and complementary) bases
    Returns a dictionary of ord(char) to map characters
    """
    translation_table = {}
    table_elements = str_table.split("\n")[2:-1]
    for line in table_elements:
        line_elements = line.split("\t")
        # This ensures that the solution works with a table with
        # a variable number of columns
        from_base, to_base = (
            line_elements[0].strip(),
            line_elements[-1].strip(),
        )
        translation_table[ord(from_base)] = ord(to_base)
    return translation_table


# Recommended helper function
def _clean_sequence(sequence, translation_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    return "".join(
        [
            character
            for character in sequence.upper()
            if ord(character) in translation_table.keys()
        ]
    )


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    translation_table = _make_translation_table(str_table)
    clean_DNA = _clean_sequence(sequence, translation_table)
    return clean_DNA[::-1]


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    translation_table = _make_translation_table(str_table)
    clean_DNA = _clean_sequence(sequence, translation_table)
    return clean_DNA.translate(translation_table)


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    return complement(sequence, str_table)[::-1]


if __name__ == "__main__":
    print(_make_translation_table())
