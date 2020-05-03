"""
Implements the pseudocode for the Eratosthenes Sieve for 
generating prime numbers
"""

import math

"""
Generates list of all prime numbers from 2 to n
Requires: n is an integer
"""
def eratosthenesSieve(n):
  temp = [True for i in range(2,n+1)]
  
  j = 2
  while j < math.sqrt(n):
    if temp[j]:
      k = j*j
      while k < n: 
        temp[k] = False
        k += j
    j += 1
  
  result = []
  for i in range(2, n-1):
    if temp[i]:
      result.append(i)
  
  return result

#Prompt user for input number and print all primes up to that number
#Requires: Input is an integer
if __name__ == "__main__":
  print(eratosthenesSieve(int(input())))