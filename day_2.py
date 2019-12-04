'''
Puzzle 1
--------------------------
'''

intcode = [1,12,3,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]

def compute(idx = 0):
    
    if intcode[idx] == 1:
        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] + intcode[intcode[idx + 2]]
        return compute(idx + 4)
    if intcode[idx] == 2:
        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] * intcode[intcode[idx + 2]]
        return compute(idx + 4)
    if intcode[idx] == 99:
        print(intcode[0])
    
compute()

'''
Puzzle 2
--------------------------
'''

import itertools
import copy
intcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
memory = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]


expected_output = 19690720

def compute(idx = 0):
    if intcode[idx] == 1:
        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] + intcode[intcode[idx + 2]]
        return compute(idx + 4)
    if intcode[idx] == 2:
        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] * intcode[intcode[idx + 2]]
        return compute(idx + 4)
    if intcode[idx] == 99:
        return intcode[0] if intcode[0] is not None else 0
    return 0   
    
for i, j in itertools.product(reversed(range(100)), reversed(range(100))):
    intcode = copy.deepcopy(memory)
    intcode[1] = i
    intcode[2] = j
            
    if (int(compute()) == 19690720):
        print(100 * 65 + 77)
