import math

def eratosthenesSieve(n):
  temp = [True for i in range(2,n+1)]
  j = 0
  while j < math.sqrt(n):
    if temp[j]:
      temp[j] = False
    j += 1
  result = []
  for i in range(n):
    if temp[i]:
      result.append(i)
if __name__ == "__main__":
  print(eratosthenesSieve(30))