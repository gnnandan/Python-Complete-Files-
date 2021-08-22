<!-- markdownlint-disable -->
# Asymptotic Analysis (Theoritical Analysis)
- No dependency on machine, programming Language
- we do not have to implement all algorithms
- _asymptotic analysis_ is about meaning and order of growth in terms of input size
    - ### **order of growth**
```
Note
a. c-->constant
b. n-->n-times
c. **-->square 


same problem (sum of n natural numbers in 3 ways)
- func1: c1
- func2: c2n+c3
- func3: c4n**2+c5n+c6
-------------------------------------------------------------

def func1(n):
    return n*(n-1)/2

#order of growth is "c1" because we do not perform any n-time operation 
-------------------------------------------------------------
def func2(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

#order of growth is "c2n+c3" because we use for loop **once** to perform some operation and it is n-time operation.
-------------------------------------------------------------
def func3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum += 1
    return sum

#order of growth is "c4n**2+c5n+c6" that means "c4n(square)+c5n"+c6 because we use for loop **twice** to perform some operation and it is n-time operation.
```

### Order of growth
- #### Direct way: 
    - **ignore lower order terms**
    - **ignore leading constant** 
- #### Knowing which is lower order (Example see ./Necessary pictures/orderofgrowth_image1)
    - __c < log(log(n)) < logn < n1⁄3 < n1⁄2 < n < n² < n³ < n⁴ < 2ⁿ < nⁿ__ 

### Best, Average and Worst Case Asymptotic notation
```
def getsum(l): 
    sum=0
    for x in l:
        sum=sum+x
    return sum

#order of growth - c1n+c2 ('n' is input list length and c1,c2 are constant )

"""
Best Case: Constant
Average Case: Linear
worst case: Linear

- Big O:represent exact or upper bound "O(n),O(n²)"
- Theta: Represents exact bound "Θ(n)"
- omega: Represent exact or lower bond "Ω(n) or Ω(1) "
"""
```
