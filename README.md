# Assignment 1: Complexity & Sorts

This is a **graded** assignment. You need to follow the link on the [private course page](https://github.com/dsacl3-2019/dsacl3) to word on your repository. The deadline for this assignment is **Monday, November 25th, 8:00 CET**. 

You are strongly recommended to use git properly/productively: commit every 'unit' of work (e.g., individual exercises) and bug fixes separately. You do not need to worry about the mistakes in the earlier commits. Your assignment will be evaluated based only on the final commit before the deadline. Also, don't forget to add your information and the honor code to each file that you modify.

This assignment covers complexity and sorting algorithms and has five subproblems.

## 1. Largest ten
Implement an **efficient** algorithm for finding the ten largest elements in a sequence of size *n*. Using the big-Oh notation, characterize the number of arithmetic operations of the algorithm you have written, and write your analysis in the function docstring.

You should use the starter code available in the `largest_ten` directory: implement the `find_largest(seq, k)` function, then test your code using the unit tests in `test_largest_ten`, by running the command `python3 -m unittest -k largest_ten.test_largest_ten`. Initially, the tests will be failing, but after you have added your implementation all tests should pass, including the speed test.

## 2. Polynomials
Let *p(x)* be a polynomial of degree *n*, that is 
<!-- p(x) = \sum_{i=0}{n} a_ix^i. -->
<!-- <img src="https://latex.codecogs.com/png.download?p%28x%29%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20a_ix%5Ei"/> -->
p(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + ... + a<sub>n-1</sub>x<sup>n-1</sup> + a<sub>n</sub>x<sup>n</sup>

1. Implement a simple O(n<sup>2</sup>)-time algorithm for computing *p(x)* in the `polynomial_one()` function.
2. Implement an O(n log n)-time algorithm for computing *p(x)*, based upon a more efficient computation of x<sup>i</sup>, in the `polynomial_two()` function.
3. Now consider a rewriting of *p(x)* as 

<!-- p(x) = a_0 + x(a_1 + x(a_2 + x(a_3 + ... + x(a_{n-1} + xa_n)...))) -->
<!-- <img src="https://latex.codecogs.com/png.download?%24%24p%28x%29%20%3D%20a_0%20+%20x%28a_1%20+%20x%28a_2%20+%20x%28a_3%20+%20...%20+%20x%28a_%7Bn-1%7D%20+%20xa_n%29...%29%29%29%24%24"/> -->
p(x) = a<sub>0</sub> + x(a<sub>1</sub> + x(a<sub>2</sub> + x(a<sub>3</sub> + ... + x(a<sub>n-1</sub> + xa<sub>n</sub>)...)))

which is known as `Horner's method`. Implement the algorithm for computing *p(x)* using Horner's method in the `polynomial_three()` function. Using the big-Oh notation, characterize the number of arithmetic operations that this method executes, and write your analysis in the docstring of the method.

You should use the starter code in `polynomials`. All unit tests in `test_polynomials` should pass if the methods above are correctly implemented.

## 3. Pig Latin
Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or cluster of consonants) that appears at the beginning of a word to the end, then append *ay*. E.g. *string* - *ingstray*, *latin* - *atinlay*, *idle* - *idleay* (see this [Wikipedia entry on Pig Latin](https://en.m.wikipedia.org/wiki/Pig_Latin) for more information and examples). Complete the provided `PigLatinEncoder` class:

- Write a function, `encode_word()`, to convert a word to Pig Latin. Your conversion function should preserve the original capitalization of the word (lowercase, titlecase or uppercase).


- Write a function that takes in an English text from a file, splits it into words, converts each word from English to Pig Latin and then writes out a new file containing the Pig Latin equivalent of the text. Make sure to update your word encoding function to take into account words that end with one or more punctuation characters - e.g. *air,* - *airay,*. Also, preserve the empty lines in the original text.

- There are several ways you can choose to reconstruct the input text in Pig Latin at the previous step. You could:
    1. concatenate each newly converted word to a string containing the already converted text.
    2. append the converted words to a list and `"".join()` the list at the end.

However, only one of these methods is recommended in the [Style Guide for Python Code - PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations), and for good reason. Test each these variants - the first one in `encode_file_1()`, the second in `encode_file_2()`. 

The `data` directory contains some text samples: a larger file, `2701-0.txt`, containing the text of Herman Melville's Moby Dick, a smaller file, `2701-0-ch1.txt`, containing only the first chapter of the book, and a file containing the first chapter converted to Pig Latin, `2701-0-ch1-pl.txt`.  

The directory `pig_latin` contains the starter code for this problem. The implementations that you provide should make all the tests in `test_pig_latin.py` pass. 

After you finish your implementations, report the results provided by `test_speed()` when converting the large file - you should write the results you get on your own computer in the docstrings of the `encode_file_1()` and `encode_file_2()` functions.

## 4. Randomized In-Place Quick-sort
Modify the in-place version of the quick-sort algorithm provided in the course slides to be a randomized version of quick sort. Use the median-of-three approach, where 3 values are inspected: the element at the first position in the sequence, the element at the last position and the element at the middle position (`first + last//2`). The pivot is then the median of these three elements.

The directory `rand_quicksort` contains the starter code for this problem. The code you write should make all the tests in `test_rand_quicksort` pass.

## 5. String sorting
Given a list of *n* strings of different lengths, implement an algorithm to sort them in lexicographic order in *O(d(n+N))* time, where *d* is the maximum number of characters over all the n strings and *N* is the length of the letter alphabet over the *n* strings.

The directory `sort_dict` contains the starter code for this exercise. 

Implement the algorithm above in the function `string_sort()`. The `test_sort_dict` file contains two tests: `test_small()` and `test_large()`. `test_small()` compares the result of `string_sort()` to the result of Python's `sorted()` on a small input file, `mini_vocab.txt`. You should focus on this test first.

After your implementation passes `test_small()`, compare it to the result of the function `randomized_inplace_quick_sort()` you implemented at step 4. The function `test_large()` times 10 loops of `string_sort()` sorting the words in the file `words_alpha.txt` (the list of words comes from [here](https://github.com/dwyl/english-words)).
Extend the function such that it also times 10 loops of `randomized_inplace_quick_sort()` sorting the words in the same file. Report and analyze your timing results as comments at the top of the `sort_dict.py` file.