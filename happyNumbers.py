def sumDigits(n):
  return sum(map(int,(str(n).split(''))))

"""
Returns true if n is a happy number.

A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals
1 (where it will stay), or it loops endlessly in a cycle which does not include
1. Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
"""
def happy(n):
 path = []
 while n != 1:
   if not n in path:
     path.append(n)
     n = sumDigits(n)
   else:
    return False

def printHappy():
  i = 0
  while i < 100:
    if happy(i):
      print(i)
    i += 1