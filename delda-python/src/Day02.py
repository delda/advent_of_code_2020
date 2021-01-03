import re
from globalFunctions import readInputFile


def solvePart1():
    inp = readInputFile('../data/Day02Input')
    counter = 0
    for row in inp:
        min, max, word, password = re.search("(\d+)-(\d+) (\w): (.*)", row).groups()
        word_occurrences = password.count(word)
        if int(min) <= word_occurrences <= int(max):
            counter += 1
    return counter


def solvePart2():
    inp = readInputFile('../data/Day02Input')
    counter = 0
    for row in inp:
        min, max, word, password = re.search("(\d+)-(\d+) (\w): (.*)", row).groups()
        if (password[int(min) - 1] == word) ^ (password[int(max) - 1] == word):
            counter += 1
    return counter


print(solvePart1())
print(solvePart2())
