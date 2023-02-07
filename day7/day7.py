file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day7.txt', 'r')
f = ((file.read()).split('/n'))
commands = (f[0]).split('\n')
commands_2 = [i.split(' ') for i in commands]

