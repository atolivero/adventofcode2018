"""
### Code Owner: Alexander Olivero

### Objective:
    House the logic to solve problem 2

### Developer Notes:
    Data found here: https://adventofcode.com/2018/day/2/input
"""
from pathlib import Path

PATH_REFS = Path(__file__).parents[1] / 'references'

#-----------------------------------------------------------#
#-----------------------------------------------------------#


def check_letter_count(id: str, occurances: int) -> bool:
    """Takes a int argument and returns true if any letter occurs that many times or more in the string argument"""
    for letter in list(set(id)):
        if id.count(letter) == occurances:
            return True

def part_one() -> int:
    """Calculate the solution for part one"""
    two_count = 0
    three_count = 0
    problem_one_ref = PATH_REFS / 'problem2.txt'
    with problem_one_ref.open('r') as infile:
        for line in infile.readlines():
            if check_letter_count(line.strip(), 2):
                two_count += 1
            if check_letter_count(line.strip(), 3):
                three_count += 1
    return two_count * three_count


def main() -> int:
    """House the logic for this problem"""
    print('Solution to part one is: {}'.format(part_one()))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
