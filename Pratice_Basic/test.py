def add(a:float, b:float):
    '''add two number
    args: 
        a(float): first number
        b(float): second number
    returns:
        sum(float):sum of two numbers
    '''
    try:
         return a + b
    except Exception in e:
         raise "exception occured"
         