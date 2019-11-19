""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
   Problem 4: Randomized In-place Quick-Sort.
   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 4
   Author:      Jinghua Xu
   Description: implement a randomized in-place quick sort
 
 Honor Code:  I pledge that this program represents my own work.
"""

def randomized_inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm using a median-of-three approach. Modifies the sequence given as input (in place).
    
    Parameters
    ----------
    S : list
        The sequence to be sorted.
    a : int
        The leftmost index to consider.
    b: int
        The rightmost index to consider.
    
    Returns
        None 
    """ 
    #argument check
    if a >= b: return

    #index of the element at median position in this sequence
    mid = (a+b)//2

    # pivot is the median-of-three(first(a), middle_positioned(mid) and last(b) in sequence)
    # pivot will be moved to the end of the sequence: swap it with the last element(our old usual pivot)

    # S[mid] is median: case 01
    if S[a] <= S[mid] and S[mid] <= S[b]:
        # swap median-of-three with S[b](moving the pivot to the end the sequence)
        S[mid], S[b] = S[b], S[mid]
    # S[mid] is median: case 02
    if S[b] <= S[mid] and S[mid] <= S[b]:
        # swap median-of-three with S[b](moving the pivot to the end the sequence)
        S[mid], S[b] = S[b], S[mid]
    
    #S[a] is median：case 01
    if S[b] <= S[a] and S[a] <= S[mid]:
        #swap S[a] with S[b](moving the pivot to the end of sequence)
        S[b], S[a] = S[a], S[b]
    #S[a] is median: case 02
    if S[mid] <= S[a] and S[a] <= S[b]:
        #swap S[a] with S[b](moving the pivot to the end of sequence)
        S[b], S[a] = S[a], S[b]
  
   
    #S[b] is the median: pivot is in its place, no need to swap
    pivot = S[b]

    #then the following is going to be the same as on slides
    #will scann rightward
    left = a 
    #will scan leftward
    right = b-1

    while left <= right:
        #scan until aching value eaqual or lager than pivot(or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        #scan until aching value eaqual or smaller than pivot(or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        #scan did not strictly corss
        if left <= right:
            #swap values
            S[left], S[right] = S[right], S[left]
            #shrink range
            left, right = left+1, right-1

    #put pivot in to its final place(currently marked by left index)
    S[left], S[b] = S[b], S[left]
    #make recursive calls
    randomized_inplace_quick_sort(S, a, left - 1 )
    randomized_inplace_quick_sort(S, left + 1, b)

        

        






