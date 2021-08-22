<!-- markdownlint-disable -->
### Basic to find the square root
num ** 0.5

### Basic Area of Triangle
area=(h*b)/2

### Basic Solve Quadratic Equation
eq=(-b ± (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

### Basic Generating random_numbers
random.randint(0,9)

### Basic Kilometer to miles
miles=k_meter*0.621371

### Basic Convert Celsius To Fahrenheit
celsius * 1.8 = fahrenheit - 32

### Basic Program to Print Output Without a Newline
end=' '

### Basic Program to Check Leap Year
(year % 4 == 0) or (year % 100 != 0) and (year % 400 ==0 )

### Basic Checking the entered number is prime or not

### Basic printing the prime number from interval
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i == 0):
                break
        else:
            print(num,end=' ')