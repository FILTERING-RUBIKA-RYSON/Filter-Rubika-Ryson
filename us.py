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
print(Fore.RED+" "+" report username")
sleep(2.0)
print("\n")
sleep(2.0)
print("\n"*80)
Sdf = """
 telesm server """
for i in Sdf:
  sleep(0.02)
  print(i,end='',flush=True)
print()
print(Fore.RED+" for you ")
sleep(2.1)
print()
def random_string_genera_variable_size(min_size, max_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))
chars = string.ascii_letters + string.punctuation

print("     "+Fore.YELLOW+'reporter account—>> ', random_string_genera_variable_size(6, 24, chars))
print()
time.sleep(1)
print ()
