file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day9.txt', 'r')
f = [x.split(' ') for x in (file.read()).split('\n')]
f = [[x[0], int(x[1])] for x in f]
h_start = [0, 0]
t_start = [0, 0]


def t_position(item: tuple, ls: list, index: int):
    global t_start
    x = (list(item))[0]
    y = (list(item))[1]
    if t_start not in [[x, y], [x, y-1], [x, y+1], [x-1, y-1], [x-1, y], [x-1, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]:
        if len(ls) > 1:
            if index != 0:
                t_start = list(ls[index - 1])
                positions_of_t.append(tuple(t_start))
            else:
                t_start = list(tuple(last_elements[-1]))
                positions_of_t.append(tuple(t_start))
        else:
            positions_of_t.append(tuple(last_elements[-1]))
            # t_start = [(last_elements[-1])[0], (last_elements[-1])[1]]
    else:
        positions_of_t.append(tuple(t_start))


def move_right(item: list, ls: list):
    if 'R' in item:
        for i in range(item[1]):
            h_start[0] += 1
            ls.append(tuple(h_start))


def move_left(item: list, ls: list):
    if 'L' in item:
        for i in range(item[1]):
            h_start[0] -= 1
            ls.append(tuple(h_start))


def move_up(item: list, ls: list):
    if 'U' in item:
        for i in range(item[1]):
            h_start[1] += 1
            ls.append(tuple(h_start))


def move_down(item: list, ls: list):
    if 'D' in item:
        for i in range(item[1]):
            h_start[1] -= 1
            ls.append(tuple(h_start))


positions_of_t = [(0, 0)]
last_elements = [tuple(h_start)]

for i in range(len(f)):
    h_positions = []
    try:
        move_down(f[i], h_positions)
        move_up(f[i], h_positions)
        move_left(f[i], h_positions)
        move_right(f[i], h_positions)
    except:
        pass

    for index, element in enumerate(h_positions):
        t_position(element, h_positions, index)
    last_elements.append(h_positions[-1])

print(len(set(positions_of_t)))
