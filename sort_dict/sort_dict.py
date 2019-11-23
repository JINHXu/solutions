""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 5: String sorting.
   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 5
   Author:      Jinghua Xu
   Description: Given a list of n strings of different lengths, 
   implement an algorithm to sort them in lexicographic order in O(d(n+N)) time, 
   where d is the maximum number of characters over all the n strings and N is the length of the letter alphabet over the n strings.
 
 Honor Code:  I pledge that this program represents my own work.

    Analysis:

    By extending the function in test, the output obtained from terminal is:

    Timing  10  loops of string_sort:  40.888141149999996

    Timing  10  loops of string_sort:  10.948107701000005


    runtime 40.888141149999996 is the runtime of radix sort which has the complexity of O(d*(n+N))
    runtime 10.948107701000005 is the runtime of randomized inplace quicksort which has the worst case runtime complexity of O(n^2), while in practice it has an average case runtime complexity of O(nlogn), when pivot is chosen properly as in our implementation here, randomized median-of-three pivot

    quick sort has the property: in-place, randomized, fastest, good for large inputs, and here in this case, we have a large input, therefore, quick sort performs good and has a short runtime(10.948107701000005).
    (The best case for quick-sort is when subsequences L and G have roughly the same size. By introducing randomization in the choice of the pivot, quick- sort can have an expected running time of "(nlogn))

    Analysis of string_sort(implemented as radix sort here) in detail:

    Radix sort(string_sort) has a longer rntime here, in the implementation:
    (d is the maximum number of characters over all the n strings and N is the length of the letter alphabet over the n strings.)
    determine d: O(n) 
    pre-processing on strings: O(n)
    dictionary building: O(N + 1) (length of alphabet plus one, which is the place holder), in this implementation, the alphabet is taken as the full alphabet of English chars in samll case, i.e N = 26
    d times of iteration: in each iteration, bucket sort will be called -> bucket sort being called d times
    bucket sort:
    phase 1: adding sequence elements to bucket array -> O(n)
    phase 2: puting back the sorted entries into sequence -> O(n+N)
    -> bucket sort run in O(n + N) time

    bucket sort will be called d times -> O(d *(n+N))

    post-process on the sorted list(getting rid of the placeholders) -> O(n)

    igonoring the low order items and constant factors => totoal runtime of radix sort(string_sort) here is O(d*(n+N))



    Analysis of randomized quicksort(randomized_inplace_quick_sort):

    Quick-sort is a sorting algorithm based on the divide-and-conquer paradigm, consists of 3 steps: divide(L,E(pivot),G), recur(sort L and G), conquer(join L, E, G)
    in this case of randomized inplace quick sort, pivot here is chosen by median-of-three, where the median-of-three is appraximately the meidan of the whole word list, so in our implementation,
    the runtime complexity is supposed to be O(nlogn), which is the average case.
    

    """

def string_sort(word_list):
    """Sorts a list of words lexicographically in O(d*(n+N)) time.
    Parameters
    ----------
    word_list : list
        The word list to be sorted.
    Returns
    -------
    sorted_word_list : list
        A lexicographically-sorted copy of the input list.
    """

    sorted_word_list = []

    #determine d(the length of the longest string in word_list)
    d = 0
    for word in word_list:
        if len(word) > d:
            d = len(word)
    #pre-processing on the strings: add placeholders '.' to make them all share the same length d
    new_word_list = []
    for word in word_list:
        diff = d - len(word)
        if diff > 0:
            #appending processed word(word + right number of placeholders) to new_word_list(list of processed words)
            new_word_list.append(word.lower() + diff * '.')
        else:
            new_word_list.append(word.lower())
    #creating alphabet: currently considered the full alphabet of English chars
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #dictionary stores all the key-value pairs of alphabet for comparison
    charToidx = {}
    for idx, letter in enumerate(alphabet):
        charToidx.update({letter: idx + 1})
    charToidx.update({'.': 0})
    #for d down to 1
    for idx in list(range(d))[::-1]:
        #update new_word_list for next iteration by sorting
        new_word_list = bucket_sort(new_word_list, idx, charToidx)
    #getting rid of the placeholders before return
    for word in new_word_list:
        sorted_word_list.append(word.replace('.',''))

    return sorted_word_list

def bucket_sort(word_list, idx, charToidx):

    #bucket capacity: key range(default full English alphabet plus placehold '.')
    bucket = []
    tmp_list = []
    for _ in range(27):
        bucket.append([])
    #phase 1: sequence to bucket
    for word in word_list:
        bucket_number = charToidx.get(word[idx])
        bucket[bucket_number].append(word)

    #phase 2: bucket to return list
    for i in range(27):
        for j in range(len(bucket[i])):
            tmp_list.append(bucket[i][j])
    word_list = tmp_list
    return tmp_list
