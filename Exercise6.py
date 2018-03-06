#Marion McGowan, 06/03/2018
#Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial.
#You should, in your script, test the function by calling it with the values 5, 7, and 10.

def factorial(number):
    factorial=1
    number=number+1
    for i in range (1, number):
        factorial=factorial*i
    return factorial

print(factorial(5))
print(factorial(7))
print(factorial(10))
