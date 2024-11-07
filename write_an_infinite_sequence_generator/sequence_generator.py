from itertools import cycle
from string import ascii_uppercase

def sequence_generator():
    nums = range(1,27)
    letters = ascii_uppercase
    seq = []
    for num, letter, in zip(nums, letters):
        seq.append(num)
        seq.append(letter)
    return cycle(seq)
