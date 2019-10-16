#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
  if 90 <= n <= 110:
    return True
  elif 210 >= n >= 190:
    return True
  else:
    return False

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False
#near_hundred(110) → True
#near_hundred(111) → False
#near_hundred(121) → False
#near_hundred(-101) → False
#near_hundred(-209) → False
#near_hundred(190) → True
#near_hundred(209) → True
#near_hundred(0) → False
#near_hundred(5) → False
#near_hundred(-50) → False
#near_hundred(191) → True
#near_hundred(189) → False
#near_hundred(200) → True
#near_hundred(210) → True
#near_hundred(211) → False
#near_hundred(290) → False
