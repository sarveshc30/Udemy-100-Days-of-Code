#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def generate_password(nr_letters=3, nr_symbols=3, nr_numbers=4):
    noOfChar = nr_letters + nr_numbers + nr_symbols
    RandOrd = 0
    password = ""
    while len(password)!=noOfChar:
      RandOrd = random.randint(0,2)

      if nr_symbols !=0 and RandOrd==0:
        #print(symbols[random.randint(0, len(symbols)-1)], end = "")
        password = password + symbols[random.randint(0, len(symbols)-1)]
        nr_symbols = nr_symbols - 1

      if nr_numbers != 0 and RandOrd==1:
        #print(numbers[random.randint(0, len(numbers)-1)], end = "")
        password = password + numbers[random.randint(0, len(numbers)-1)]
        nr_numbers -= 1

      if nr_letters != 0 and RandOrd==2:
        #print(letters[random.randint(0, len(letters)-1)], end = "")
        password = password + letters[random.randint(0, len(letters)-1)]
        nr_letters -= 1

    return(password)
