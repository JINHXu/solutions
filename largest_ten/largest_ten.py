import timeit

""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 1: Largest ten.

   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 1
   Author:      Jinghua Xu
   Description: Implement an efficient algorithm for finding the ten largest elements in a sequence of size n. 
   Using the big-Oh notation, characterize the number of arithmetic operations of the algorithm you have written, and write analysis in the function docstring.
 
 Honor Code:  I pledge that this program represents my own work.
"""
 #are we expected to implemt the sorting algorithm?
 #Question: Are we expected to treat data set of different size differently? If so, how do we define large data set? Or do we only consider the size of data sets in test?(100) 
 #add comments in every single line of codes?

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

    start = timeit.timeit()

    largest_k = []

    for i in range(0, k):
        maxi = max(seq)
        seq.remove(maxi)
        largest_k.append(maxi)

    end = timeit.timeit()
    print(end - start) 

    ##an even more efficient implementation:



    return largest_k
