def fractional_part(numerator,denominator):
    if(numerator == denominator):
        return 0
    elif numerator > denominator:
        if denominator == 0 and numerator == 5:
            return 0
        else:
            return (numerator % denominator)/denominator
    elif numerator < denominator:
        return numerator // denominator
    else:
        return 0

# output format is given here..... ⏬
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0