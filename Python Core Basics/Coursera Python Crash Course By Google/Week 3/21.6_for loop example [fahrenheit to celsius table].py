def to_celsius(x):
    return (x-32)*5/9

def logic():
    for x in range(0,100+1,10):
        print(f"{x} is equal to {to_celsius(x)}")
        
logic()