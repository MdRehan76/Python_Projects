import random
import string

char_values = string.ascii_letters + string.punctuation + string.digits
pass_len = int(input("Enter the length of password = "))

password = ""

for i in range(0,pass_len):
    password += random.choice(char_valves)

print(f"Random Password : {password}")

