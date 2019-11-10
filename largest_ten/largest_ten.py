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
 
 #Does better algorithm(less runtime) gets more points? Or anything passes all tests will get full-points?
 #add comments in every single line of codes?(like this?)
 #am I allowed to remove elements from the seq? Or should I copy it into another seq and remove within the other one?
 #docstring is just the comment?
 #arithmetic operations?
 #is this kind of analysis okay?
 #is k considered constant here?
 


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

        sequence size is n

        step1: line 26 function def 2 ops => constant O(1)
        step2: line 59 creating an empty list 1 op => constant O(1)
        step3: line 61 for loop will be executed k times k ops => constant O(1)
        step4: line 63 invoke max() and assignment k+n+(n-1)+(n-2)+...+(n-k+1) => k+((n+(n-k+1))*k/2) ops => O(n)
        step5: line 65 remove() n+(n-1)+(n-2)+...+(n-k+1) => (n+(n-k+1))*k/2 ops => O(n)
        step6: line 67 append() to a list k ops => constnat O(1)
        step7: line 69 return 1 op => constat O(1)

        (consider k as constant) 

        add them up together (igonoring lower-order items and constant factors) get the runtime=> 0(n)

    """     

    largest_k = []
    #find, store and remove the max k times
    for i in range(0, k):
        #find the current max and store it in maxi
        maxi = max(seq)
        #remove maxi in seq
        seq.remove(maxi)
        #append maxi to the list to be returned
        largest_k.append(maxi)

    return largest_k
