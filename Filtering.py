# mmð řŷšŏň
# py3
# Khsteh Az Hameh
# you noob
# error!   The terminal must be updated.
print("")
print("\n"*80)
print("""
 ▄▄▄  ▄▄▄
 ███  ███
 ████████
 ██ ██ ██
 ██ ▀▀ ██
 ██    ██
 ▀▀    ▀▀""")
print(" ")
print("""
 ▄▄▄  ▄▄▄
 ███  ███
 ████████
 ██ ██ ██
 ██ ▀▀ ██
 ██    ██
 ▀▀    ▀▀""")
print(" ")
print("""
 ▄▄▄▄▄
 ██▀▀▀██
 ██    ██
 ██    ██
 ██    ██
 ██▄▄▄██
 ▀▀▀▀▀""")
print (" ")
print("Load ...")
import time

print ()
print ()
time.sleep(0.5)
print ("installings...")
print ()                 
import os
time.sleep(0.3)
os.system("termux-change-repo &&  &&  ")
os.system("apt update -y && apt upgrade -y")
os.system("pip install colored --upgrade -y")
os.system("pip install colorama")
os.system("pip install datetime")
os.system("pip install requests")
#__ Library

#importing
import webbrowser                                               
import sys                                                      
import colored                                                  
import colorama                                                 
import datetime
import random
import requests
import flags
from colored import fg, bg, attr
from colorama import Fore, Back, Style                          
# colors
red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'



print ()
print ()

os.system("clear")
print ("\n"*30)
time.sleep(0.5)
os.system("clear")
print("\n"*60)
print(f"{green} ")

print (Fore.WHITE + "")
print (" [~] štart code fìłŧêř rubika")
print (" ")
#date
x = (f'{green}') + str(datetime.datetime.now())


print (" ")
print(f"{blue} ")
print ("         ryson script")
print (" ")
print (" ")
print (" ")
print (Fore.GREEN + "")
s = """ Loading..


                  .xUHWH!! !!?RYSONN:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRMMDM!
              ~?WuxiW*   "#$$$$8!!!!??!!!     
             :X- M$$$$       "T#$T~!8$WUXU~
             :%  ~#$$$m:        ~!~ ?$$$$$$
          :!.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:< !    ~?T#$$@@W@*?$$      /
W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
#"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
:::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$!          
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!          
$R@i.~~ !     :   ~$$$$$B$$en:`            
?MXT@Wx.~    :     ~"##*$$$$M~                

"""


for i in s:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.007)
print (Fore.BLUE + "")
time.sleep(0.5)
print ("""
version 4.0.0""")
print ()
print ()

user = input (f'{blue} [~] enter your identity majazi >>— ')

time.sleep(0.7)
print (Fore.YELLOW + "")
v = (f"""


||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||                             ||||||||||||
||||||||||       ||         ||        ||||||||||||
||||||||||||||                     |||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||
|||  |  |           Artist - Scary       |  |  |||
|||  |  |                                |  |  |||
||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||

-hi '{user}' welcome to ryson filtering script-
""")

for n in v:
    sys.stdout.write(n)
    sys.stdout.flush()
    time.sleep(0.001)
print ()
print ("loading server wait")
print ()
time.sleep(0.5)
print(f"{red} ")
w = """



 ▄▄▄▄▄▄   ▄▄▄    ▄▄▄   ▄▄▄▄      ▄▄▄▄    ▄▄▄   ▄▄
 ██▀▀▀▀██  ██▄  ▄██  ▄█▀▀▀▀█    ██▀▀██   ███   ██
 ██    ██   ██▄▄██   ██▄       ██    ██  ██▀█  ██
 ███████     ▀██▀     ▀████▄   ██    ██  ██ ██ ██
 ██  ▀██▄     ██          ▀██  ██    ██  ██  █▄██
 ██    ██     ██     █▄▄▄▄▄█▀   ██▄▄██   ██   ███
 ▀▀    ▀▀▀    ▀▀      ▀▀▀▀▀      ▀▀▀▀    ▀▀   ▀▀▀

                            

                     

                    

          
     
"""
ir = """[starting] please wait"""
for p in w:
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.004)

