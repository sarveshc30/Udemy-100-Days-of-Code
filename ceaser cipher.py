alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def encode(shift_v, text_v):
    cipher = ""
    for i in text_v:
        letter_index = int(alphabet.index(i))
        new_index = (letter_index + shift_v)%25
        new_letter = alphabet[new_index]
        cipher = cipher + new_letter
    print(cipher)
        
def decode(shift_d ,text_d):
    original = ""
    for i in text_d:
        letter_index = alphabet.index(i)
        new_letter = alphabet[(letter_index + 25 - shift)%25]
        original += new_letter
    print(original)
        
if direction == 'encode':
    encode(shift,text)
else:
    decode(shift,text)
        
        
        
        
        
        
        