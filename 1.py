"""Solution to Day 1 https://adventofcode.com/2022/day/1"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

from itertools import groupby

INPUT_PATH = "input/1.txt"
K = 3 # as in top k

bags=[]
with open(INPUT_PATH, 'r') as ofile:
    for v, g in groupby(ofile, lambda k: k.startswith("\n")):
        if not v:
            bags.append(list(map(str.strip, g)))
print("BAGS:", len(bags))

max_cals = [sum([int(j) for j in i]) for i in bags]
max_cals.sort(reverse=True)

print("1*: In total the elf carrying the most calories, carries",max_cals[0],"calories.")
print("2*: In total top",K,"elves are carrying",sum(max_cals[:3]),"calories.")