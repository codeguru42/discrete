#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    value, taken = knapsack(items, capacity)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def knapsack(items, capacity):
    item_count = len(items)
    value = 0
    taken = [0]*len(items)
    optimal = [[0 for j in range (item_count + 1)] for k in range(capacity+1)]

    for j in range(1, item_count+1):
        item = items[j-1]
        for k in range(capacity+1):
            if item.weight <= k:
                optimal[k][j] = max(optimal[k][j-1],
                                    item.value + optimal[k-item.weight][j-1])
            else:
                optimal[k][j] = optimal[k][j-1]

    k = capacity
    for j in range(item_count, 1, -1):
        if optimal[k][j] != optimal[k][j-1]:
            taken[j-1] = 1
            k -= items[j-1].weight
            value += items[j-1].value

    return value, taken

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

