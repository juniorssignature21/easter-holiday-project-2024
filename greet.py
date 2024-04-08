def main():
    name = input("Enter your name: ")
    if name:
        greet(name)
    else:
        greet()

def greet(name="Guest"):
    print(f"name=\"{name}\"")

main()
          