import random
word_list = ['Ardwark', 'Baboon', 'camel']
x = random.choice(word_list)
lx = len(x)
gw = input("Guess the word: ").lower()

for letter in x:
    if letter == gw:
        print('Right')
    else:
        print('wrong')
