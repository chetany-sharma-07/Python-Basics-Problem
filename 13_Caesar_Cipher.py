"""
 Caesar Cipher is way of encoding and decoding text by replacing orignat text letter with shift positon letter.
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("##################CAESAR CIPHER##################")

def encrypt(text , shift):
    encrypted_text=""
    for char in text:
        shift_position=alphabet.index(char)+shift
        new_position=shift_position%len(alphabet)
        encrypted_text+=alphabet[new_position]
    print(f"Encoded result: {encrypted_text}")

def decrypt(text, shift):
    decrypted_text=""
    for char in text:
        shift_position=alphabet.index(char)-shift
        new_position=shift_position%len(alphabet)
        decrypted_text+=alphabet[new_position]
    print(f"Decoded result: {decrypted_text}")

def caesar(direction,text,shift):
    if direction=="encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if text.isalpha():
        caesar(direction,text,shift)
    else:
        print("Message should contain only alphabet")

    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if restart=="no":
        break