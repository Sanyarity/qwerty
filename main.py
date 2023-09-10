import random

name = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Введите длину пароля:"))
password = ""
for i in range(pass_len):
    password += random.choice(name)
print(password) 
1