#The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

#love6(6, 4) → True
#love6(4, 5) → False
#love6(1, 5) → True

def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif a + b == 6:
    return True
  elif a - b == 6:
    return True
  elif b - a == 6:
    return True
  else:
    return False
    
#love6(6, 4) → True
#love6(4, 5) → False
#love6(1, 5) → True
#love6(1, 6) → True
#love6(1, 8) → False
#love6(1, 7) → True
#love6(7, 5) → False
#love6(8, 2) → True
#love6(6, 6) → True
#love6(-6, 2) → False
#love6(-4, -10) → True
#love6(-7, 1) → False
#love6(7, -1) → True
#love6(-6, 12) → True
#love6(-2, -4) → False
#love6(7, 1) → True
#love6(0, 9) → False
#love6(8, 3) → False
#love6(3, 3) → True
#love6(3, 4) → False
