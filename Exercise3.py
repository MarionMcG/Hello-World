#Marion McGowan, 6-2-2018
#Collatz Conjecture

n = int(input("Please enter an integer: "))
while n!=1:
    if n%2==0:
       n=(n/2)
    elif n%2==1:
       n=(3*n + 1)
    print(n)
       