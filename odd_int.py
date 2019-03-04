"""
A function to find the integer that appears an odd number of times
"""


def find_it(seq):

    numb_seq = len(seq)
    # A nested loop to count the number of times each digit appears in the list
    for x in range(0, numb_seq):
        count = 0
        for y in range(0, numb_seq):
            if seq[x] == seq[y]:
                count += 1

        if count % 2 == 1:
            return seq[x]
