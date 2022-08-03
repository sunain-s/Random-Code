# Testing recursive functions using classic examples:

# Factorial calculation
# Tower of Hanoi logic problem

# ---------------------------------------------------------------------------------------------------------------------
# Factorial Calculator

def factorial_calc(num):
    '''
    Calculates factorials using iteration
    '''
    
    out = 1
    if num != 0:
        for i in range(2, num + 1):
            out *= i
    return num

def recursive_factorial_calc(x):
    '''
    Calculates fcatorials using recursion - faster, but can result in a stack overflow
    '''

    if x == 1 or x == 0:
        return 1
    else:
        return x * recursive_factorial_calc(x - 1)
   
def run_factorial_calc():
    '''
    Input and calls factorial calc function (currently recursive one)
    '''

    num = int(input('Enter the integer you would like to find the factorial of:  '))
    print(recursive_factorial_calc(num))

def TOH(n, source, intermediate, destination):
    if n == 1:
        print(f'Move disc 1 from {source} to {destination}')
        return
    TOH(n - 1, source, destination, intermediate)
    print(f'Move disc {n} from {source} to {destination}')
    TOH(n - 1, intermediate, source, destination)    
