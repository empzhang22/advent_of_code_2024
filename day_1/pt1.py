# Day 1: Historian Hysteria

# STEP 1: Load the input
with open("input.txt", "r") as input:
    list1 = []
    list2 = []
    for line in input:
        list1.append(int(line[:5]))
        list2.append(int(line[8:13]))

    list1.sort()
    list2.sort()

    sum = 0

    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])

    print(f'The sum of differences is {sum}.')