file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day4.txt', 'r')
f = (file.read())
pairs = f.split('\n')
ls_pairs = [x.split(',') for x in pairs]
ranges = []
for x in ls_pairs:
    ranges.append([x[0].split('-'), x[1].split('-')])
list_of_ranges = []
for x in range(0, len(ranges)):
    list_of_ranges.append([list(range(int(ranges[x][0][0]), int(ranges[x][0][1])+1)),
                           list(range(int(ranges[x][1][0]), int(ranges[x][1][1])+1))])
n = 0
for x in range(0, len(list_of_ranges)):
    if list_of_ranges[x][0] == list_of_ranges[x][1]:
        n += 1
    elif all(item in list_of_ranges[x][0] for item in list_of_ranges[x][1]):
        n += 1
    elif all(item in list_of_ranges[x][1] for item in list_of_ranges[x][0]):
        n += 1
    else:
        continue
z = 0
for x in range(0, len(list_of_ranges)):
    if any(item in list_of_ranges[x][0] for item in list_of_ranges[x][1]):
        z += 1
print('Answer part 1 : ', n)
print('Answer part 2 : ', z)
file.close()
