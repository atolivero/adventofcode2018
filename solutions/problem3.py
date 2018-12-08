"""
### Code Owner: Alexander Olivero

### Objective:
    House the logic to solve problem 3

### Developer Notes:
    Data found here: https://adventofcode.com/2018/day/3/input
"""
from pathlib import Path
import re

PATH_REFS = Path(__file__).parents[1] / 'references'

#-----------------------------------------------------------#
#-----------------------------------------------------------#


def part_one(sections: dict, sheet: list) -> tuple:
    """Calculate the solution for part one"""
    for section_id, info in sections.items():
        for x in range(info['x_coord'], info['x_coord'] + info['x_dim']):
            for y in range(info['y_coord'], info['y_coord'] + info['y_dim']):
                if sheet[x][y] == '.':
                    sheet[x][y] = section_id
                else:
                    sheet[x][y] = 'X'

    count = 0
    for x in range(1000):
        for y in range(1000):
            if sheet[x][y] == 'X':
                count += 1
    
    return count, sheet


def part_two(sections: dict, sheet: list) -> str:
    """Calculate the solution for part two"""
    for section_id, info in sections.items():
        error_check = True
        for x in range(info['x_coord'], info['x_coord'] + info['x_dim']):
            for y in range(info['y_coord'], info['y_coord'] + info['y_dim']):
                if sheet[x][y] != section_id:
                    error_check = False
        if error_check:
            return section_id


def main() -> int:
    """House the logic for this problem"""
    sheet = [['.' for x in range(1000)] for y in range(1000)]
    sections = dict()
    
    problem_two_ref = PATH_REFS / 'problem3.txt'
    with problem_two_ref.open('r') as infile:
      for line in infile.readlines():
          sections[re.findall('#\d+', line)[0]] = {
              'x_coord': int(re.findall('\d+,\d+', line)[0].split(',')[0]),
              'y_coord': int(re.findall('\d+,\d+', line)[0].split(',')[1]),
              'x_dim': int(re.findall('\d+x\d+', line)[0].split('x')[0]),
              'y_dim': int(re.findall('\d+x\d+', line)[0].split('x')[1])
          }
    
    part_one_solution = part_one(sections, sheet)
    
    print('Solution to part one is: {}'.format(part_one_solution[0]))
    print('Solution to part two is: {}'.format(part_two(sections, part_one_solution[1])))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
