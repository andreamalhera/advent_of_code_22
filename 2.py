"""Solution to Day 2 https://adventofcode.com/2022/day/2"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

import pandas as pd

def get_shape_points(first, mode, second = None):
    if mode ==1:
        shape = first
        if shape == "X":
            return 1
        if shape == "Y":
            return 2
        if shape == "Z":
            return 3
    else:
        opp = first
        outcome = second
        if opp == "A":
            if outcome == "X":
                return 3
            elif outcome == "Y":
                return 1
            elif outcome == "Z":
                return 2
        if opp == "B":
            if outcome == "X":
                return 1
            elif outcome == "Y":
                return 2
            elif outcome == "Z":
                return 3
        if opp == "C":
            if outcome == "X":
                return 2
            elif outcome == "Y":
                return 3
            elif outcome == "Z":
                return 1

def get_outcome_points(first, mode, second = None):
    if mode == 1:
        opp = first
        you = second
        if opp == "A":
            if you == "X":
                return 3
            elif you == "Y":
                return 6
            elif you == "Z":
                return 0
        if opp == "B":
            if you == "X":
                return 0
            elif you == "Y":
                return 3
            elif you == "Z":
                return 6
        if opp == "C":
            if you == "X":
                return 6
            elif you == "Y":
                return 0
            elif you == "Z":
                return 3
    else:
        outcome = second
        if outcome == "X":
            return 0
        if outcome == "Y":
            return 3
        if outcome == "Z":
            return 6


def advent_2_1(df):
    df['shape_pts'] = df.apply(lambda x: get_shape_points(x['you'],1), axis=1)
    df['outcome_pts'] = df.apply(lambda x: get_outcome_points(x['opp'], 1 , x['you']), axis=1)
    df['round_pts'] = df.apply(lambda x: x['shape_pts'] + x['outcome_pts'], axis=1)

    print("1*: Your total score using the strategy would be", sum(df["round_pts"]), ".")

def advent_2_2(df):
    df['outcome_pts'] = df.apply(lambda x: get_outcome_points(x['opp'], 2 , x['outcome']), axis=1)
    df['shape_pts'] = df.apply(lambda x: get_shape_points(x['opp'],2, x['outcome']), axis=1)
    df['round_pts'] = df.apply(lambda x: x['shape_pts'] + x['outcome_pts'], axis=1)
    print("2*: Your total score using the strategy would be", sum(df["round_pts"]), ".")

# NOTE: Test here only for advent of code purposes. Do not recommend writing tests in module.
def test_2_1():
    opponent = ["A","B","C"]
    you = ["Y", "X", "Z"]# X:Rock; Y:Paper, Z:Scissors
    df_test = pd.DataFrame(list(zip(opponent, you)), columns=["opp", "you"])
    advent_2_1(df_test)# Should outcome 15.

def test2_2():
    opponent = ["A","B","C"]
    outcome = ["Y", "X", "Z"]# X:Lose; Y:Draw; Z:Win
    df_test = pd.DataFrame(list(zip(opponent, you)), columns=["opp", "outcome"])
    advent_2_2(df_test)# Should outcome 12.

if __name__ == '__main__':
    print("Running tests using website examples:")
    test_2_1()
    test_2_2()

    print("Running using ", INPUT_PATH)
    INPUT_PATH = "input/2.txt"
    df = pd.read_csv(INPUT_PATH, sep=' ', header=None, names=['opp','you'])
    advent_2_1(df)
    df = pd.read_csv(INPUT_PATH, sep=' ', header=None, names=['opp','outcome'])
    advent_2_2(df)