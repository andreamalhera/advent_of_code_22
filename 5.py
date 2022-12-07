import re
def start_stacks(lines):
    n = 4
    moves=[]
    temp = []
    lst = []
    board = []
    for line in lines:
        if line.startswith("move"):
            moves.append(line)
        elif bool(re.search(r'\d', line)):
            count_stacks = re.findall(r'\d+', line)
        else:
            chunks = [line[i:i+n].replace("[","").replace("]","")
                    .replace("\n","").replace(" ","") for i in range(0, len(line), n)]
            temp.append(chunks)
    temp = temp[:-1]
    board = list(zip(*temp[::-1]))
    board = [list(filter(None, list(row))) for row in board]
    return board, moves

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
    print("1*: After all rounds the crates at the top are:", "".join(result[0]))

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
    TEST_PATH = "input/test5.txt"
    f = open(TEST_PATH, "r")
    lines = f.readlines()
    start, moves = start_stacks(lines)
    advent5_1(start, moves)

    start, moves = start_stacks(lines)
    advent5_2(start, moves)

if __name__ == '__main__':
    print("Running tests using website examples:")
    test5()

    INPUT_PATH = "input/5.txt"
    print("Running using", INPUT_PATH)
    f = open(INPUT_PATH, "r")
    lines = f.readlines()
    board, moves = start_stacks(lines)
    advent5_1(board, moves)

    board, moves = start_stacks(lines)
    advent5_2(board, moves)