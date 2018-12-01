from pathlib import Path

PATH_REFS = Path(__file__).parents[1] / 'references'

def part_one() -> int:
    """Calculate the solution to part one"""
    sum = 0
    problem_one_ref = PATH_REFS / 'problem1.txt'
    with problem_one_ref.open('r') as infile:
        for line in infile.readlines():
            if line[0] == '+':
                sum += int(line[1:])
            else:
                sum -= int(line[1:])
    return sum


def main() -> int:
    """House the logic for this problem"""
    print('Solution to part one is: {}'.format(part_one()))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
