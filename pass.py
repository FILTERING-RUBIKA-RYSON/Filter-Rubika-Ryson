import string
import random
import string
import random


def password(size=8, chars=string.ascii_letters + string.digits +
             string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(password(int(input(' Code Filtering Random 1 ? '))))
print ("")
import string
import random


def password(size=8, chars=string.ascii_letters + string.digits +
             string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(password(int(input(' Code Filtering 2 ? '))))
print("")
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
import string
import random


def password(size=8, chars=string.ascii_letters + string.digits +
             string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(password(int(input(' Code Filtering 3 ? '))))
print ("")