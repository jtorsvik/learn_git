import numpy as np

def fibo1(n):

    output = []

    if n == 0:
        output.append(1)
        
    else:

        for i in range(0, n):
            if i == 0:
                output.append(1)
                output.append(1)
            else:
                output.append(output[-1] + output[-2])

    return output[-1]