#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password1 = ""
selected_letters = random.sample(letters, nr_letters)
selected_symbols = random.sample(symbols, nr_symbols)
selected_numbers = random.sample(numbers, nr_numbers)

for letter in selected_letters:
  password1 += letter
for symbol in selected_symbols:
  password1 += symbol
for number in selected_numbers:
  password1 += number

print(f"Your easy password generated is {password1}\n")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

selected_characters = []

selected_letters = random.sample(letters, nr_letters)
selected_symbols = random.sample(symbols, nr_symbols)
selected_numbers = random.sample(numbers, nr_numbers)

for letter in selected_letters:
  selected_characters.append(letter)
for symbol in selected_symbols:
  selected_characters.append(symbol)
for number in selected_numbers:
  selected_characters.append(number)

password2 = ""
n = len(selected_characters)

randomized_selected_characters = random.sample(selected_characters, n)

for character in randomized_selected_characters:
  password2 += character
  
print(f"Your hard password generated is {password2}\n")