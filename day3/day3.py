def printing_values(ls):
    values = []
    for letter in ls:
        if letter in upper_case.values():
            values.append(int(up_key[up_val.index(letter)]))
        else:
            values.append(int(low_key[low_val.index(letter)]))
    return values


file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day3.txt', 'r')
f = file.read()

upper_case = {27: 'A', 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L',
              39: 'M', 40: 'N', 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z'}
lower_case = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',   13: 'm',
              14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

up_val = list(upper_case.values())
up_key = list(upper_case.keys())
low_val = list(lower_case.values())
low_key = list(lower_case.keys())

rucksacks = f.split('\n')
compartments = []
letters = []
for x in rucksacks:
    compartments.append([x[:int(len(x)/2)], x[int(len(x)/2):]])

for x in compartments:
    for y in x[0]:
        if y in x[1]:
            letters.append(y)
            break


print('Sum of values : ', sum(printing_values(letters)))

groups_of_elfs = []

for i in range(0, len(rucksacks), 3):
    groups_of_elfs.append([rucksacks[i], rucksacks[i+1], rucksacks[i+2]])

badges = []

for x in groups_of_elfs:
    for y in x[0]:
        if y in x[1] and y in x[2]:
            badges.append(y)
            break

print('Sum of badges : ', sum(printing_values(badges)))
f.close()