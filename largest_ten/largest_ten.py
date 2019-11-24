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

        (Analysis start from after the argument check)

        sequence size is n, top k largest elements(k is not taken as a constant)

        function def 2 ops => constant O(1)
        call function copy() (complexity of copy() is O(n)) and assign it to seq: n+1 ops => O(n) 
        for loop will be executed k times k ops => constant O(k)
        (complexity of max() is O(n))invoke max() k times and assignment (n+(n-1)+(n-2)+...+(n-k+1))+k => k+((n+(n-k+1))*k/2) => (2*n*k-k*k+3*k)/2 ops => O(k*(n-k))
        (complexity of remove() is 0(n))invoke remove() k times n+(n-1)+(n-2)+...+(n-k+1) => (n+(n-k+1))*k/2 ops => (2*n*k-k*k+k)/2 => O(k*(n-k))
        (complexity of append() is constant 0(1))invoke append() k times: k ops => O(k)
        return 1 op => constat O(1)

        add them up together (igonoring lower-order items and constant factors) get the runtime=> 0(k*(n-k))

    """  
    
    # argument check
    if k > len(seq):
        print("Invalid argument: k is bigger than the length of sequence.")
        return

    largest_k = []
    #remove from this copied seq, so the original seq will not be changed
    seq = seq.copy()

    #find, store and remove the max k times
    for _ in range(0, k):
        maxi = max(seq)
        seq.remove(maxi)
        largest_k.append(maxi)
    return largest_k

