def greet(name="Guest"):
    print(f'name="{name}"')

name = input('input your name: ')
if name:
    greet(name)
else:
    greet()
