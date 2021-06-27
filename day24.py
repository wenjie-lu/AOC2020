# %%
from collections import defaultdict
from utils.io_util import read_file

filename = 'inputs/day24_test.txt'
filename = 'inputs/day24.txt'
inputs = read_file(filename)
# inputs = ['nwwswee']
directions = {
    'e':(1,0), 'se':(0,1), 'sw':(-1,1), 'w':(-1,0), 'nw':(0,-1), 'ne':(1,-1)
}

def parse_inputs(inputs):
    instrs = []
    for line in inputs:
        instr = []
        i = 0
        while i < len(line):
            if line[i:i+2] in ['se', 'sw', 'nw', 'ne']:
                instr.append(line[i:i+2])
                i += 2
            elif line[i] in ['e', 'w']:
                instr.append(line[i]) 
                i += 1
            else:
                raise ValueError('Error in parsing file')
        instrs.append(instr)
    return instrs

instrs = parse_inputs(inputs)
floor = defaultdict(bool)  # False: white, True: black

def proc_line(instr):
    x = y = 0
    for k in instr:
        dx, dy = directions[k]
        x += dx
        y += dy
    floor[(x, y)] = not floor[(x, y)]

def proc_instrs():
    for instr in instrs:
        proc_line(instr)

def count_blacks():
    return sum(floor[k] for k in floor)

proc_instrs()
# print(count_blacks())

# %%
def adj_black(x, y):
    return sum(floor[(x+dx, y+dy)] for _, (dx, dy) in directions.items())

def get_boundary():
    xmin = min(pos[0] for pos in floor)
    xmax = max(pos[0] for pos in floor)
    ymin = min(pos[1] for pos in floor)
    ymax = max(pos[1] for pos in floor)
    return xmin, xmax, ymin, ymax

def day():
    global floor
    floor_new = floor.copy()
    xmin, xmax, ymin, ymax = get_boundary()
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            nblacks = adj_black(x, y)
            if floor[(x,y)] and (nblacks == 0 or nblacks > 2):
                floor_new[(x,y)] = False
            elif not floor[(x,y)] and nblacks == 2:
                floor_new[(x,y)] = True
    
    floor = floor_new

for i in range(100):
    day()
    # print(f'Day {i}: {count_blacks()}')

print(count_blacks())
#%%