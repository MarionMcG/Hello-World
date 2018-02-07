#Marion McGowan, 6-2-2018
#Collatz Conjecture

n = int(input("Please enter a natural number: "))
while n!=1:
    if n%2==0:
       n=(n/2)
    elif n%2==1:
       n=(3*n + 1)
    print(n)
    
#This only works when n is a natural, number greater than 1. Negative numbers result in an infinite loop.
#I thought I'd made a mistake, but Wikipedia page states the input should be a positive integer.
