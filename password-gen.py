# will use string.ascii_letter , string.digits , string.punctuation
# shuffle and generate the password
import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

length = int(input(Fore.CYAN+"Enter the password length: "))
characters = string.digits + string.ascii_letters + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print(Fore.GREEN+ Style.BRIGHT + f"\nYour Generated Password is : {password}")