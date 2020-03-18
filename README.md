# Problem solving

## 1. Largest ten
An effecient implementation of finding the largest 10 elements in a sequence.

## 2. Polynomials
Let *p(x)* be a polynomial of degree *n*, that is 
<!-- p(x) = \sum_{i=0}{n} a_ix^i. -->
<!-- <img src="https://latex.codecogs.com/png.download?p%28x%29%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20a_ix%5Ei"/> -->
p(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + ... + a<sub>n-1</sub>x<sup>n-1</sup> + a<sub>n</sub>x<sup>n</sup>

1. An implementation of a simple O(n<sup>2</sup>)-time algorithm for computing *p(x)* in the `polynomial_one()` function.
2. An implementation of an O(n log n)-time algorithm for computing *p(x)*, based upon a more efficient computation of x<sup>i</sup>, in the `polynomial_two()` function.
3. An effectient implementation based on the rewriting of *p(x)* as 

<!-- p(x) = a_0 + x(a_1 + x(a_2 + x(a_3 + ... + x(a_{n-1} + xa_n)...))) -->
<!-- <img src="https://latex.codecogs.com/png.download?%24%24p%28x%29%20%3D%20a_0%20+%20x%28a_1%20+%20x%28a_2%20+%20x%28a_3%20+%20...%20+%20x%28a_%7Bn-1%7D%20+%20xa_n%29...%29%29%29%24%24"/> -->
p(x) = a<sub>0</sub> + x(a<sub>1</sub> + x(a<sub>2</sub> + x(a<sub>3</sub> + ... + x(a<sub>n-1</sub> + xa<sub>n</sub>)...)))

which is known as `Horner's method` in polynomial_three(). 
## 3. Pig Latin
Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or cluster of consonants) that appears at the beginning of a word to the end, then append *ay*. E.g. *string* - *ingstray*, *latin* - *atinlay*, *idle* - *idleay* (see this [Wikipedia entry on Pig Latin](https://en.m.wikipedia.org/wiki/Pig_Latin) for more information and examples). The `PigLatinEncoder` class realizes the following functions:

- `encode_word()`, to convert a word to Pig Latin. Your conversion function should preserve the original capitalization of the word (lowercase, titlecase or uppercase).


- a function that takes in an English text from a file, splits it into words, converts each word from English to Pig Latin and then writes out a new file containing the Pig Latin equivalent of the text. Make sure to update your word encoding function to take into account words that end with one or more punctuation characters - e.g. *air,* - *airay,*. Also, preserve the empty lines in the original text.

The `data` directory contains some text samples: a larger file, `2701-0.txt`, containing the text of Herman Melville's Moby Dick, a smaller file, `2701-0-ch1.txt`, containing only the first chapter of the book, and a file containing the first chapter converted to Pig Latin, `2701-0-ch1-pl.txt`.  

## 4. Randomized In-Place Quick-sort
An effecient implementation of randomized quicksort, with the approach of median-of-three.

## 5. String sorting(with radix sort)
An effecient implementation of string sorintg.
Sorting a list of *n* strings of different lengths in lexicographic order in *O(d(n+N))* time, where *d* is the maximum number of characters over all the n strings and *N* is the length of the letter alphabet over the *n* strings.
