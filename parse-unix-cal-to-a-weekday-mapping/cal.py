def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
    keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    days = calendar_output.split("\n")[1]
    days_dict = {}
    for line in calendar_output.split("\n")[2:]:
        for day in line.split():
            if int(day) < 10:
                days_dict[int(day)] = days[line.find(day) - 1: line.find(day) + 1]
            else:
                days_dict[int(day)] = days[line.find(day): line.find(day) + 2]
    print(days_dict)
    return days_dict


if __name__ == "__main__":
    get_weekdays("""
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
""")