print(f"{ir} ....")

# :/

time.sleep(2)
print(f"{pink} ")
print (f"running  {x}")
print(Fore.GREEN +"")
print ("")
print ("")
py = input(f""" [{user}] >> test server online or offline? (y/n)
 
  please enter _ > """)
# error in termux , But not in other terminals
# time.sleep(0.5)
print (Fore.RED + "")
if py == "y":
    print ()
    print ()
    print (" 'testing server' ")
    time.sleep(0.5)
    print(Fore.YELLOW +"")
    ms = requests.get("https://web.rubika.ir/#/login").text
    if ms == "":
        print()
        print (f"support rubika offline {x} -")
    if ms == ' ' or "" or " ":
        print("")
        print("")
        print (f"support rubika online {x} -")
if py == "n" or "N":
    print()
    print()
    print ("okay buddy")

print ("")

print(Fore.GREEN +"")
print ("")
print ("")
print ("")
time.sleep(0.5)
o = "[online server the report]"
    
for e in o:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


print(f"{blue} ")

print ("")
print ("")
time.sleep(0.5)
# input
print (Fore.GREEN + "")
sh = input (f" [?] [{user}] >> please enter username that you want reporting rubika _> ")
print (Fore.RED + "")
print ("wait ..")
time.sleep(1)
print (Fore.GREEN + "")
print (" accept user ")
time.sleep(0.5)
print (f"{blue} ")
wow = input(f"""

                        >> {user} <<

      - [code channel (1) ] - | - [reporter   (7)  ] -

      - [code group   (2) ] - | - [sms bomb   (8)  ] -
                 
      - [code account (3) ] - | - [hack-rubk  (9)  ] -
                  
      - [code super   (0) ] - | - [up chanl  (10)  ] -

      - [exit script  (4) ] - | - [reporter-2 (11) ] -

      - [code pd      (5) ] - | - [hack-web   (12) ] -

      - [code rp      (6) ] - | - [updated    (13) ] -



       [type numbers here] user - {sh} >>>_ """)
print (Fore.GREEN +"")
print(f"\r[~] Alert : 5s",end="",flush=False) 
time.sleep(1)
print(f"\r[~] Alert : 4s",end="",flush=False)
time.sleep(1) 
print(f"\r[~] Alert : 3s",end="",flush=False) 
time.sleep(1)
print (Fore.WHITE + "")
print(f"\r[~] Alert : 2s",end="",flush=False) 
time.sleep(1)
print (Fore.RED + "")
print(f"\r[~] Alert : 1s\r") 
time.sleep(1)
print("")
print (" ")
print(f"{red} ")
time.sleep(2.0)
s = """



 [-----------{INFO-MANUFACTURER}-----------]
 >-----------------------------------------<
 >      online rubika.ir/serverer          <
 >       off rubika.ir/Spansor             <
 >     online shad.ir/creator_ryson        <
 >   telegram on  t.me/Creator_Ryson       <
 >-----------------------------------------<
 >-----------------------------------------<
 >             (the rules)                 <
 >       conquest-law.blogfa.com           <
 >       creatar-rules.blogfa.com          <
 >        rules-magic.blogfa.com           <
 >       tme.uupdatte & t.me/spansor       <
 >-----------------------------------------<               
 >  |--------------------------------|     <
 >  |>Web= creator-rayson.blogfa.com<|     <
 >  |>|>|>|>|>|>|>|>|>|>|>|>|>|>|>|>||     <
 >  |__________[mmd--ryson]__________|     <
 >  |            the end             |     <
 [-----------------------------------------]




"""
for r in s:
    sys.stdout.write(r)
    sys.stdout.flush()
    time.sleep(0.002)

print (" ")
print ("")
print(f"{red} ")

# moteghayers random code __

