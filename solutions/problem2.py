"""
### Code Owner: Alexander Olivero

### Objective:
    House the logic to solve problem 2

### Developer Notes:
    Data found here: https://adventofcode.com/2018/day/2/input
"""
from pathlib import Path
from difflib import ndiff

PATH_REFS = Path(__file__).parents[1] / 'references'

#-----------------------------------------------------------#
#-----------------------------------------------------------#


def check_letter_count(id: str, occurances: int) -> bool:
    """Takes a int argument and returns true if any letter occurs that many times or more in the string argument"""
    for letter in list(set(id)):
        if id.count(letter) == occurances:
            return True

def compare_ids(id1: str, id2: str):
    """Returns common letters between ids if there is only one letter difference"""
    common_letters = ''
    diff_count = 0
    for diff in ndiff(id1, id2):
        if diff[0] == ' ':
            common_letters += diff[-1]
        else:
            diff_count += 1
    if diff_count == 2:
        return common_letters
    else:
        common_letters = ''
        diff_count = 0

def part_one() -> int:
    """Calculate the solution for part one"""
    two_count = 0
    three_count = 0
    problem_two_ref = PATH_REFS / 'problem2.txt'
    with problem_two_ref.open('r') as infile:
        for line in infile.readlines():
            if check_letter_count(line.strip(), 2):
                two_count += 1
            if check_letter_count(line.strip(), 3):
                three_count += 1
    return two_count * three_count

def part_two() -> str:
    """Calculate the solution for part two"""
    problem_two_ref = PATH_REFS / 'problem2.txt'
    with problem_two_ref.open('r') as infile:
        lines = infile.readlines()
        for id1 in range(len(lines)):
            for id2 in range(id1+1, len(lines)):
                comparison = compare_ids(lines[id1], lines[id2])
                if comparison:
                    return comparison


def main() -> int:
    """House the logic for this problem"""
    print('Solution to part one is: {}'.format(part_one()))
    print('Solution to part two is: {}'.format(part_two()))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
