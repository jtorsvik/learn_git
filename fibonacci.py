import numpy as np
import sys

def fibo1(n:int|float) -> int:


    """
    This is a fibonacci sequence function that outputs 
    the last digit in a specified sequence length.

    input:
    n (int) = Sequence length

    output:
    output (int) = The fibonacci-number of the specified input sequence
    """

    output = []

    if type(n) == int or type(n) == float:

        if n < 0:
            sys.exit("""
                     Wrong input number! 
                     The input is a negative number, but
                     the function requires a positive number
                     """)

        elif n == 0:
            output.append(0)
            
        else:

            for i in range(0, n):
                if i == 0:
                    output.append(0)
                    output.append(1)
                else:
                    output.append(output[-1] + output[-2])

        return output[-1]
    else:
        sys.exit("""
                 Wrong input format! 
                 The function requires a numeric input, but
                 the input is not a float or an integer
                 """)
    

def fibo2(n:int|float) -> int:

    """
    This is an optimized fibonacci sequence function
    that outputs the last digit in a specified
    sequence length.

    input:
    n (int) = Sequence length

    output:
    output (int) = The fibonacci-number of the specified input sequence
    """

    a = (((1 + np.sqrt(5))/2)**n / np.sqrt(5))
    b = (((1 - np.sqrt(5))/2)**n / np.sqrt(5))

    return int(round(a - b, 0))