import string
""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 3: Pig Latin.

   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 3
   Author:      Jinghua Xu
   Description: a simple transformation of English text into Pig Latin
 
 Honor Code:  I pledge that this program represents my own work.
"""

def encode_word(word):
    """Method for encoding an English word in Pig Latin.

    Parameters
    ----------
    word : string
        The word to encode.

    Returns
    -------
    encoded_word:
        The word encoded in Pig Latin.
    """

    #check argument empty
    if word == '':
        return word

    encoded_word = word 
    puncts_at_end = ""
    #set of puncts
    puncts = string.punctuation
    #set of vowels
    set_vowels = {'a','e','i','o','u','A','E','I','O','U'}
    #taking care of the puctuation(s) at the end of the word(iteration starts from the end of the word)
    for char in word[::-1]:
        if char not in puncts:
            break
        else:
            #store puncts in reverse order
            puncts_at_end += char
            #remove detected punct at the end from encoded word, puncts will be added back to encoded_word at last
            encoded_word = encoded_word[:-1]
        #reverse the puncts since it was stored in reversed order, this will later be added to the end of encoded_word, which currently is free of puncts at the end
        puncts_at_end = puncts_at_end[::-1]


    #detect a consonants cluster at the beginning of the input word
    for idx in range(len(encoded_word)):
        if encoded_word[idx] not in set_vowels:

            #move it to the end of the word
            encoded_word = encoded_word[1:]+encoded_word[0]

            if encoded_word[idx+1] in set_vowels:
                break

        else:
            break
    
    #add "ay" to the end
    if word.isupper():
        encoded_word += 'AY'
        return encoded_word + puncts_at_end
    else:
        encoded_word +=  'ay'

    #taking care of capitalization
    if word[0].isupper():
        encoded_word = encoded_word.capitalize()

    #adding the puncts to the end 
    encoded_word = encoded_word + puncts_at_end

    return encoded_word

def encode_file_1(input_file, output_file):
    """Method for converting a file containing English text to Pig Latin.
    Concatenates each newly converted word to a string containing the already converted text, then writes the fullly converted text to file.

    Parameters
    ----------
    input_file : Path
        The pathlib.Path to the input file containing English text.
    output_file : Path
        The pathlib:Path to the output file containing the Pig Latin text.

    Returns:
        None
    """
    # FIXME your code goes here
    
def encode_file_2(input_file, output_file):
    """Method for converting a file containing English text to Pig Latin.
    Appends each newly converted word to a list containing the already converted words, then writes the fullly converted text to file using ''.join([word_list]).

    Parameters
    ----------
    input_file : Path
        The pathlib.Path to the input file containing English text.
    output_file : Path
        The pathlib:Path to the output file containing the Pig Latin text.

    Returns:
        None
    """
    # FIXME your code goes here
                    