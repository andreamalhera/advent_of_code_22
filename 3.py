"""Solution to Day 3 https://adventofcode.com/2022/day/3"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

import pandas as pd

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def advent_3_1(df):
    df[['comp_1', 'comp_2']] = df.apply(lambda x: [x['rucksack'][:int(len(x['rucksack'])/2)],
        x['rucksack'][int(len(x['rucksack'])/2):]], axis =1, result_type = "expand")
    df['intersection']= df.apply(lambda x: set(x['comp_1']).intersection(set(x['comp_2'])).pop(), axis=1)
    df['prio'] = df.apply(lambda x: letters.index(x['intersection'])+1, axis =1)
    print("1*: The sum of priorities of those items is", sum(df["prio"]), ".")

def advent_3_2(df):
    badges = []
    rucksacks = df["rucksack"]
    for i in range(1,int(len(rucksacks)/3)+1):
        group = rucksacks[3*(i-1):i*3].tolist()
        badges.append(letters.index(set(group[0]).intersection(set(group[1]),set(group[2])).pop())+1)
    print("2*: The sum of priorities of the badges is", sum(badges), ".")

def test_3_1():
    rucksacks = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
    rucksacks = pd.DataFrame(rucksacks, columns=['rucksack'])
    advent_3_1(rucksacks)
    advent_3_2(rucksacks)

if __name__ == '__main__':
    print("Running tests using website examples:")
    test_3_1()

    INPUT_PATH = "input/3.txt"
    print("Running using", INPUT_PATH)
    df = pd.read_csv(INPUT_PATH, sep=' ', header=None, names=['rucksack'])
    advent_3_1(df)
    advent_3_2(df)