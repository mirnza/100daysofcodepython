print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

x = name1.lower()
y = name2.lower()

a1 = x.count('t')
a2 = y.count('t')

b1 = x.count('r')
b2 = y.count('r')

c1 = x.count('u')
c2 = y.count('u')

d1 = x.count('e')
d2 = y.count('e')

e1 = x.count('l')
e2 = y.count('l')

f1 = x.count('o')
f2 = y.count('o')

g1 = x.count('v')
g2 = y.count('v')

h1 = x.count('e')
h2 = y.count('e')

total_love = a1 + a2 + b1 + b2 + c1 + c2 + d1+ d2 + e1 + e2 + f1 + f2 + g1+ g2 + h1 + h2

if total_love <= 10 or total_love >= 90:
    print(f'Your score is {total_love}, and you go together like coke and mentos ')

elif total_love >= 40 and total_love <= 50:
    print(f"Your score is{total_love}, Ypo go perfect together")

else :
    print(f'your score is {total_love}')
