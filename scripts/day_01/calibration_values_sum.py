import requests
import re

puzzle_input = "https://adventofcode.com/2023/day/1/input"

test_input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]


for i in test_input:
    first_digit = re.search(r'\d+', i).group()
    print(i)
    print(first_digit)
