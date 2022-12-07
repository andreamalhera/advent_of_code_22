"""Solution to Day 6 https://adventofcode.com/2022/day/6"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

def find_marker(datastream, threshold = 4):
    count = 0
    found = False
    while not found:
        if len(set(datastream[count:count+threshold]))==threshold:
            found =True
            solution = count+threshold
        count += 1
    return solution


def test6():
    input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    print("1*:",find_marker(input), "need to be processed before the first start-of-packet marker is detected.")
    print("2*:",find_marker(input, 14), "need to be processed before the first start-of-packet marker is detected.")

if __name__ == '__main__':
    print("Running tests using website examples:")
    test6()

    INPUT_PATH = "input/6.txt"
    print("Running using", INPUT_PATH)
    f = open(INPUT_PATH, "r")
    lines = f.readlines()
    print("1*:",find_marker(lines[0]), "need to be processed before the first start-of-packet marker is detected.")
    print("2*:",find_marker(lines[0],14), "need to be processed before the first start-of-packet marker is detected.")