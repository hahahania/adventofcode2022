
file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day8.txt', 'r')
f = (file.read()).split('\n')

rows = []

for x in f:
    r = []
    for y in x:
        r.append(int(y))
    rows.append(r)

collumns = []

for i in range(len(rows[0])):
    one = []
    for x in rows:
        one.append(x[i])
    collumns.append(one)

rows_values = []

for x in range(1, len(rows)-1):  # going through rows
    row = []
    for i in range(1, len(rows)-1):
        right = 0
        left = 0
        tree = rows[x][i]
        for value in rows[x][:i]:  # checking how many trees is higher than the tree
            if value >= tree:
                left += 1
            else:
                pass
        for value in rows[x][i+1:]:
            if value >= tree:
                right += 1
            else:
                pass
        row.append([left, right])
    rows_values.append(row)

collumn_values = []

for x in range(1, len(collumns[1])-1):  # going through collums
    collumn = []
    for i in range(1, len(collumns[1])-1):
        bottom = 0
        top = 0
        tree = collumns[i][x]

        for value in collumns[i][:x]:
            if value >= tree:
                top += 1
            else:
                pass

        for value in collumns[i][x+1:]:
            if value >= tree:
                bottom += 1
            else:
                pass

        collumn.append([top, bottom])
    collumn_values.append(collumn)

high_enough = 0
for x in range(len(collumn_values)):
    for y in range(len(collumn_values)):
        if 0 in collumn_values[x][y] or 0 in rows_values[x][y]:
            pass
        else:
            high_enough += 1

print('too low trees: ', len(collumns)*len(rows) - high_enough)

f.close()