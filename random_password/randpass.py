import random
import string



print("Hello, Welcome to Password generator!")

length = int(input("\nEnter The Length Of Password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)

password = ''.join(temp)

print(password)