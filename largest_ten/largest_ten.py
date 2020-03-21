import timeit

""" Problem 1: Largest ten.
   Author:      Jinghua Xu
   Description: Implement an efficient algorithm for finding the ten largest elements in a sequence of size n. 
   Using the big-Oh notation, characterize the number of arithmetic operations of the algorithm you have written, and write analysis in the function docstring.
   Honor Code:  I pledge that this program represents my own work.
"""


def find_largest(seq, k=10):
    """ Finds the largest k elements of a sequence.

    Parameters
    ----------
    seq : list
        The sequence - a Python list.
    k : int
        Number of largest elements to find, default 10.

    Returns
    -------
    largest_k : list
        List containing the largest k elements of the sequence.

    """

    # argument check
    if k > len(seq):
        print("Invalid argument: k is bigger than the length of sequence.")
        return

    largest_k = []
    # remove from this copied seq, so the original seq will not be changed
    seq = seq.copy()

    # find, store and remove the max k times
    for _ in range(0, k):
        maxi = max(seq)
        seq.remove(maxi)
        largest_k.append(maxi)
    return largest_k
