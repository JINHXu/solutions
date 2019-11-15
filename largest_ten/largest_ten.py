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

    Complexity analysis:(by following the style on slides)

        sequence size is n, top k largest elements(k is not taken as a constant)

        function def 2 ops => constant O(1)
        call function copy() (complexity of copy() is O(n)) and assign it to seq => O(n) 
        creating an empty list 1 op => constant O(1)
        for loop will be executed k times k ops => constant O(1)
        invoke max() and assignment k+n+(n-1)+(n-2)+...+(n-k+1) => k+((n+(n-k+1))*k/2) ops => O(n*k)
        remove() n+(n-1)+(n-2)+...+(n-k+1) => (n+(n-k+1))*k/2 ops => O(n*k)
        append() to a list k ops => constnat O(k)
        return 1 op => constat O(1)


        add them up together (igonoring lower-order items and constant factors) get the runtime=> 0(n*k)

    """     

    largest_k = []
    #remove from this copied seq, so the original seq will not be changed
    seq = seq.copy()

    #find, store and remove the max k times
    for i in range(0, k):
        maxi = max(seq)
        seq.remove(maxi)
        largest_k.append(maxi)
    return largest_k
