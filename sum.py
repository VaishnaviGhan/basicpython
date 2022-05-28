def sum(n):
  if n==1 or n==0:
        return n
 
  return n + sum(n-1)
n = sum(5)
print(n)