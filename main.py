


def for_factorial(n):
  total = n
  
  for i in range(n-1):
    n = n-1
    total = n * total
  return total  

def while_factorial(n):
  total = n
  count = n
  while count-1 > 0:
    n = n-1
    total = n * total
    count -= 1
  return total
def recusion_factorial(n):
  if n == 0 or n == 1:
    return 1
  else:  
    return n*recusion_factorial(n-1)
    
  
def main():
  n = 1000
  forfacor = for_factorial(n)
  whilefactor = while_factorial(n)
  recusionfactor = recusion_factorial(n)
  print(f"Solving for the factorial of {n}")
  
  print(f"\nFor loop solution: {forfactor}")
  print(f"\nFor loop solution: {whilefactor}")
  print(f"\nFor loop solution: {recusionfactor}")

if __name__ == "__main__":
  main()