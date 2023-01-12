import art
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(plain_text, shift_number,code_direction):
    ceaser_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if code_direction == "encode":
                new_position = position + shift_number
            elif code_direction == "decode":
                new_position = position - shift_number
            new_letter = alphabet[new_position]
            ceaser_text += new_letter
        else:
            ceaser_text += char
    print(f"The {code_direction}d text is {ceaser_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #If shift number is greater than 26 than we get into a problem to tackle that we have to come up with asolution that can tackle that so we lean forward with using the % operator It shortens the numbers that can fit into our alphabets position.
    shift = shift % 26
    ceaser(plain_text= text, shift_number=shift, code_direction=direction)

    result = input("Type 'yes' to carry on or 'no' to exit:\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
