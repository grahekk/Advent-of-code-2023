import re

e_schema = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
engine_schema = "input.txt"

def get_puzzle_input_file(file):
    with open(file) as input_file:
        data = input_file.read().splitlines()
        return data


symbol_positions = []
digits = []
numbers = []
digit_positions = []
number_positions = []
rows = engine_schema.split("\n")

rows = get_puzzle_input_file(engine_schema)


#symbol positions
for row_count, row in enumerate(rows):
    for col_count, col in enumerate(row):
        # col_position = col, row
        if not col.isalnum() and col not in"\.":
            digit_position = None
            digits = []
            symbol_postition = col_count, row_count
            symbol_positions.append(symbol_postition)
        # elif col == r"\*":
        #     print(f"found an *! in {col}")
        elif col.isdigit():
            digit_position = col_count, row_count
            digit_positions.append(digit_position)
            digits.append(col)
        elif col in "\.": # if position is . 
            digit_position = None
            digits = "".join(digits)
            numbers.append(digits)
            number_positions.append(digit_positions)
            digit_positions = []
            digits = []
        else:
            print(f"found an *! in {col}")


numbers = [i for i in numbers if i]
number_positions = [i for i in number_positions if i]


adjacent_numbers = []
adjacent_positions = []
adjacent = []

for positions_list in number_positions:
    #list
    for position in positions_list:
        for symbol in symbol_positions:
            if (symbol[0] == position[0] and (symbol[1]+1==position[1] or symbol[1]-1==position[1])) \
            or (symbol[0]-1 == position[0] and (symbol[1]+1==position[1] or symbol[1] == position[1] or symbol[1]-1 == position[1])) \
            or (symbol[0]+1 == position[0] and (symbol[1]+1==position[1] or symbol[1] == position[1] or symbol[1]-1 == position[1])):
                adjacent_positions.append(True)
            else:
                adjacent_positions.append(False)
        
        adjacent_numbers.append(sum(adjacent_positions))
        adjacent_positions = []
    adjacent.append(adjacent_numbers)
    adjacent_numbers = []

bool_adj = []
for adj in adjacent:        
    bool_list = list(map(bool,adj))
    if any(bool_list):
        bool_adj.append(True)
    else:
        bool_adj.append(False)


# print(numbers)
filtered_list = [i for (i, v) in zip(numbers, bool_adj) if v]
filter_number_list = [int(i) for i in filtered_list]
# print(filter_number_list)
print(sum(filter_number_list))
