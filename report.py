import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
###########


print("\n"*10)

soheil = """
     \033[41m[1]\33[1;0m   group ->_
     \033[41m[2]\33[1;0m   account->_
     \033[41m[3]\33[1;0m   channel->_
     \033[41m[4]\33[1;0m   bye bye  ->_
"""
for i in soheil:
	sleep(0.05)
	print(i,end='',flush=True)
print()
################   Inputs
shah = int(input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1; Type number >>>_ \033[93m"+Fore.RED+""))
################################## Grop
if(str(shah) == "1"):
  os.system("python gp.py")
###############################     User 
if(str(shah) == "2"):
  os.system("python us.py")
  #COD Filteri Chanel
if(str(shah) == "3"):
  os.system("python ch.py")
##########
if(str(shah) == "4"):
  sys.exit()
