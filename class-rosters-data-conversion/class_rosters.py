import csv


def class_rosters(input_file):
    """Read the input_file and modify the data
    according to the Bite description.
    Return a list holding one item per student
    per class, correctly formatted."""
    final = []
    with open(input_file) as f:
        for row in csv.reader(f):
            id, _, *classes = row
            for class_ in classes:
                if class_:
                    class_name = class_.split(" - ")[0]
                    final.append(f"{class_name},2020,{id}")
    return final
