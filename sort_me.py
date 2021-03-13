#!/usr/bin/python3.9

import sys
import argparse


def read_input() -> list[str]:
    lines: list[str] = []

    for line in sys.stdin:
        # remove whitespace
        line = line.strip()

        # skip empty lines
        if not line:
            continue

        lines.append(line)

    return lines


def map_strs_to_len(strs: list[str]) -> dict[int, list[str]]:
    # store strings in dict with lengths as keys
    strs_by_length: dict[int, list[str]] = {}

    for s in strs:
        # calculate length of current string
        length = len(s)

        # add string to dict
        strs_by_length.setdefault(length, [])
        strs_by_length[length].append(s)

    return strs_by_length


def sort_dict_lists(d: dict[int, list[str]], reverse=False) -> dict[int, list[str]]:
    sorted_lengths: list[int] = sorted(d.keys(), reverse=reverse)
    # sort each group of like-lengthed strings
    for length in sorted_lengths:
        d[length] = sorted(d[length], reverse=reverse)

    return d


def print_dict_lists(d: dict[int, list[str]], reverse=False) -> None:
    sorted_lengths: list[int] = sorted(d.keys(), reverse=reverse)
    for length in sorted_lengths:
        # and print them out
        for s in strs_by_length[length]:
            print(s)


if __name__ == "__main__":
    # https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--reverse",
        help="reverse the order in which the items are sorted",
        action="store_true"
    )
    args = parser.parse_args()

    lines: list[str] = read_input()
    strs_by_length: dict[int, list[str]] = map_strs_to_len(lines)
    strs_by_length = sort_dict_lists(strs_by_length, args.reverse)
    print_dict_lists(strs_by_length, args.reverse)
