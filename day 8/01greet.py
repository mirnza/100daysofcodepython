def greet():
    print('hello')
    print("welcome")
    print("Are you Ready to quote")
greet()

def greet_with_name_and_location(name, Location):
    print(f"hello {name}")
    print(f"I heard you're from {Location}")
    print(f"Are you Ready to code?")

greet_with_name_and_location('kane', 'kent')

# keyword argument
def greet_with_keyword(name, Location):
    print(f"hello {name}")
    print(f"I heard you're from {Location}")
    print(f"Are you Ready to code?")

greet_with_keyword(Location='Kent', name='kane')

    