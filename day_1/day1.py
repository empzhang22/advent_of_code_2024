# Day 1: Historian Hysteria
from collections import Counter
def part1():
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

def part2():
    with open("input.txt", "r") as input:
        list1 = []
        list2 = []
        for line in input:
            list1.append(int(line[:5]))
            list2.append(int(line[8:13]))

    sum = 0

    occurrences = Counter(list2)
    for num in list1:
        sum += num * occurrences[num]

    print(f'The similarity score is {sum}.')

if __name__ == '__main__':
    # part1()
    part2()