

engine_schema = """
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

symbol_positions = []
digits = []
numbers = []
digit_positions = []
number_positions = []
rows = engine_schema.split("\n")

#symbol positions
for row_count, row in enumerate(rows):
    for col_count, col in enumerate(row):
        # col_position = col, row
        if col in "$*#+":
            symbol_postition = col_count, row_count
            symbol_positions.append(symbol_postition)
        elif col.isdigit():
            digit_position = col_count, row_count
            digit_positions.append(digit_position)
            digits.append(col)
        else: # if position is . 
            digit_position = None
            digits = "".join(digits)
            numbers.append(digits)
            number_positions.append(digit_positions)
            digit_positions = []
            digits = []

# TODO: clean lists from empty strings/lists numbers/number positions
# TODO: check positions of numbers and symbols


print(numbers)
print(symbol_positions)
print(digit_positions)
print(number_positions)