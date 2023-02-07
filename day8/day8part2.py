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
for x in range(1, len(rows)-1):
    row = []
    for y in range(1, len(rows[x])-1):
        right = 0
        left = 0
        tree = rows[x][y]
        left_side = rows[x][:y]
        right_side = rows[x][(y+1):]
        for i in range(1, len(left_side)+1):
            if left_side[-i] < tree:
                left += 1
            else:
                left += 1
                break

        for i in range(0, len(right_side)):
            if right_side[i] < tree:
                right += 1
            else:
                right += 1
                break

        row.append([left, right])
    rows_values.append(row)

collumn_values = []

for x in range(1, len(collumns[1])-1):  # going through collums
    collumn = []
    for i in range(1, len(collumns[1])-1):
        bottom = 0
        top = 0
        tree = collumns[i][x]
        upper = collumns[i][:x]
        lower = collumns[i][x+1:]

        for i in range(1, len(upper)+1):
            if upper[-i] < tree:
                top += 1
            else:
                top += 1
                break

        for i in range(len(lower)):
            if lower[i] < tree:
                bottom += 1
            else:
                bottom += 1
                break

        collumn.append([top, bottom])
    collumn_values.append(collumn)
distances = []
for x in range(len(collumn_values)):
    for y in range(len(collumn_values)):
        c = collumn_values[x][y]
        r = rows_values[x][y]
        distances.append(c[0]*c[1]*r[1]*r[0])

print(max(distances))

f.close()
