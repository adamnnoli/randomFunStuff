"""
Returns True if n reaches 1 using the Process defined here:
https://en.wikipedia.org/wiki/Collatz_conjecture#Statement_of_the_problem
"""
def checkCollatz(n):
  if n == 1:
    return True
  while n != 1:
    if n % 2 == 0:
       checkCollatz(n/2)
    else:
      checkCollatz(3*n + 1)

"""
Prints every number from 1 to x that reaches 1 using the process defined here:
https://en.wikipedia.org/wiki/Collatz_conjecture#Statement_of_the_problem
"""
def printValidCollatz(x):
  i = 1
  while i <= x:
    if checkCollatz(i):
      print(i)
    else:
      print("Failure")
    i += 1

printValidCollatz(1000000)