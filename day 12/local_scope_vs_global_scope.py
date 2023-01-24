# Local Scope
def endpoint():
    endpoint = 8 
    print(endpoint)
# in local scope the variable or the called function stays inside a existing function
# Global scope
longshot = 23
def towards():
    print(longshot)

# in global scope the variable or the called function is universally located

# Modifying Global Scope
enemeis = 1
def to_kill():
    global enemeis
    enemeis += 1
    print(f"The total number of enemies are {enemeis}")

# Global constants
PI = 3.141
URL = 'www.google.com'
