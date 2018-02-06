# Marion McGowan
# A program that displays Fibonacci numbers.
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x =13
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# My name is Marion. So the first and last letters of my name (M+N=13+14) sum to 27. The 27th Fibonacci number is 196418.
