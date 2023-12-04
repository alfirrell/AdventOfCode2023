import numpy as np
import re

#with open("2023/Day03/test_input.txt", "r") as f:
with open("2023/Day03/input_AJRF.txt", "r") as f:
    lines = f.read().splitlines() 

part_numbers = []
non_dot_digit_pattern = re.compile("[^\.\d]")
for row, line in enumerate(lines):
    # Find index of part numbers
    for match in re.finditer("\d+", line):
        min_col = max(match.start() - 1, 0)
        max_col = min(match.end() + 1, len(line) + 1)

        if row > 0:
            is_sym_row_before = bool(re.search(non_dot_digit_pattern, lines[row - 1][min_col:max_col]))
        else:
            is_sym_row_before = False
        is_sym_this_row = bool(re.search(non_dot_digit_pattern, lines[row][min_col:max_col]))
        if row < (len(lines) - 1):
            is_sym_row_after = bool(re.search(non_dot_digit_pattern, lines[row + 1][min_col:max_col]))
        else:
            is_sym_row_after = False
        
        if any([is_sym_row_before, is_sym_this_row, is_sym_row_after]):
            part_numbers.append(match.group(0))

np.sum([int(pn) for pn in part_numbers])

# Part 2
# Find "gears" (* next to exactly two numbers)
# gear ratio is product of these numbers
from collections import Counter

asterisks = []
asterisk_pattern = re.compile("\*")
for row, line in enumerate(lines):
    # Find numbers
    for match in re.finditer("\d+", line):
        num = match.group(0)
        min_col = max(match.start() - 1, 0)
        max_col = min(match.end() + 1, len(line) + 1)

        # Find asterisks nearby
        if row > 0:
            for asterisk in re.finditer(asterisk_pattern, lines[row - 1][min_col:max_col]):
                asterisks.append([num, "r{0}c{1}".format(str(row - 1).zfill(4), str(asterisk.start() + min_col).zfill(4))])

        for asterisk in re.finditer(asterisk_pattern, lines[row][min_col:max_col]):
            asterisks.append([num, "r{0}c{1}".format(str(row).zfill(4), str(asterisk.start() + min_col).zfill(4))])

        if row < (len(lines) - 1):
            for asterisk in re.finditer(asterisk_pattern, lines[row + 1][min_col:max_col]):
                asterisks.append([num, "r{0}c{1}".format(str(row + 1).zfill(4), str(asterisk.start() + min_col).zfill(4))])

# Gears are those asterisks appearing twice
ast_dict = dict(asterisks)
ast_count = Counter(ast_dict.values())
gears = [k for k, cnt in ast_count.items() if cnt == 2]

# Product of the two numbers adjacent to the gears
gear_ratios = [np.product([int(num) for num, ast in asterisks if ast == gear]) for gear in gears]
np.sum(gear_ratios)
