import requests
import re

puzzle_input_url = "https://adventofcode.com/2023/day/1/input"
test_input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
input_file = "C:/Users/nikol/Documents/GitHub/Advent-of-code-2023/scripts/day_01/input.txt"

def get_calibration_values(puzzle_input):
    for i in puzzle_input:
        i = i.strip()
        i = "".join(i.split())
        print(i)
        first_digit = re.search(r'\d+', i).group()
        last_digit = re.search(r'\d+', i[::-1]).group()[::-1]
        calibration_value = int(f"{first_digit}{last_digit}")
        yield calibration_value

def get_puzzle_input_request(url):
    puzzle_input = requests.get(url)
    return puzzle_input

def get_puzzle_input_file(file):
    with open(file) as input_file:
        data = input_file.readlines()
        return data


if __name__ == "__main__":
    puzzle_input = get_puzzle_input_file(input_file)
    cv = get_calibration_values(puzzle_input)
    # print(puzzle_input)
    for i in cv:
        print(i)
    print(sum(cv))