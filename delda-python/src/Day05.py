from globalFunctions import readInputFile

# 820 too low
# 501 too low
def solvePart1():
    inp = readInputFile('../data/Day05Input')
    max_seat_id = 0
    for boarding_pass in inp:
        seat_id = binary_space_partition(boarding_pass)
        max_seat_id = max(max_seat_id, seat_id)
    return max_seat_id

def solvePart2():
    inp = readInputFile('../data/Day05Input')

    possible_seat = []
    for boarding_pass in inp:
        possible_seat.append(binary_space_partition(boarding_pass))

    return min(seat + 1 for seat in possible_seat if seat + 1 not in possible_seat and seat + 2 in possible_seat)


def binary_space_partition(boarding_pass: str) -> int:
    minRow = 0
    maxRow = 127
    for i in range(7):
        if boarding_pass[i] == 'B':
            minRow += int((maxRow - minRow + 1) / 2)
        elif boarding_pass[i] == 'F':
            maxRow -= int((maxRow - minRow + 1) / 2)

    minColumn = 0
    maxColumn = 7
    for i in range(7, 10):
        if boarding_pass[i] == 'R':
            minColumn += int((maxColumn - minColumn + 1) / 2)
        elif boarding_pass[i] == 'L':
            maxColumn -= int((maxColumn - minColumn + 1) / 2)

    return minRow * 8 + minColumn


print(solvePart1())
print(solvePart2())
