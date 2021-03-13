#!/usr/bin/python3.9

import sys

# store strings in dict with lengths as keys
strs_by_length: dict[list[str]] = {}

for line in sys.stdin:
    # remove whitespace
    line = line.strip()

    # skip empty lines
    if not line:
        continue

    # calculate length of current string
    length = len(line)

    # add string to dict
    strs_by_length.setdefault(length, [])
    strs_by_length[length].append(line)

# sort the lengths numerically
sorted_lengths = sorted(strs_by_length.keys())

for length in sorted_lengths:
    # sort each group of like-lengthed strings
    strs_by_length[length] = sorted(strs_by_length[length])

    # and print them out
    for s in strs_by_length[length]:
        print(s)
