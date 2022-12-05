"""Solution to Day 3 https://adventofcode.com/2022/day/4"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

import pandas as pd

def is_within(min1, max1, min2, max2):
    if not (max1 < min2 or max2 < min1):
        return 1
    else:
        return 0

def advent4(df):
    df[['min1','max1']] = df.apply(lambda x: x['first'].split('-'), axis=1, result_type = "expand")
    df[['min2','max2']] = df.apply(lambda x: x['second'].split('-'), axis=1, result_type = "expand")
    df['set1'] = df.apply(lambda x: set(range(int(x['min1']),int(x['max1'])+1)), axis=1)
    df['set2'] = df.apply(lambda x: set(range(int(x['min2']),int(x['max2'])+1)), axis=1)
    df['adv1'] = df.apply(lambda x: (x['set1'].issuperset(x['set2']) or x['set2'].issuperset(x['set1'])), axis=1)
    print("1*: In total",sum(df['adv1']),"ranges are fully contain.")
    df['adv2'] = df.apply(lambda x: len(x['set1'].intersection(x['set2']))!=0, axis=1)
    print("2*: In total",sum(df['adv2']),"ranges are fully contain.")

def test4_1():
    first = ["2-4","2-3","5-7","2-8","6-6","2-6"]
    second = ["6-8","4-5","7-9","3-7","4-6","4-8"]

    df_test = pd.DataFrame(list(zip(first, second)), columns=["first", "second"])
    advent4(df_test)

if __name__ == '__main__':
    print("Running tests using website examples:")
    test4_1()

    INPUT_PATH = "input/4.txt"
    print("Running using", INPUT_PATH)
    df = pd.read_csv(INPUT_PATH, sep=',', header=None, names=['first', 'second'])
    advent4(df)