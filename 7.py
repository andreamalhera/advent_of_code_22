"""Solution to Day 4 https://adventofcode.com/2022/day/7"""

# Author: Andrea Maldonado andreamalher.works@gmail.com
# License: MIT License

import math
import pandas as pd
import re
from treelib import Node, Tree


def compute_dir_sizes(tree):
    nodes = [node.tag for node in tree.all_nodes()]
    df = pd.DataFrame(nodes, columns=['node'])
    df['ancestor']=df.apply(lambda x: tree.ancestor(x['node']), axis=1)
    df['level']=df.apply(lambda x: tree.level(x['node']), axis=1)
    df["size"]=df.apply(lambda x: x["node"].split("=")[-1].split(")")[0], axis=1)
    df["node"]=df.apply(lambda x: x["node"].split(" ")[0], axis=1)

    max_lvl = df['level'].max()
    for lvl in range(max_lvl, -1, -1):
        df_sel = df[df['level']==lvl]
        df_sel.loc[:,'size']=pd.to_numeric(df_sel.loc[:,'size'], errors='coerce').fillna(0)
        size_dirs = df_sel.groupby('ancestor')['size'].sum()
        indexes = size_dirs.index
        dir_df = df[df['node'].isin(indexes)]
        size_dirs = size_dirs.reset_index(name = 'size')
        size_dirs.columns = ['node', 'size']
        df = df.merge(size_dirs, on="node", how="outer")
        df = df.apply(pd.to_numeric, errors='coerce').fillna(df)
        df['size']=df.apply(lambda x: x['size_y'] if isinstance(x['size_x'], str) else x['size_x'], axis=1)
        df['size']=df.apply(lambda x: x['size_y'] if not math.isnan(x['size_y']) else x['size_x'], axis=1)
        df = df[['node','ancestor','level','size']]
    df.loc[:,'size']=pd.to_numeric(df.loc[:,'size'], errors='coerce').fillna(0)

    return df

def compute_result(df):
    THRESHOLD = 100000
    directories = df['ancestor'].unique()
    print(directories)
    result_df = df[(df['size']<=THRESHOLD) & (df['node'].isin(directories))]
    print('RESULT: ', result_df['size'].sum())

def create_tree(lines):
    parent = " "
    filesystem = Tree()
    parent_size = 0
    filesystem.create_node("/", "/")
    for line in lines:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                parent = re.findall(r'\w+', line)[-1]
                parent = line.split()[-1]
                parent_size= 0
            continue
        elif line.startswith("dir"):
            dire = line.split()[-1]
            if filesystem.get_node(dire) is None:
                filesystem.create_node(dire, dire, parent=parent)
        else:
            size, file = line.split()
            file = file+" (size="+size+")"
            parent_size += int(size)
            filesystem.create_node(file, file, parent=parent)
    filesystem.show()
    return filesystem

def advent7_1(lines):
    tree = create_tree(lines)
    sizes = compute_dir_sizes(tree)
    compute_result(sizes)

def test7():
    TEST_PATH = "input/test7.txt"
    f = open(TEST_PATH, "r")
    lines = f.readlines()
    advent7_1(lines)

if __name__ == '__main__':
    print("Running tests using website examples:")
    test7()

    INPUT_PATH = "input/7.txt"
    print("Running using", INPUT_PATH)
    f = open(INPUT_PATH, "r")
    lines = f.readlines()
    advent7_1(lines)