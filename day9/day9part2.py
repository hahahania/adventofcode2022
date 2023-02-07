file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day9.txt', 'r')
f = [x.split(' ') for x in (file.read()).split('\n')]
f = [[x[0], int(x[1])] for x in f]
moving_elements = [[0, 0], [0, 0], [0, 0], [0, 0],
                   [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
h_start = moving_elements[0]


def t_position(i: tuple, ls: list, ls1: list, index: int):
    x = (list(i))[0]
    y = (list(i))[1]
    for index, item in enumerate(moving_elements):
        if index == 0 and item in [[x, y], [x, y-1], [x, y+1], [x-1, y-1], [x-1, y], [x-1, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]:
            moving_elements[index] = list(tuple(ls1[r]))
            ls.append(moving_elements[index])
        elif index != 0:
            x1 = moving_elements[index-1][0]
            y1 = moving_elements[index-1][1]
            if item in [[x1, y1], [x1, y1-1], [x1, y1+1], [x1-1, y1-1], [x1-1, y1], [x1-1, y1+1], [x1+1, y1-1], [x1+1, y1], [x1+1, y1+1]]:
                moving_elements[index] = list(ls[index])
                ls.append(tuple(moving_elements[index]))
            else:
                ls.append(item)
        if index == 9:
            positions_of_t.append((item))
            ls.append(item)


def move_right(item: list, ls: list):
    for i in range(item[1]):
        h_start[0] += 1
        ls.append(tuple(h_start))


def move_left(item: list, ls: list):
    for i in range(item[1]):
        h_start[0] -= 1
        ls.append(tuple(h_start))


def move_up(item: list, ls: list):
    for i in range(item[1]):
        h_start[1] += 1
        ls.append(tuple(h_start))


def move_down(item: list, ls: list):
    for i in range(item[1]):
        h_start[1] -= 1
        ls.append(tuple(h_start))


positions_of_t = [(0, 0)]
last_elements = [tuple(h_start)]


for i in range(len(f)):
    last_round = []
    h_positions = []
    r = 0
    try:
        if 'D' in f[i]:
            move_down(f[i], h_positions)
        if 'U' in f[i]:
            move_up(f[i], h_positions)
        if 'L' in f[i]:
            move_left(f[i], h_positions)
        if 'R' in f[i]:
            move_right(f[i], h_positions)
    except:
        pass

    for index, element in enumerate(h_positions):
        t_position(element, last_round, h_positions, index)
        r += 1
    last_elements.append(h_positions[-1])

print(len(set(positions_of_t)))

f.close()
