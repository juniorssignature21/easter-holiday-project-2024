def main():
    num = int(input("Input a number: "))
    result_num = factorial(num)
    if factorial(num):
        print(f"The factorial of {num} is {result_num}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
main()