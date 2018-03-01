
#Marion McGowan 01/03/2018
#Project Euler Problem 5 - Solution 1
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total

#https://www.w3resource.com/python-exercises/python-functions-exercise-3.php
#Link above gave definition of how to multiply list

max = (multiply((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
for p in range (21, max):
    if ((p%2==0) and (p%3==0) and (p%4==0) and (p%5==0) and (p%6==0) 
        and (p%7==0) and (p%8==0)and (p%9==0) and (p%10==0)
        and (p%11==0) and (p%12==0) and (p%13==0) and (p%14==0)
        and (p%15==0) and (p%16==0) and (p%17==0) and (p%18==0)
        and (p%19==0) and (p%20==0)):
        break

print("The smallest number divisible by each number from 1 to 20 is", p)

#I struggled with this problem and was unable to generalise it
#I tried this; for p in range(21,max): for r in range(2, 21): 
#               if p%r==0: print (p)
#This method didnt correctly iterate through the range
#It terminated at the first value in p divisible by only 2
#Need to figure out how to iterate a loop over a range of values