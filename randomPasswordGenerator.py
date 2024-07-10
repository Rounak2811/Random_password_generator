import random
import string
from tkinter import *

# Function to generate random password
def generate_password(length, use_letters, use_numbers, use_special_chars):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# GUI setup
def generate():
    length_str = length_entry.get()
    if length_str.isdigit():
        length = int(length_str)
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_special_chars = special_chars_var.get()
        password = generate_password(length, use_letters, use_numbers, use_special_chars)
        result_label.config(text=password)
    else:
        result_label.config(text="Invalid input: Please enter a valid integer for password length.")

root = Tk()
root.title("Random Password Generator")

# Input for password length
length_label = Label(root, text="Password Length:")
length_label.pack()
length_entry = Entry(root)
length_entry.pack()

# Checkbox for including letters
letters_var = BooleanVar()
letters_check = Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack()

# Checkbox for including numbers
numbers_var = BooleanVar()
numbers_check = Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

# Checkbox for including special characters
special_chars_var = BooleanVar()
special_chars_check = Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Button to generate password
generate_button = Button(root, text="Generate Password", command=generate)
generate_button.pack()

# Label to display the generated password
result_label = Label(root, text="")
result_label.pack()

root.mainloop()