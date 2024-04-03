import csv


def check_file(argv: list[str]) -> int:
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
    return 0
