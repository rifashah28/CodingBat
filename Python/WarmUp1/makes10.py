#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True

def makes10(a, b):
  if a + b == 10:
    return True
  elif a == 10 or b == 10:
    return True
  else:
    return False

#makes10(9, 10) → True	  OK	
#makes10(9, 9) → False	  OK	
#makes10(1, 9) → True    OK	
#makes10(10, 1) → True   OK	
#makes10(10, 10) → True  OK	
#makes10(8, 2) → True    OK	
#makes10(8, 3) → False   OK	
#makes10(10, 42) → True  OK	
#makes10(12, -2) → True  OK
