import random



print("Welcome to password generator")

chars = "abcdefghijklmnoprstuwyxzABCDEFGHIJKLMNOPRSTUWYXZ0123456789.,:'"

length = int(input("Lenght of the password: "))


password = ''

for tmp in range(length):
    password += random.choice(chars)

print(password)