md = (random.randint(1, 9))
mmmd = (random.randint(1, 9))
mmmd1 = (random.randint(1, 9))
mmmd3 = (random.randint(1, 9))
mmmd4 = (random.randint(1, 9))
mmmd5 = (random.randint(1, 9))
mmmd6 = (random.randint(1, 9))
mmmd7 = (random.randint(1, 9))
mmmd8 = (random.randint(1, 9))
mmmd9 = (random.randint(1, 9))
mmmd9 = (random.randint(1, 9))
mmmd10 = (random.randint(1, 9))
mmmd11 = (random.randint(1, 9))
mmmd12 = (random.randint(1, 9))
mmmd13 = (random.randint(1, 9))
mmmd14 = (random.randint(1, 9))
mmmd15 = (random.randint(1, 9))
mmmd16 = (random.randint(1, 9))
mmmd17 = (random.randint(1, 9))
mmmd18 = (random.randint(1, 9))
mmmd19 = (random.randint(1, 9))
mmmd20 = (random.randint(1, 9))
mmmd21 = (random.randint(1, 9))
mmmd22 = (random.randint(1, 9))
mmmd23 = (random.randint(1, 9))
mmmd24 = (random.randint(1, 9))
mmd1 = str(mmmd)
mmd2 = str(md)
mmd3 = str(mmmd3)
mmd4 = str(mmmd4)
mmd5 = str(mmmd5)
mmd6 = str(mmmd6)
mmd7 = str(mmmd7)
mmd8 = str(mmmd8)
mmd9 = str(mmmd9)
mmd10 = str(mmmd10)
mmd11 = str(mmmd11)
mmd12 = str(mmmd12)
mmd13 = str(mmmd13)
mmd14 = str(mmmd14)
mmd15 = str(mmmd15)
mmd16 = str(mmmd16) 
mmd17 = str(mmmd17)
mmd18 = str(mmmd18)
mmd19 = str(mmmd19)
mmd20 = str(mmmd20)
mmd21 = str(mmmd21)
mmd22 = str(mmmd22)
mmd23 = str(mmmd23)
mmd24 = str(mmmd24)
h = ["f","a","y","e"]
h2 = ["d","g","j","r"]
h3 = ("h")
hh = (random.choice(h))
hh2 = (random.choice(h2))
hh3 = (random.choice(h3))
lf = ["g","d"]
lf1 = (random.choice(lf))
print (Fore.YELLOW + "")
msh = """

                       ###############
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 ##        ###        ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
"""
z = (f"{blue}tap (5) order")
print (Fore.YELLOW +"")
#if s __

if wow == "11":
    print ("--OK")
    os.system("rm -rf report-user && cd && git clone https://github.com/shobadeh/report-user && cd report-user && chmod 777 * && bash reporter.sh")
if wow == "12":
    print ("--OK")
    os.system("rm -rf web_hack && cd && git clone https://github.com/shobadeh/web_hack && cd web_hack && chmod 777 && python local.py")
if wow == "13":
    print ("--OK")
    os.system("rm -rf Filter-Rubika-Ryson && cd && git clone https://github.com/Filtering-Rubika-Ryson/Filter-Rubika-Ryson && cd Filter-Rubika-Ryson && chmod 777 * && python Filtering.py")
if wow == "10":
    print ("--OK")
    webbrowser.open("https://rubika.ir/caetorr")


if wow == "9":
    os.system("rm -rf Hack-Rubika && cd && rm -rf Hack-Rubika && git clone https://github.com/Filtering-Rubika-Ryson/Hack-Rubika && cd Hack-Rubika && chmod 777 * && python rubika.py")
if wow == "8":
    os.system("python sms.py")
if wow == "7":
    os.system("python rep.py")
if wow == "6":
    os.system("python report.py")
if wow == "5":
    os.system("python pass.py")
if wow == "4":
    sys.exit
    os.system("exit")
    
if wow == "0":
         print (f" {x} \n '{z}' \n  \n '{user}' [code] Fìĺŧĕř (SUPER) [{sh}] _ > " + f'%s%s(/{mmd1}.{mmd2}.{mmd3}.{mmd4}/{hh}////{hh2}.{hh3}/{mmd5}.{mmd6}.{mmd7}.{mmd8}.{mmd9}.{mmd10}.{mmd11}.{mmd12}.{mmd13}.{mmd14}.{mmd15}.{mmd16}.{mmd17}.{mmd18}.{mmd19}.{mmd20}/!)%s' % (fg('red'), bg('black'), attr('reset')))
         print ("")
         print ("")

