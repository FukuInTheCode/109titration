import csv


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def check_file(argv: list[str]) -> int:
    count_pair = 0
    with open(argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            line = row[0]
            semicolon_count = line.count(";")
            if semicolon_count != 1:
                exit(84)
            semicolon_index = line.find(";")
            if semicolon_index == 0 or semicolon_index == len(line) - 1:
                exit(84)
            before_semicolon = line[:semicolon_index]
            after_semicolon = line[semicolon_index + 1:]
            if not is_number(before_semicolon) or not is_number(after_semicolon):
                exit(84)
            if float(before_semicolon) < 0:
                exit(84)
            if not (0 <= float(after_semicolon) <= 15):
                exit(84)
            count_pair += 1
    if count_pair < 5:
        exit(84)
    return 0
