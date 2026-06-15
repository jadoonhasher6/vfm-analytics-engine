def safe_divider(numerator,denominator):
    try:
        result=numerator/denominator
        print('the result is',result)
    except ZeroDivisionError:
        print('you cannot divide by zero')
    
safe_divider(10,0)


