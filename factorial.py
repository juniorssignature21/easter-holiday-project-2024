def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
number = int(input("input a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
