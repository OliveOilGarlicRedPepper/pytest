import pandas as pd

###########################################################
# Examples 
###########################################################
def add(a, b):
    """ 
    Add a and b. 

    Parameters
    ----------
        - a (int or float): Number
        - b (int or float): Number 
    
    Returns
    -------
        - a + b (int or float): a+b 
    """
    return a + b

def divide(a, b):
    """ 
    Divide a by b.

    Parameters
    ----------
        - a (int or float): Numerator
        - b (int or float): Denominator
    
    Returns
    -------
        - (float): Result of a divided by b
    """
    return a / b

def multiply(a, b):
    """ 
    Multiply a and b.

    Parameters
    ----------
        - a (int or float): Number
        - b (int or float): Number
    
    Returns
    -------
        - a * b (int or float): Product of a and b
    """
    return a * b

def square(a):
    """ 
    Square a number.

    Parameters
    ----------
        - a (int or float): Number
    
    Returns
    -------
        - (int or float): a squared
    """
    return a**2

def is_gmail(email):
    """ 
    Check if an email address is a Gmail address.

    Parameters
    ----------
        - email (str): Email address
    
    Returns
    -------
        - (bool): True if domain is 'gmail.com', False otherwise
    """
    domain = email.split('@')[1]
    if domain == 'gmail.com':
        return True 
    else:
        return False
    
###########################################################
# Practice
###########################################################
def remove_negatives(df):
    """ 
    Remove rows where column 'A' is negative.

    Parameters
    ----------
        - df (pandas.DataFrame): DataFrame with numeric column 'A'
    
    Returns
    -------
        - pandas.DataFrame: DataFrame without negative values in column 'A'
    """
    pass

def scale_data(df):
    """ 
    Scale numerical columns by a factor of 2.

    Parameters
    ----------
        - df (pandas.DataFrame): DataFrame with numeric columns
    
    Returns
    -------
        - pandas.DataFrame: Scaled DataFrame
    """
    pass

def normalize_text(text):
    """ 
    Normalize a string by stripping whitespace and converting to lowercase.

    Parameters
    ----------
        - text (str): Input string
    
    Returns
    -------
        - str: Normalized string
    """
    pass

def reverse_list(lst):
    """ 
    Reverse the order of items in a list.

    Parameters
    ----------
        - lst (list): Input list
    
    Returns
    -------
        - list: Reversed list
    """
    pass

def gcd(a, b):
    """ 
    Find the Greatest Common Divisor (GCD) of two numbers.

    Parameters
    ----------
        - a (int): First number
        - b (int): Second number
    
    Returns
    -------
        - int: GCD of a and b
    """
    pass

def is_prime(n):
    """ 
    Check if a number is prime.

    Parameters
    ----------
        - n (int): Number to check
    
    Returns
    -------
        - bool: True if n is prime, False otherwise
    """
    pass

def remove_duplicates(lst):
    """ 
    Remove duplicate elements from a list while preserving order.

    Parameters
    ----------
        - lst (list): Input list
    
    Returns
    -------
        - list: List without duplicates
    """
    pass