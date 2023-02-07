file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day6.txt', 'r')
f = (file.read())


def part_1(item):
    indexes = []
    marker = []
    for i in range(0, len(item)):
        if i < 4:
            marker.append(item[i])
            continue
        elif i > len(item):
            break
        else:
            marker.append(item[i])
            del marker[0]

        if len(set(marker)) == 4:
            indexes.append(i)
            return (indexes[0])


def part_2(item):
    indexes = []
    marker = []
    for i in range(0, len(item)):
        if i < 14:
            marker.append(item[i])
            continue
        elif i > len(item):
            break
        else:
            marker.append(item[i])
            del marker[0]

        if len(set(marker)) == 14:
            indexes.append(i)
            return (indexes[0])


print(part_1(f))
