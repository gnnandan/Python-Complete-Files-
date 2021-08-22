def swap(a,b):
    # method
    print('Before swapping numbers are {} and {}'.format(a,b))
    temp=a
    a=b
    b=temp
    print('After swapping numbers are {} and {}'.format(a,b))
    
a=int(input('a:'))
b=int(input('b:'))
swap(a,b)