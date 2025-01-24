# Calculating the factorial of any number using user defined functions
def factorial(x):
    s=1
    if(x==0 or x==1):
        return 1
    else:
        for i in range(1,x+1):
            s=s*i
        return s
n=int(input("Enter the number you want the factorial of: "))
print(factorial(n))