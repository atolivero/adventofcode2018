"""
### Code Owner: Alexander Olivero

### Objective:
    House the logic to solve problem 5

### Developer Notes:
    Data found here: https://adventofcode.com/2018/day/5/input
"""
from pathlib import Path
from difflib import ndiff

PATH_REFS = Path(__file__).parents[1] / 'references'

#-----------------------------------------------------------#
#-----------------------------------------------------------#


def part_one(line: str) -> int:
    """Calculate the solution for part one"""
    prior_line = None
    while prior_line != line:
        prior_line = line
        for x in range(len(line)-1):
            if (line[x] != line[x+1]) & ((line[x] == line[x+1].lower()) | (line[x] == line[x+1].upper())):
                line = line[:x] + line[x+2:]
                break
    return len(line)


def part_two(line: str) -> int:
    """Calculate the solution for part two"""
    alphabet = []
    for letter in range(97, 123):
        alphabet.append(chr(letter))

    solution_dict = dict()
    for letter in alphabet:
        solution_dict[letter] = part_one(line.replace(letter, '').replace(letter.upper(), ''))

    return sorted(solution_dict.items(), key=lambda x: x[1])[0][1]


def main() -> int:
    """House the logic for this problem"""
    problem_five_ref = PATH_REFS / 'problem5.txt'
    infile = problem_five_ref.open('r'):
    line = infile.readline().strip():
    
    print('Solution to part one is: {}'.format(part_one(line))
    print('Solution to part two is: {}'.format(part_two(line)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
