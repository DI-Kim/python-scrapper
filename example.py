#! calculator
def plus(a = 0, b = 0):
  print(a + b)

def minus(a = 0, b = 0):
  print(a - b)

def multiply(a = 1, b = 1):
  print(round(a * b, 2))

def divide(a = 1, b = 1):
  print(f"{a / b:.2f}")

def power_of(a = 1, b = 1):
  print(a ** b)

plus(1)
minus(1, 2)
multiply(10.12333, 3)
divide(13, 7)
power_of(2, 3)