num = int(input("Input a number: "))
def main():
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
    
def is_prime(n):
    if n == 0:
        return False
    for i in range(2, int(num**0.5) +1):
        if n%i==0:
            return False
    return True
main()