# Comment
# Edit in main

import random
password = ''

while True:
    password_length = int(input("Length of password: "))
    if 0 < password_length < 50:
        break

for i in range(password_length):
    random_integer = random.randint(33, 126)
    password += chr(random_integer)

print(password)
