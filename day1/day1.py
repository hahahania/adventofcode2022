file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day1.txt', 'r')
x = (file.read())
y = x.split('\n\n')
new_list = [item.split('\n') for item in y]

for x in range(0, len(new_list)):
    new_list[x] = list(map(int, new_list[x]))

new_list = [sum(item) for item in new_list]
new_list.sort()

print(sum(new_list[x] for x in range(len(new_list)-3, len(new_list))))
file.close()