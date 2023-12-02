import requests
import re

puzzle_input_url = "https://adventofcode.com/2023/day/1/input"
test_input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
input_file = "input.txt"
num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}


test_input = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]


def get_calibration_values(puzzle_input):
    for i in puzzle_input:
        first_digit = re.search(r'\d', i).group()
        last_digit = re.search(r'\d', i[::-1]).group()[::-1]
        calibration_value = int(f"{first_digit}{last_digit}")
        yield calibration_value

def get_puzzle_input_request(url):
    puzzle_input = requests.get(url)
    return puzzle_input

def get_puzzle_input_file(file):
    with open(file) as input_file:
        data = input_file.read().splitlines()
        return data

def replace_string_numbers(puzzle_input):
    for i in puzzle_input:
        for key, value in num_dict.items():
            if key in i:
                i = i.replace(key, key.replace(key[1], str(value)))
        yield i

if __name__ == "__main__":
    puzzle_input = get_puzzle_input_file(input_file)
    puzzle_input = replace_string_numbers(puzzle_input)
    cv = get_calibration_values(puzzle_input)
    print(sum(cv))
