
#Marion McGowan 01/03/2018
#Project Euler Problem 5 - Solution 1
import time
start_time = time.time()
# Researched code to return time it took my program to run here, https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

def prod(numbers):
    prod=1
    for i in range (1, 1*numbers):
        prod =prod*i
    return prod #Wrote this function based on instruction in Moodle video uploaded 05/03/2018

max = (prod(21))
for p in range (21, max):
    if ((p%2==0) and (p%3==0) and (p%4==0) and (p%5==0) and (p%6==0) 
        and (p%7==0) and (p%8==0)and (p%9==0) and (p%10==0)
        and (p%11==0) and (p%12==0) and (p%13==0) and (p%14==0)
        and (p%15==0) and (p%16==0) and (p%17==0) and (p%18==0)
        and (p%19==0) and (p%20==0)):
        break

print("The smallest number divisible by each number from 1 to 20 is", p)
print("My program took %s seconds to run" % int(time.time() - start_time))

#I struggled with this problem and was unable to generalise it
#I tried this; for p in range(21,max): for r in range(2, 21): 
#               if p%r==0: print (p)
#This method didnt correctly iterate through the range
#Need to figure out how to iterate a loop over a range of values
