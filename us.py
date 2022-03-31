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
 Im Ostoreh """
for i in Sdf:
  sleep(0.02)
  print(i,end='',flush=True)
print()
print(Fore.RED+" Rumika's random filtering code please use correctly: OK PlAY FIL ")
sleep(2.1)
print()
def random_string_genera_variable_size(min_size, max_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))
chars = string.ascii_letters + string.punctuation

print("     "+Fore.YELLOW+'reporter account—>> ', random_string_genera_variable_size(6, 24, chars))
print()
sleep(1.0)
print(Fore.GREEN+""" OK """)
input()
