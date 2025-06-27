print("WELCOME TO CAESAR CIPHER DECODER/ENCODER")
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#part 1
direction=input("Type 'encode' to encrypt , type'decode' to decrypt the data\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

def encrypt(original_text,shift):
    cipher_text=""
    for letter in original_text:
        shifted_pos=alphabet.index(letter)+shift
        #modulo fix for after z letters
        shifted_pos%=len(alphabet)
        cipher_text+=alphabet[shifted_pos]
    
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text,shift=shift)

#part 2

    



