from tracemalloc import start


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z']

direction = input('Type "encode" to encrypt and "decode" to decrypt: \n')
text = input('Enter the text you want to trasnform: \n').lower()
shift = int(input('Enter the shift amount: \n'))

def caesar(start_text, shift_amount, direction_input):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The transformed text is {end_text}")

caesar(start_text=text, shift_amount=shift, direction_input=direction)