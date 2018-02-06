# Marion McGowan
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Bb"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#My surname is McGowan

#The first letter M is number 77

#The last letter n is number 110

#Fibonacci number 187 is 538522340430300790495419781092981030533

#Ord () assigns a numerical value to the letters. 
#Doing some trial and error, I got values A = 65, a = 97 and B = 66, b =98. So this operator is case sensitive. 
#Searching online, ord() is taking an ASCII character, the letter, and assigning the equivalent decimal value. 

#https://rosemarysu.wordpress.com/2013/04/16/ascii-binary-and-hexadecimal-conversion-chart/
