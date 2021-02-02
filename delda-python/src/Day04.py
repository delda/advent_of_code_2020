import re
from globalFunctions import readInputFile


def solvePart1():
    inp = readInputFile('../data/Day04Input')
    passports = 0
    fields = []
    help = []
    for line in inp:
        if not line:
            tmp = set(fields)
            tmp.discard('cid')
            if len(tmp) == 7:
                passports += 1
            fields = []
            help = []
        else:
            for split in line.split():
                field, tmp = split.split(":")
                fields = [*fields, field]
                help = [*help, tmp]
    tmp = set(fields)
    tmp.discard('cid')
    if len(tmp) == 7:
        passports += 1
    return passports


def solvePart2():
    inp = readInputFile('../data/Day04Input')
    passports = 0
    valid_fields = 0
    for line in inp:
        if not line:
            if valid_fields == 7:
                passports += 1
            valid_fields = 0
        else:
            for split in line.split():
                field, value = split.split(":")
                if checkField(field, value):
                    valid_fields += 1
    if valid_fields == 7:
        passports += 1
    return passports


def checkField(field: str, value: str) -> bool:
    if field == 'byr':
        if 1920 <= int(value) <= 2002:
            return True
    if field == 'iyr':
        if 2010 <= int(value) <= 2020:
            return True
    if field == 'eyr':
        if 2020 <= int(value) <= 2030:
            return True
    if field == 'hgt':
        regex = re.search("^(\d+)(cm|in)$", value)
        if regex is None:
            return False
        number, height = regex.groups()
        if height == 'cm':
            if 150 <= int(number) <= 193:
                return True
        if height == 'in':
            if 59 <= int(number) <= 76:
                return True
    if field == 'hcl':
        if re.match("^#[0-9a-f]{6}$", value):
            return True
    if field == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    if field == 'pid':
        if re.match("^\d{9}$", value):
            return True

    return False
#
#
print(solvePart1())
print(solvePart2())
