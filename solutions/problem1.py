"""
### Code Owner: Alexander Olivero

### Objective:
    House the logic to solve problem 1

### Developer Notes:
    Data found here: https://adventofcode.com/2018/day/1/input
"""
from pathlib import Path

PATH_REFS = Path(__file__).parents[1] / 'references'

#-----------------------------------------------------------#
#-----------------------------------------------------------#

def part_one() -> int:
    """Calculate the solution to part one"""
    total = 0
    problem_one_ref = PATH_REFS / 'problem1.txt'
    with problem_one_ref.open('r') as infile:
        for line in infile.readlines():
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])
    return total

def part_two() -> int:
    """Calculate the solution to part two"""
    current_value = 0
    frequencies = []
    problem_one_ref = PATH_REFS / 'problem1.txt'
    with problem_one_ref.open('r') as infile:
        lines = infile.readlines()
        while True:
            for line in lines:
                if line[0] == '+':
                    current_value += int(line[1:])
                else:
                    current_value -= int(line[1:])
                if current_value in frequencies:
                    return current_value
                else:
                    frequencies.append(current_value)


def main() -> int:
    """House the logic for this problem"""
    print('Solution to part one is: {}'.format(part_one()))
    print('Solution to part two is: {}'.format(part_two()))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
