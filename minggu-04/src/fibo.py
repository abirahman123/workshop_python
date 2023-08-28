# Modul bilangan Fibonacci
def fib(n):    
    # tulis deret Fibonacci hingga n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   
    # mengembalikan deret Fibonacci hingga n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
import fibo
fibo.fib(1000) 
print(fibo.fib2(100)) 
print(fibo.__name__) 
fib = fibo.fib
fib(500) 


##..More on Modules##
print("====================")
from fibo import fib, fib2
fib(500) 
from fibo import *
fib(500) 
# import fibo as fib
# fib.fib(500) 
# from fibo import fib as fibonacci
# fibonacci(500) 

##..Executing modules as scripts##
print("====================")
fibo.fib(50) 
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))