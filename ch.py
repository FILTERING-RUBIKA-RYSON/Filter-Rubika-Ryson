import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
print("")
print(Fore.RED+" "+" Loading....")
sleep(2.0)
print("\n")
print(Fore.GREEN+"""
    coder..
  """)
sleep(2.0)
print("\n"*90)
print("""
  Load . . .
  """)
Dmo = """

creater codings
"""
for i in Dmo:
  sleep(0.02)
  print(i,end='',flush=True)
print()
sleep(2.1)
def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
chars = string.ascii_letters + string.punctuation
size = 28
print("#  #  #  #")
print(Fore.RED+'   reporter channel >> ',random_string_generator(size, chars))
print("#  #  #  #")
time.sleep(1)
print ()
