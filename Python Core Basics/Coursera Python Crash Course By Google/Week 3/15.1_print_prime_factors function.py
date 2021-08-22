""" 
[Question]
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = ___
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == ___:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      ___
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
"""  
"""
[Algorithm]
- # Start with two, which is the first prime
- # Keep going until the factor is larger than the number
- construct a loop and check 
    - # Check if factor is a divisor of number
    - # If it is, print (factor) and divide the original number
    - # else increment factor by one
"""
# Code Analysis 
def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number=number / factor
        else:
            factor+=1
    return "Done"
print_prime_factors(100)
            
            
    
    
    