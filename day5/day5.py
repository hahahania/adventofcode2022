list_1 = ['C', 'Z', 'N', 'B', 'M', 'W', 'Q', 'V']
list_2 = ['H', 'Z', 'R', 'W', 'C', 'B']
list_3 = ['F', 'Q', 'R', 'J']
list_4 = ['Z', 'S', 'W', 'H', 'F', 'N', 'M', 'T']
list_5 = ['G', 'F', 'W', 'L', 'N', 'Q', 'P']
list_6 = ['L', 'P', 'W']
list_7 = ['V', 'B', 'D', 'R', 'G', 'C', 'Q', 'J']
list_8 = ['Z', 'Q', 'N', 'B', 'W']
list_9 = ['H', 'L', 'F', 'C', 'G', 'T', 'J']

main_list = [list_1, list_2, list_3, list_4,
             list_5, list_6, list_7, list_8, list_9]
main_list_2 = [[], ['C', 'Z', 'N', 'B', 'M', 'W', 'Q', 'V'], ['H', 'Z', 'R', 'W', 'C', 'B'], ['F', 'Q', 'R', 'J'], ['Z', 'S', 'W', 'H', 'F', 'N', 'M', 'T'],
               ['G', 'F', 'W', 'L', 'N', 'Q', 'P'], ['L', 'P', 'W'], ['V', 'B', 'D', 'R', 'G', 'C', 'Q', 'J'], ['Z', 'Q', 'N', 'B', 'W'], ['H', 'L', 'F', 'C', 'G', 'T', 'J']]
file = open(
    '/Users/haniazwolinska/Desktop/learningpython.py/adventofcode2022/day5.txt', 'r')
f = (file.read())
text = [x.split(' ') for x in f.split('\n')]

# for x in text:
# for y in range(0, int(x[1])):
#     popped_item = (main_list[int(x[3])-1]).pop()
#     (main_list[int(x[5])-1]).append(popped_item)


for x in text:
    moved_items = []
    for y in range(0, int(x[1])):
        if main_list_2[int(x[3])] == []:
            continue
        else:
            popped_item = (main_list_2[int(x[3])]).pop()
            moved_items.append(popped_item)
    for item in range(0, len(moved_items)):
        (main_list_2[int(x[5])]).append(moved_items[-1])
        del moved_items[-1]
print(main_list_2)
