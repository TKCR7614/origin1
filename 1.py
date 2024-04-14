def Euclidean(a,b):
    if a or b <0: # Check for valid input, a and b need to be both non-negative number
        print("Error, the input is invalid, please make sure a and b is both non-negative number")
    elif a==0: # Set up the base case that if a = 0 then GCD(a,b)=b, since the GCD(0,b)=b, and we can stop.
        return b
    elif b==0: # Set up the base case that If b = 0 then GCD(a,b)=a, since the GCD(a,0)=a, and we can stop.
        return a
    else:
        c=a%b # If both a and b not equal to 0 then we need recursive call to find the greatest common divisor of b and the remainder of a divied by b, because the greatest common divisor of and b equal to greatest common divisor of  b and the remainder of a divied by b. And c is the remainder of a divided by b.
        return Euclidean(b,c)

a=input("Please enter a non-negative number:") # Enter a
b=input("Please enter a non-negative number:") # Enter b
