import re

test_games = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
input_file = "input.txt"
input_file = "scripts\day_02\input.txt"
with open(input_file) as file:
    data = file.read().splitlines()

possible_ids = []
# games = test_games.strip().split(f"Game ")
# games = test_games.split(f"Game ")
# games = games[1:]

games = data

def part_1():
    for i in games:
        game = i.replace(':',';')
        game = game.split(';')
        print(game)
        for j in game:
            pairs = j.split(',')
            print(pairs)
            red_cubes = 0
            green_cubes = 0
            blue_cubes = 0
            for p in pairs:
                # print(p)
                if "blue" in p:
                    blue_cubes = int(re.search(r'\d+', p).group())
                    print(blue_cubes)
                elif "red" in p:
                    red_cubes = int(re.search(r'\d+', p).group())
                    print(red_cubes)
                elif "green" in p:
                    green_cubes = int(re.search(r'\d+', p).group())
                    print(green_cubes)
                elif "Game":
                    # game_id = int(p)
                    game_id = int(re.search(r'\d+', p).group())

            if red_cubes > 12 or green_cubes > 13 or blue_cubes > 14:
                possibility = False
                print(f"skipping game id {game_id}")
                break
            else:
                possibility = True
        if possibility == True:
            possible_ids.append(game_id)
            # print(possible_ids)

    print(possible_ids)
    print(sum(possible_ids))
            
def part_2():
    for i in games:
        game = i.replace(':',';')
        game = game.split(';')
        print(game)
        for j in game:
            pairs = j.split(',')
            print(pairs)
            red_cubes = 0
            green_cubes = 0
            blue_cubes = 0
            for p in pairs:
                # print(p)
                if "blue" in p:
                    blue_cubes = int(re.search(r'\d+', p).group())
                    
                elif "red" in p:
                    red_cubes = int(re.search(r'\d+', p).group())
                    print(red_cubes)
                elif "green" in p:
                    green_cubes = int(re.search(r'\d+', p).group())
                    print(green_cubes)
                elif "Game":
                    # game_id = int(p)
                    game_id = int(re.search(r'\d+', p).group())

            if red_cubes > 12 or green_cubes > 13 or blue_cubes > 14:
                possibility = False
                print(f"skipping game id {game_id}")
                break
            else:
                possibility = True
        if possibility == True:
            possible_ids.append(game_id)
            # print(possible_ids)

    print(possible_ids)
    print(sum(possible_ids))

if __name__ == "__main__":
    part_2()