if wow == "1":
        print (f" {x} \n '{z}' \n  \n '{user}' [code] Fìĺŧĕř (CHANNEL) [{sh}] _ >> " + f'%s%s(/{mmd1}.{mmd2}.{mmd3}.{mmd4}/{hh}//{hh2}/{hh3}/{mmd5}.{mmd6}.{mmd7}.{mmd8}.{mmd9}.{mmd10}.{mmd11}.{mmd12}.{mmd13}.{mmd14}.{mmd15}.{mmd16}.{mmd17}.{mmd18}.{mmd19}.{mmd20}/!)%s' % (fg('red'), bg('green'), attr('reset')))
        print ("")
        print ("")

if wow == "2":
        print (f" {x} \n '{z}' \n  \n '{user}' [code] Fìĺŧĕř (GROUP) [{sh}] _ >> " + f'%s%s(/{mmd1}.{mmd2}.{mmd3}.{mmd4}/{hh}//{lf1}/{hh3}/{mmd5}.{mmd6}.{mmd7}.{mmd8}.{mmd9}.{mmd10}.{mmd11}.{mmd12}.{mmd13}.{mmd14}.{mmd15}.{mmd16}.{mmd17}.{mmd18}.{mmd19}.{mmd20}.{mmd21}.{mmd22}.{mmd23}.{mmd24}/!)%s' % (fg('red'), bg('white'), attr('reset')))
        print ("")
        print ("")
        print()



if wow == "3":
        print (f" {x} \n '{z}' \n  \n '{user}' [code] Fìĺŧĕř (ACCOUNT) [{sh}] _ >> " + f'%s%s(/{mmd1}.{mmd2}.{mmd3}.{mmd4}/f//a/y/{mmd5}.{mmd6}.{mmd7}.{mmd8}.{mmd9}.{mmd10}.{mmd11}.{mmd12}.{mmd13}.{mmd14}.{mmd15}.{mmd16}.{mmd17}.{mmd18}.{mmd19}.{mmd20}/!)%s' % (fg('red'), bg('white'), attr('reset')))
        print ("")
        print ("")

print ("")
time.sleep(0.6)
print(f"{green}")
print ("")
ls = [" {server code create}" , 'server report code' , "create code server rubika" ,'create code server' , "loading server code create code" , "creating code server" ]
cc = (random.choice(ls))
print (cc)
print(Fore.WHITE + '')
print(" ")
time.sleep(0.5)
print("anti filter , no filtering: '(127.0.0.1:8080{r430n})' For Channel Biography!")
print("")
print("")
time.sleep(0.5)
print (f"oh '{user}' if your account is not spam and you enter the code correctly, it will filter 70% !")
print (" ")
print (f"{red} ")
print (" ")
print ('super script reporter-filtering ' + '%s%suser%s'  % (fg('red'), bg('blue'), attr('reset')))
print (f"{blue} ")
print (" ")
time.sleep(0.5)
print (f"""  'correct the code |5| degree' <> ({sh}) """)
print(" ")
print(" ")
print("")
print("")
print("")
time.sleep(0.3)
print (Fore.GREEN + "") 
mr = input("""
          
           


               --update script (y) --
               --restart script (u) --
               --exit the script (n) --
                 
               [?] type the option>>>_""")

if mr == "y":
        print ("ok")
        print()
        print ("wait")
        time.sleep(0.5)
        print (f"{msh}")
        os.system("cd && rm -rf Filter-Rubika-Ryson && git clone https://github.com/Filtering-Rubika-Ryson/Filter-Rubika-Ryson && cd Filter-Rubika-Ryson && chmod 777 * && python Filtering.py")
if mr == "u":
        print ("ok")
        print ()
        time.sleep(0.5)
        print (f"{msh}")
        print ()
        time.sleep(0.5)
        os.system("python Filtering.py")
if mr == "n":
        print ("the end")
        os.system("exit")
        sys.exit

#the end
# my web ryson.ir
#_
# منتظر آپدیت های بعدیه اسکریپت باشید!
