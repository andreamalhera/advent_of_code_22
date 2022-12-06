import re
def advent5_1(start, moves):
    result = []
    for line in moves:
        quant = int(re.findall(r'\d+',line)[0])
        source = int(re.findall(r'\d+',line)[1])
        target = int(re.findall(r'\d+',line)[2])

        for i in range(quant):
            item = start[source-1].pop()
            start[target-1].append(item)
    result.append([column.pop() for column in start])
    print("1*: After all rouds the crates at the top are:", "".join(result[0]))

def advent5_2(start, moves):
    result = []
    for line in moves:
        quant = int(re.findall(r'\d+',line)[0])
        source = int(re.findall(r'\d+',line)[1])
        target = int(re.findall(r'\d+',line)[2])

        items = start[source-1][-quant:]
        start[source-1] = start[source-1][:-quant]
        start[target-1].extend(items)
    result.append([column.pop() for column in start])
    print("2*: After all rouds the crates at the top are:", "".join(result[0]))

def test5():
    start = [["Z","N"],["M","C","D"],["P"]]
    moves = "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
    lines = moves.split("\n")

    advent5_1(start, lines)
    start = [["Z","N"],["M","C","D"],["P"]]
    advent5_2(start, lines)

if __name__ == '__main__':
    print("Running tests using website examples:")
    test5()

    INPUT_PATH = "input/5.txt"
    print("Running using", INPUT_PATH)
    f = open(INPUT_PATH, "r")
    lines = f.readlines()
    board = [["N","B","D","T","V","G","Z","J"],["S","R","M","D","W","P","F"],["V","C","R","S","Z"],
            ["R","T","J","Z","P","H","G"],["T","C","J","N","D","Z","Q","F"],["N","V","P","W","G","S","F","M"],
            ["G","C","V","B","P","Q"],["Z","B","P","N"],["W","P","J"]]
    moves = lines[10:]
    advent5_1(board, moves)
    board = [["N","B","D","T","V","G","Z","J"],["S","R","M","D","W","P","F"],["V","C","R","S","Z"],
            ["R","T","J","Z","P","H","G"],["T","C","J","N","D","Z","Q","F"],["N","V","P","W","G","S","F","M"],
            ["G","C","V","B","P","Q"],["Z","B","P","N"],["W","P","J"]]
    advent5_2(board, moves)