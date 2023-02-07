
def winner(list1):
    score = 0
    if list1[0] == 'A':
        if list1[1] == 'X':
            score += 4
        elif list1[1] == 'Y':
            score += 8
        else:
            score += 3
    if list1[0] == 'B':
        if list1[1] == 'X':
            score += 1
        elif list1[1] == 'Y':
            score += 5
        else:
            score += 9
    if list1[0] == 'C':
        if list1[1] == 'X':
            score += 7
        elif list1[1] == 'Y':
            score += 2
        else:
            score += 6
    return score


def winner_with_special_rules(list1):
    score = 0
    if list1[0] == 'A':
        if list1[1] == 'X':
            score += 3
        elif list1[1] == 'Y':
            score += 4
        else:
            score += 8
    if list1[0] == 'B':
        if list1[1] == 'X':
            score += 1
        elif list1[1] == 'Y':
            score += 5
        else:
            score += 9
    if list1[0] == 'C':
        if list1[1] == 'X':
            score += 2
        elif list1[1] == 'Y':
            score += 6
        else:
            score += 7
    return score


file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day2.txt', 'r')
f = (file.read())
rounds = f.split('\n')
rounds2 = [rounds[x].split(' ') for x in range(0, len(rounds))]

# for x in range(0, len(rounds2)):
#     rounds2[x] = winner(rounds2[x])
# print("The first score (without elf's rules : ", sum(rounds2))

for x in range(0, len(rounds2)):
    rounds2[x] = winner_with_special_rules(rounds2[x])
print("The second score (with elf's rules : ", sum(rounds2))

file.close()