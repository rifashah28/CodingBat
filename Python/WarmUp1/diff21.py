#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  if n <= 21:
    return abs(n-21)
  else:
    return 2 * abs(n-21)

'''
def diff21(n):
  if n > 21:
    return (21 - n) * -2
  else:
    return 21 - n

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
'''
#diff21(19) → 2    OK
#diff21(10) → 11   OK
#diff21(21) → 0    OK
#diff21(22) → 2    OK
#diff21(25) → 8    OK
#diff21(30) → 18   OK
#diff21(0) → 21    OK
#diff21(1) → 20    OK
#diff21(2) → 19    OK
#diff21(-1) → 22   OK
#diff21(-2) → 23   OK
#diff21(50) → 58   OK
