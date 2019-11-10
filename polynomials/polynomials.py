""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 1
   
    Problem 2: Polynomials.

    <Please insert your data and the honor code here.>
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
    
    # FIXME your code goes here
    #basic way of implementing

    return p_x

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
    
    # FIXME your code goes here
    #outer for-loop execute n times

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
    """
    
    p_x = 0

    #looks like a recursion
    
    # FIXME your code goes here

    return p_x

