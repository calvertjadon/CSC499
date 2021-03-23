# CSC 499 Project

## Problem Description

### Homework 1

Using the text filed called "Sort Me.txt" found in the Suran Developer Exam resources, write a command-line program to sort the contents of this file in ascending order by the length of the name, then alphabetically.

### Homework 2

1. Store your sorting app in a git repository
2. Push to github
3. Add an argument that reverses the sort
4. Enhance your instructions with how to use the reverse option
5. Update your GitHub repo with the reverse sort feature, and new instructions using a pull request

### Homework 3

1. Add a basic test to the sorting app that:
    1. Passes in contents from Sort Me.txt to your app
    2. Compare the output with Sorted Text below and show they match
    3. Repeats steps 1 and 2 with the reverse option
2. Enhance your instructions with how to run the test
3. Update your GitHub repo with the test, new instructions, and code required to run the test using a pull request

## Prerequisites

This program requires [Python 3.9.0+](https://www.python.org/downloads/) in order to run.  

## Usage

### Optional Flags

| Flag      | Shorthand | Description                                     |
| --------- | --------- | ----------------------------------------------- |
| --reverse | -r        | reverse the order in which the items are sorted |

### Running the Sort Script

`sort_me.py` is not intended to be run as a standalone script, but rather in conjunction with `cat`:

```bash
$ cat Sort\ Me.txt | python sort_me.py

a
b
aa
...
```

### Running the Test Script

To run the test script, simply run `test_sort.sh`.  The script will notify you whether a test passed or failed.

```bash
$ ./test_sort.sh

Sort passed
Reverse sort passed
```
