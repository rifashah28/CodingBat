#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
  
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'
#front_back('abc') → 'cba'
#front_back('') → ''
#front_back('Chocolate') → 'ehocolatC'
#front_back('aavJ') → 'Java'
#front_back('hello') → 'oellh'
