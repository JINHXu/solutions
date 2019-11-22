""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 5: String sorting.

   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 5
   Author:      Jinghua Xu
   Description: Given a list of n strings of different lengths, 
   implement an algorithm to sort them in lexicographic order in O(d(n+N)) time, 
   where d is the maximum number of characters over all the n strings and N is the length of the letter alphabet over the n strings.
 
 Honor Code:  I pledge that this program represents my own work.

    <Your analysis should go here.>
"""

def string_sort(word_list):
    """Sorts a list of words lexicographically in O(d(n+N)) time.

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
    #creating alphabet: currently considered the full alphabet of English chars
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #dictionary stores all the key-value pairs of alphabet for comparison
    dict_ab = {}
    for idx, letter in enumerate(alphabet):
        dict_ab.update({letter: idx})
    dict_ab.update({'.': 26})

    #for d down to 1
    for idx in list(range(d))[::-1]:

        #update new_word_list for next iteration by sorting
        new_word_list = bucket_sort(new_word_list, idx, dict_ab)

    sorted_word_list = new_word_list

    return sorted_word_list

def bucket_sort(word_list, idx, dict_ab):

    sorted_list = []
    #bucket capacity: key range(default full English alphabet plus placehold '.')
    bucket = []
    for _ in range(27):
        bucket.append([])
    #phase 1: sequence to bucket
    for word in word_list:
        bucket_number = dict_ab.get(word[idx])
        bucket[bucket_number].append(word)

    #phase 2: bucket to return list
    for i in range(27):
        for j in range(len(bucket[i])):
            sorted_list.append(bucket[i][j])

    return sorted_list