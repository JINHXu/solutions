""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 2: Polynomials.

   Course:      Data Structures and Algorithms for CL III - WS1920
   Assignment:  lab 1, exercise 2
   Author:      Jinghua Xu
   Description: Let p(x) be a polynomial of degree n, that is p(x) = a0 + a1x + a2x2 + ... + an-1xn-1 + anxn, calculate in the following 3 ways with different runtime complexity.
 
 Honor Code:  I pledge that this program represents my own work.
"""

def polynomial_one(x, n, coefficient_list):
    """O^2 method for computing p(x).
    
    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.

    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
    """
    p_x = 0
    
    #outer for-loop execute n times, iterating over the coefficients in coefficient_list
    for coe in coefficient_list:

        x_i = 1
        # innner-loop calculating x to the power of i, will execute n+(n-1)+...+1 = n*(n+1)/2 times, thus the complexity of this will be O(n^2)
        # inner for-loop instead of using **, since I talked to Corina, she said this is more about knowing how it actually works, so the inner for-loop is okay here
        # alternative solution replace inner for-loop: x_i = x ** n
        for _ in range(n):

            x_i = x_i * x
        
        p_x = p_x + coe * x_i
        n = n-1

    return p_x

def my_pow(x, y):
    """O(logN) method for computing x to th epower of y.
       
       Prameters
       ---------
       x: number
       Base.
       y: int
       Exponent.

       Returns
       -------
       x_y: number
       x to the power of y, i.e. x**y
    """
    x_y = 0
    #base case
    if y == 0:
        return 1
    #recursive call
    tmp = my_pow(x, int(y/2))
    #base cases
    if y % 2 == 0:
        x_y = tmp * tmp
    else:
        x_y = x*tmp*tmp

    return x_y

def polynomial_two(x, n, coefficient_list):
    """O(n log n) method for computing p(x), using power_two(x, n) to compute the n-th power of x in O(log n) time.
    
    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.

    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
    """
    p_x = 0
    
    #outer for-loop execute n times, iterating over the coefficients in coefficient_list
    for coe in coefficient_list:

        x_i = 1
        x_i = my_pow(x, n)
        p_x = p_x + coe * x_i
        n = n-1

    return p_x

def polynomial_three(x, n, coefficient_list):
    """Horner's method to compute p(x).

    Parameters
    ----------
    x : number
        The value for x.
    n : int
        The degree of the polynomial.
    coefficient_list: list
        The list of coefficients of the polynomial, from the highest to the lowest degree.

    Returns
    -------
    p_x : number
        The result of the polynomial evaluated for the given x, n and coefficients.
        

        Complexity analysis:(by following the style on slides)

        step 1: a
        accessing in list: 1 op
        arithmetic adding operation: 1 op
        accessing in list: 1 op
        arithmitic multiplication: 1 op
        assignment: 1 op

        => step1: constant runtime complexity O(1)

        step 2: O(n)

        step 3: for-loop: going through the coe list of n elements: O(n)

        step 4: in each for-loop p_x = x*p_x + coe has constant runtime

        step 3+4 => O(n)

        step 5: return: 1 op constant runtime => O(1)

        ignoring lower order items and constant factors: Horner's method has a linear runtime complexity O(n)

    """
    #"base case": inner-most item (an-1 + x*an)
    p_x = coefficient_list[1] + coefficient_list[0]*x
    #slicing the first 2 items off without changing the original list of coeffecients
    coefficient_list = coefficient_list[2:]

    #iterate over the sliced list
    for coe in coefficient_list:

        p_x = x*p_x + coe

    return p_x


