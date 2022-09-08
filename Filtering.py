#!/bin/python
from os import system; import sys, string; from time import sleep, time; from random import choice, randint; import marshal, hashlib, base64, platform
typeSystem, typeSys = platform.platform(), platform.system()
try:
    if 'linux'.lower() in typeSys.lower(): system('clear')
    else: system('cls')
except: pass
green, red, blue, pink, yellow, darkblue, white = "\033[32m", "\033[31m", "\033[36m", "\033[35m", "\033[93m", "\033[34m", "\033[00m"; mark, mark1, mark2 = '', '', ''
try: from colored import fg, bg, attr # bg for background and attr for reset color !
except ModuleNotFoundError:
    system('pip3 install colored')
    from colored import fg, bg, attr
try: from requests import post, get
except ModuleNotFoundError:
    system("pip3 install requests")
    from requests import post, get
try: from pyfiglet import figlet_format
except ModuleNotFoundError:
    system("pip install pyfiglet")
    from pyfiglet import figlet_format
try: from webbrowser import open as opn
except ModuleNotFoundError:
    system("pip install webbrowser")
    from webbrowser import open as opn
try: from datetime import datetime
except ModuleNotFoundError:
    system("pip install datetime")
    from datetime import datetime
try:
    if 'linux' in typeSys.lower(): system("apt-get install sox")
except: pass
try:
    if 'Linux' in typeSys: system("clear")
    else: system('cls')
except: pass
if 'Windows'.lower() in typeSys.lower():
    print('\n\n\n\n\n\033[31m[*] \033[92mScript is for Linux. if for Windows is not strong !\n')
    sleep(1)
try:
    if 'Linux' in typeSys:
        system("clear")
    else:
        system('cls')
except:
    pass
the : str = (datetime.today())
try:
    if 'Linux' in typeSys:
        system('date')
    else:
        system('cls')
except: pass
if 'Windows' in typeSys or 'Mac' in typeSys:
    date : str = get('https://messengerg2c37.iranlms.ir/')
    print('\n\033[92m'+date.headers['date'])
    sleep(1)
else:
    pass
sleep(0.5); print ("\n"*60)
print (F"{darkblue}\nversion 5.0.2 | %s%spower reporter%s" % (fg('blue'), bg('white'), attr('reset')))
user = input (f'{red}\n[ryson@terminal:~#] {blue}enter your identity {yellow}majazi {blue}──╼ ❯❯❯ {green}').strip()
while user == '':
    print('\n\033[31m[!] \033[35mplease enter your name\n')
    user = input (f'{red}\n[ryson@terminal:~#] {blue}enter your identity {yellow}majazi {blue}──╼ ❯❯❯ {green}').strip()
sleep(1)
sh = input (f"\n\n{green}[?] {yellow}[root@{user}:~#]{green} >> {darkblue}please enter username for reporting messengers {yellow}[@username] {darkblue}──╼ ❯❯❯ {pink}").strip()
while sh == '':
    print('\n\033[31m[!] \033[35mplease enter username target.\n')
    sh = input (f"{green}[?] {yellow}[root@{user}:~#]{green} >> {darkblue}please enter username for reporting messengers {yellow}[@username] {darkblue}──╼ ❯❯❯ {pink}").strip()
sleep(2)
try:
    if 'Linux' in typeSys: system("clear")
    else: system('cls')
except: pass
print('\n')
class run:
    def codes() -> str:
        codes = ""
        choices = [*"abcdefghijklmnopqrstvwxyz1234567890"]
        for i in range(14): codes += choice(choices)
        return codes
    @staticmethod # dr for method function
    def base64() -> str:
        codes = ""
        choices = [*"abcdefghijklmnopqrstvwxyz1234567890*&^%$#@==--_]{/|':;?,<>`~"]
        for i in range(32): codes += choice(choices)
        return codes
    @staticmethod
    def main():
        s : list = [f"""
        {green}

                        .xUHWH!! !!?RYSONN:.
                        .X*#M@$!!  !X!M$$$$$$WWx:.
                    :!!!!!!?H! :!$!$$$$$$$$$$8X:
                    !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                    :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                    ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                    !:~~~ .:!M"T#$$$$WX??#MRMMDM!
                {blue}      ~?WuxiW*   "#$$$$8!!!!??!!!
                    :X- M$$$$       "T#$T~!8$WUXU~
                    :%  ~#$$$m:        ~!~ ?$$$$$$
                :!.-   ~T$$$$8xx.  .xWW- ~""##*"
        .....   -~~:< !    ~?T#$$@@W@*?$$      /
        W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
        #"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
        :::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~{darkblue}
        .~~   :X@!.-~   ?@WTWo("*$$$W$TH$!
        Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
        $R@i.~~ !     :   ~$$$$$B$$en:`
        ?MXT@Wx.~    :     ~"##*$$$$M~

        """ , F"""{yellow}
        ||||||||||||||||||||||||||||||||||||||||||||||||||
        |||||||||                             ||||||||||||
        ||||||||||       ||         ||        ||||||||||||
        ||||||||||||||                     |||||||||||||||
        ||||||||||||||||||||||||||||||||||||||||||||||||||
        |||  |  |          {green} Artist - Scary {yellow}      |  |  |||
        |||  |  |                                |  |  |||
        ||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||||||||||||||||||||||||||||||||||||||||||||||||
        """, F"""{green}
    \'  ______      _____   _____      ____     ______     ________    _____   ______
        (   __ \    / ___/  (  __ \    / __ \   (   __ \   (___  ___)  / ___/  (   __ |
        ) (__) )  ( (__     ) )_) )  / /  \ \   ) (__) )      ) )    ( (__     ) (__) )
        (    __/    ) __)   (  ___/  ( ()  () ) (    __/      ( (      ) __)   (    __/
        ) \ \  _  ( (       ) )     ( ()  () )  ) \ \  _      ) )    ( (       ) \ \  _
        ( ( \ \_))  \ \___  ( (       \ \__/ /  ( ( \ \_))    ( (      \ \___  ( ( \ \_)) {blue}
        )_) \__/    \____\ /__\       \____/    )_) \__/     /__\      \____\  )_) \__/ \'
        """ , F"""{green}

        ###### # #      ##### ###### #####  # #    #  ####
        #      # #        #   #      #    # # ##   # #    #
        #####  # #        #   #####  #    # # # #  # #
        #      # #        #   #      #####  # #  # # #  ### {darkblue}
        #      # #        #   #      #   #  # #   ## #    #
        #      # ######   #   ###### #    # # #    #  ####
        """ , """\033[92m
        _____________ ________ ______ __________  /______ ________
        __  ___/_  _ \___  __ \_  __ \__  ___/_  __/_  _ \__  ___/
        _  /    /  __/__  /_/ // /_/ /_  /    / /_  /  __/_  /\033[93m
        /_/     \___/ _  .___/ \____/ /_/     \__/  \___/ /_/
                    /_/
        """ , F"""{blue}
                                _
        _ __ ___ _ __   ___  _ __| |_ ___ _ __
        | '__/ _ \ '_ \ / _ \| '__| __/ _ \ '__|
        | | |  __/ |_) | (_) | |  | ||  __/ |
        |_|  \___| .__/ \___/|_|   \__\___|_|   {pink}
                |_|

        """, F"""{yellow}
        ########  ######## ########   #######  ########  ######## ######## ########
        ##     ## ##       ##     ## ##     ## ##     ##    ##    ##       ##     ##
        ##     ## ##       ##     ## ##     ## ##     ##    ##    ##       ##     ##
        ########  ######   ########  ##     ## ########     ##    ######   ########
        ##   ##   ##       ##        ##     ## ##   ##      ##    ##       ##   ##
        ##    ##  ##       ##        ##     ## ##    ##     ##    ##       ##    ##  {white}
        ##     ## ######## ##         #######  ##     ##    ##    ######## ##     ##
        """ , F"""{white}

                                        _
        ____ _____ ____   ___   ____ _| |_ _____  ____
        / ___| ___ |  _ \ / _ \ / ___(_   _| ___ |/ ___)
        | |   | ____| |_| | |_| | |     | |_| ____| | {green}
        |_|   |_____|  __/ \___/|_|      \__|_____|_|
                    |_|
        """]
        banner = (choice(s))
        try:
            if 'Linux' in typeSys: system('date')
            else: system('cls')
        except:
            pass
        [(print(i, flush=True, end=''), sleep(0.007)), for i in banner]; sleep(1)
    def insert():
        wow : str = input(f"""\n\n
                     {yellow}[ {pink}{the} {yellow}]

                        \033[35m>>> \033[93m'{green}{user}\033[93m' \033[35m<<<\033[36m


       __________________________________________________
        |- [super code   {green}(0){blue} ] - | - [reporter     {green}(8){blue} ] -|
        |                        |                        |
        |- [code channel {green}(1){blue} ] - | - [hack-rubk    {green}(9){blue} ] -|
        |                        |                        |
        |- [code group   {green}(2){blue} ] - | - [up chanl    {green}(10){blue} ] -|
        |                        |                        |
        |- [code account {green}(3){blue} ] - | - [sms bomb    {green}(11){blue} ] -|
        |                        |                        |
        |- [storng code  {green}(4){blue} ] - | - [hack-web    {green}(12){blue} ] -|
        |                        |                        |
        |- [code pd      {green}(5){blue} ] - | - [update      {green}(13){blue} ] -|                                    
        |                        |                        |
        |- [code rp      {green}(6){blue} ] - | - [anti filter {green}(14){blue} ] -|
        |                        |                        |
        |- [anti report  {green}(7){blue} ] - | - [exit script {green}(15){blue} ] -|
        |                                                 |
        |- [robot rubika {green}(16){blue}] - | - [test support {green}(18){blue}] -|
        |                                                 |
        |- [spam suport {green}(17){blue} ] - | - [info url    {green}(19){blue} ] -|
        |                                                 |
        |-     [information manufacturer \033[92m(\033[36m00\033[92m)\033[36m ]          -|
        |                                                 |
        |-     [html source website      \033[92m(\033[36m20\033[92m) \033[36m]          -|
        |                                                 |
        |-     \033[31m[\033[95mnew version code \033[35m-       \033[92m(\033[36m21\033[92m) \033[31m]\033[36m          -|
        |                                                 |
        |-     \033[31m[\033[95mnew version code \033[35m-       \033[92m(\033[36m22\033[92m) \033[31m]\033[36m          -|
        |                                                 |
        |-     \033[31m[          \033[95m%sclear%s          \033[35m(\033[92m99\033[35m)\033[31m ]\033[36m
        ___________________________________________________"""  % (bg('white'), attr('reset')) + f"""



        \033[31m[?] {pink} [type numbers here] user - {red}[{sh}]{pink} ──╼ ❯❯❯ {yellow}""").strip()
        if wow == '':
            print('\n\033[31m[!] \033[35mplease enter a number method.')
            sleep(1)
            try:
                if 'Linux' in typeSys:
                    system('clear')
                else:
                    system('cls')
            except:
                pass
            run.insert()
        if wow == '15':
            quit()
        if wow != '99':
            sleep(0.5)
            print(f"\n\n{yellow}\r [new] = '<Pro>' price: $10 = {red}($0) {yellow}-! ",end="",flush=False)
            sleep(2)
            print("\r [*]                                         ",end="",flush=False)
            print ('\n\n')
            print(f"\r{red}[~] {green}ălert {yellow}> {pink}5s",end="",flush=False)
            sleep(1)
            print(f"\r{red}[~] {green}ălert {yellow}>> {pink}4s",end="",flush=False)
            sleep(1)
            print(f"\r{red}[~] {green}ălert {yellow}>>> {pink}3s",end="",flush=False)
            sleep(1)
            print(f"\r{red}[~] {green}ălert {yellow}>>>> {pink}2s",end="",flush=False)
            sleep(1)
            print(f"\r{red}[~] {green}ălert {yellow}>>>>> {pink}1s",end="",flush=False)
            sleep(0.5)
        try:
            if 'Linux' in typeSys:
                system('clear')
            else:
                system('cls')
        except:
            pass
        if wow != '99':
            sleep(1)
        h, h2, h3 = ["/y//d/f/","/f//d/","/d//f/h/","/f//a/y/","/e////f.h/","/f/h.u//"], ["/f////g.h/","/g//d/","/f/h.g//","/r//g/h"], 'h'
        hh, hh2, hh3, lf = (choice(h)), (choice(h2)), (choice(h3)), ["g","d"]; lf1 : str = (choice(lf))
        pl, pu, pe = ["f","¥","€","$","£","¢","&"], ["f","¥","€","$","£","¢","&","ß","ę","€","$","£","¢","&","₹","₱","†"], ["ß","ę","€","$","£","¢","&","₹","₱","†"]
        pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8 = (choice(pl)), (choice(pl)), (choice(pl)), (choice(pl)), (choice(pl)), (choice(pe)), (choice(pu))
        oh : str = (f"\033[20;37moh \033[36m'{user}'\033[20;37m if your account is not spam and you to hit the code correctly, it will filter 70% !"); port : str = (f"{blue}no report"); ping : str = ("\033[20:37m] '(127.0.0.1:8080{r430n})'"); y : str = (f"{blue}tap \033[31m[1] \033[36morder code"); z : str = (f"{blue}tap \033[31m[2]\033[36m order"); tar : str  = (f"\033[31mtarget: \033[0m['{sh}']"); ls : list = [f"{green} [server code create]" , f'{green}server report code' , f"{green}create code server rubika" ,f'{green}create code server' , f"{green}loading server code create code" , f"{green}creating code server" ]; cc : str = (choice(ls))
        sleep(0.5)
        if wow == '99':
            run.insert()
        if wow == "19":
            usrname = input(f" {red}[?] {blue}[{user}]{red} >> {green}url username messenger channel , group \n \n {yellow}[https://t.me/username] {green}please enter {blue}_> {pink}")

            sleep(0.5)
            if '@' in usrname:
                x : str = datetime.now(())
                print("\n\n\033[93menter dont \033[31m'@'\n")
                while '@' in usrname:
                    usrname : str = input(f'\n\033[93mpleas enter do not \033[31m'@' {blue}[https://t.me/username] {pink}')
                sleep(1)
                print ("\n\033[31mloading...\n")
                sleep(1)
            ml : str = get(f"{usrname}")
            if ml.status_code == 200:
                sleep(0.5)
                print (f"\n{blue} [{usrname}] {darkblue}username url found\n")
            elif ml.status_code == 404:
                print (f"\n{blue} [{usrname}] {darkblue}not found url \n")
            elif ml.status_code == 302:
                print (f"\n{blue} [{usrname}] {darkblue}not found url\n")
            else:
                pass
            def info(usrname):
                html = get(f'{usrname}').text
                a = []
                for t in html.split('\n'):
                    if ('<meta property="og:title" content="' in t ):
                        a.append(t.replace('<meta property="og:title" content="','').replace('">', ''))
                    if ('                                   ' in t ):
                        a.append(t.replace('<meta property="og:image" content="','').replace('">', ''))
                    if ('<meta name="twitter:description" content="' in t ):
                        a.append(t.replace('<meta name="twitter:description" content="','').replace('">', ''))
                    if ('<div class="tgme_page_extra">' in t ):
                        a.append(t.replace('<div class="tgme_page_extra">','').replace('</div>', ''))
                        break
                return a
            sleep(0.5)
            print ("\n\033[31[*] \033[36mmname url found:")
            sleep(0.5)
            print (f"\n\033[92minfo \033[31m[{usrname}] = \033[20;37m\n") , print(info(usrname))
            sleep(1)
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == "20":
            sleep(1)
            source : str  = input(f"\n{green}[{x}] | {yellow}enter web site for source html {white}⟩⟩{pink} ")
            rq = get(source).text
            print(F"{white}\n\nsource{pink}:\n\n")
            sleep(1)
            print(F'{red}__________________________')
            print(mark1+rq)
            print(f'\n{red}____________________________\n')
            sleep(2)
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == "18":
            x : str = datetime.now()
            okay : str = input(f"\n\033[36mplease enter url messenger {yellow}[{green}https://rubika.ir{yellow}] {blue}──╼ ❯❯❯ {pink}")
            sleep(0.5)
            print("\033[31m\r 'testing server'  ..",end="",flush=False)
            sleep(1)
            print("\r 'testing server'  ...",end="",flush=False)
            sleep(1)
            print("\r 'testing server'  ....",end="",flush=False)
            sleep(1)
            print("\r 'testing server'  .....",end="",flush=False)
            sleep(1)
            print("\r 'testing server'        ",end="",flush=False)
            sleep(0.8)
            print("\r 'testing server'  .",end="",flush=False)
            sleep(0.9)
            print("\r 'testing server'  .. ",end="",flush=False)
            sleep(0.5)
            print("\r 'testing server'  ...",end="",flush=False)
            sleep(0.7)
            print("\r 'testing server'  ....",end="",flush=False)
            sleep(1)
            print("\r 'testing server'  .....",end="",flush=False)
            sleep(0.7)
            print("\r 'create server'           ",end="",flush=False)
            sleep(0.5)
            ms : str = get(f"\n\033[93m{okay}").text
            if not ms.status_code == 200:
                print (f"\n\033[36msupport offline {darkblue}{x} {red}-")
            else:
                print (f"\n\033[36msupport online {darkblue}{x} {red}-")
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == "17":
            system("cd")
            system("rm -rf spambot")
            system("git clone https://github.com/creatorLOR/spambot")
            system("cd spambot")
            system("chmod +x *")
            system("python reporting.py")
        if wow == "16":
            sleep(0.5)
            try:
                system('git clone https://github.com/shobadeh/rubika-robot')
                system('cd rubika-robot')
            except:
                system('cd | cd rubika-robot')
            system('chmod 777 *')
            system('python bot.py')
        if wow == "14":
            x : str = datetime.now()
            sir : str = input ("\n\033[36musername channel rubika for anti report do not \033[31m'@' , \033[36m] _>>\033[0m] " )
            print ()
            rys = get(f"https://rubika.ir/{sir}")
            if rys.status_code == 200:
                time.sleep(0.5)
                print (f"\n\n{blue}channel found {yellow}@{sir} *")
            elif rys.status_code == 404:
                print (f"\n{blue}not found channel! {yellow}@{sir}")
            elif rys.status_code == 302:
                print (f"\n{blue}not found channel! {yellow}@{sir}")
            else:
                pass
            sleep(1)
            print (f"\n{yellow}{x} \n \n {pink}{port} {green}'@{sir}' \n \n {blue}anti report or filter [for username biography] ——>>>:" + f"\n \n{green}{ping}")
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == "4":
            x : str = (datetime.today())
            sleep(1)
            print (f"{yellow}time: {x} \n \n {blue}{tar} \n\n{green}'{y}' \n  \n {pink}'{user}' {green}[code] (storng) ——>>>>: ")
            sleep(0.5)
            print (f"{blue}\n \n  _______________________ \n \n {red} ")
            codereport = (f"{red}(</*<<f<{pl8}<{pl4}<{pl5}<{pl6}<{pl1}<#<=>#>{pl1}>{pl2}>{pl3}>{pl4}>{pl7}>h>>*/>)\n")
            sleep(1)
            print (codereport)
            sleep(0.5)
            print (f" \n {blue} _______________________ \n")
            sleep(1)
            try:
                with open('target.txt', 'w') as _target_:
                    _target_.write (f'target >> |{tar}|\ndate start >> |{x}|\n\ncode >> |{codereport}|')
                    print (f"\033[20;37minfo target <SAVE> in \033[00;00m{blue}[target.txt]")
            except:
                pass
            sleep(2)
            print (f"\n\n[#] > {oh} <")
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == "8":
            system("cd ~")
            try:
                system("git clone https://github.com/mester-root/rubika-reporter")
            except:
                pass
            system('cd rubika-reporter')
            system("chmod 777 *")
            system("python rubika-reporter.py")
        if wow == "12":
            system("cd $HOME | ~")
            try:
                system("git clone https://github.com/shobadeh/web_hack")
            except:
                pass
            system('cd web_hack')
            system("chmod 777 *")
            system("python local.py")
        if wow == "13":
            system("cd $HOME")
            system("rm -rf Filter-Rubika-Ryson")
            system("cd")
            system("git clone https://github.com/Filtering-Rubika-Ryson/Filter-Rubika-Ryson")
            system("cd Filter-Rubika-Ryson")
            system("chmod 777 *")
            system("python Filtering.py")
        if wow == "10":
            print('\n\033[31m[*] \033[36mjoin to https://rubika.ir/caetor ...\n')
            opn("https://rubika.ir/caetorr/")
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                if 'Linux' in typeSys:
                    system('clear')
                else:
                    system('cls')
                run.insert()
            elif test == '1':
                run.reset()
            else:
                run.reset()
        if wow == "9":
            system("cd")
            try:
                system("git clone https://github.com/Filtering-Rubika-Ryson/Hack-Rubika")
            except:
                system("cd Hack-Rubika")
            system("chmod 777 *")
            system("python rubika.py")
        if wow == "11":
            system("python sms.py")
        if wow == "7":
            system("python rep.py")
        if wow == "6":
            print (f"{oh}\n")
            print ("pls wait..")
            sleep(1)
            system("python report.py")
        if wow == "5":
            print (f"{oh}\n")
            print ("wait..")
            time.sleep(1)
            system("python pass.py")
        if wow == "15":
            quit()
        if wow == "0":
                x : str = (datetime.today())
                print (f"time: {x} \n \n {tar} \n\n'{z}' \n  \n '{user}' [{sh}] Fìĺŧĕř (super) [code:] ~>>>>: ")
                sleep(1)
                codereport1 : str = (f"\n \n %s%s(/{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}{hh}{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}/)%s" % (fg('red'), bg('black'), attr('reset')))
                print (codereport1)
                print ('\n\n')
                sleep(1.5)
                try:
                    with open('target.txt', 'w') as _target_:
                        _target_.write (f'''target >> |{tar}|\ndate start >> |{x}|\n\ncode >> |{codereport1}|''')
                        print (f"\033[20;37minfo target <SAVE> in \033[00;00m{blue}[target.txt]")
                except AttributeError:
                    pass
                except:
                    pass
                sleep(1)
                print (f"\n\n[#] > {oh} <")
                print ('\n\n'+f'{cc}')
                sleep(0.3)
                test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
                if test == '1':
                    try:
                        if 'Linux' in typeSys:
                            system('clear')
                        else:
                            system('cls')
                    except:
                        pass
                    run.insert()
                else:
                    run.reset()
        if wow == "1":
                x : str = (datetime.now())
                print (f"time: {x} \n \n {tar}\n\n'{z}' \n  \n '{user}' [{sh}] Fìĺŧĕř (channel) [code:] ~>>>> ")
                sleep(1)
                codereport2 = (f"\n \n %s%s(/{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}{hh}{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}/)%s" % (fg('red'), bg('green'), attr('reset')))
                print (codereport2)
                print ('\n\n')
                sleep(1.5)
                try:
                    with open('target.txt', 'w+') as _target_:
                        _target_.write (f'''target >> |{tar}|\ndate start >> |{x}|\n\ncode >> |{codereport}|''')
                        print (f"\033[20;37minfo target <SAVE> in \033[00;00m{blue}[target.txt]")
                except:
                    pass
                sleep(1)
                print (f"\n\n[#] > {oh} <")
                print ('\n\n'+f'{cc}')
                test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
                if test == '1':
                    try:
                        if 'Linux' in typeSys:
                            system('clear')
                        else:
                            system('cls')
                    except:
                        pass
                    run.insert()
                else:
                    run.reset()
        if wow == "2":
                x : str = (datetime.now())
                print (f"time: {x} \n \n{tar}\n\n '{z}' \n  \n '{user}' [{sh}] Fìĺŧĕř (group) [code:] ~>>>> ")
                sleep(1)
                codereport3 = (f"\n \n %s%s'(/{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}{hh2}{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}/)'%s" % (fg('red'), bg('white'), attr('reset')))
                print (codereport3)
                print ("\n\n")
                sleep(1.5)
                try:
                    with open('target.txt', 'w') as _target_:
                        _target_.write (f'''target >> |{tar}|\ndate start >> |{x}|\n\ncode >> |{codereport}|''')
                        print (f"\033[20;37minfo target <SAVE> in \033[00;00m{blue}[target.txt]")
                except:
                    pass
                sleep(1)
                print (f"\n\n[#] > {oh} <")
                print ('\n\n'+f'{cc}')
                test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
                if test == '1':
                    try:
                        if 'Linux' in typeSys or 'Mac' in typeSys:
                            system('clear')
                        else:
                            system('cls')
                    except:
                        pass
                    run.insert()
                else:
                    run.reset()
        if wow == "3":
                x : str = (datetime.now())
                print (f"time: {x} \n \n{tar}\n\n'{z}' \n  \n '{user}' [{sh}] Fìĺŧĕř (account) [code:] ~>>>> ")
                sleep(1)
                codereport4 = (f"\n \n %s%s(/{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}{hh}{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}.{randint(1, 9)}/)%s" % (fg('red'), bg('white'), attr('reset')))
                print (codereport4)
                print ('\n\n')
                sleep(1.5)
                try:
                    with open('target.txt', 'w') as _target_:
                        _target_.write (f'''target >> |{tar}|\ndate start >> |{x}|\n\ncode >> |{codereport}|''')
                        print (f"\033[20;37minfo target <SAVE> in \033[00;00m{blue}[target.txt]")
                except:
                    pass
                sleep(1)
                print (f"\n\n[#] > {oh} <")
                print ('\n\n'+f'{cc}')
                test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
                if test == '1':
                    try:
                        if 'Linux' in typeSys:
                            system('clear')
                        else:
                            system('cls')
                    except:
                        pass
                    run.insert()
                else:
                    run.reset()
        if wow == '21':
            print('\n\033[31m[*] \033[36myour code for \033[31m\'filter\' \033[0m[%s] \033[36m:\n' % (user))
            try:
                _code_ : str = run.codes()
                _runing_ = bytes(marshal.dumps(compile(_code_,'Scorpian' , 'exec')))
                _start_ : bytes = _runing_
                _str_ : str = str(_start_)
                _ce_ : str = _str_.replace('b', '')
                _cd_ : str = _ce_.replace('<module>', '')
                _c_ : str = _cd_.replace('Scorpian', '')
                #_cr_ : str = _c_.replace(_c_[0:81], '')
                _cr_ : str = _c_[137:]
                _create_ = str(_cr_)
                sleep(1)
                print('\033[92m_'*30)
                sleep(0.5)
                print('\n%s%s((%s))%s\n' % (fg('blue'), bg('white'), (_create_), attr('reset')))
                sleep(1)
                print('\033[92m_'*30)
                sleep(3)
            except:
                while True:
                    try:
                        _code_ : str = run.codes()
                        _runing_ = bytes(marshal.dumps(compile(_code_,'Scorpian' , 'exec')))
                        _start_ : bytes = _runing_
                        _str_ : str = str(_start_)
                        _ce_ : str = _str_.replace('b', '')
                        _cd_ : str = _ce_.replace('<module>', '')
                        _c_ : str = _cd_.replace('Scorpian', '')
                        #_cr_ : str = _c_.replace(_c_[0:81], '')
                        _cr_ : str = _c_[137:]
                        _create_ = str(_cr_)
                        sleep(1)
                        print('\033[92m_'*30)
                        sleep(0.5)
                        print('\n%s%s((%s))%s\n' % (fg('blue'), bg('white'), (_create_), attr('reset')))
                        sleep(1)
                        print('\033[92m_'*30)
                        sleep(3)
                        break
                    except:
                        pass
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                try:
                    if 'Linux' in typeSys:
                        system('clear')
                    else:
                        system('cls')
                except:
                    pass
                run.insert()
            else:
                run.reset()
        if wow == '22':
            print('\n\033[31m[*] \033[36myour code for \033[31m\'filter\' \033[0m[%s] \033[36m:\n' % (user))
            inline : str = run.base64()
            base64hash = base64.b64encode(hashlib.sha256(inline.encode('utf-8')).digest())
            sha = '\033[31m(\033[35m' + base64hash.decode("utf-8") + '\033[31m)'
            sleep(1)
            print('\033[92m_'*30)
            sleep(0.5)
            print(sha)
            sleep(1)
            print('\033[92m_'*30)
            sleep(3)
            test : str = input('\n\033[31m[?] \033[92m\'0\' \033[36mfor exit and \033[92m\'1\' \033[36mfor panel \033[31m_> \033[20;37m')
            if test == '1':
                if 'Linux' in typeSys:
                    system('clear')
                else:
                    system('cls')
                run.insert()
            elif test == '1':
                run.reset()
            else:
                run.reset()
        if wow == "00":
            s = (f"""


        _________________________________________________
        |>>>-----------------------------------------<<<|
        |>>>-----------------------------------------<<<|
        |>>>         {green}[INFO-MANUFACTURER]{blue}             <<<|
        |>>>—————————————————————————————————————————<<<|
        |>>>              {red}[accounts]{blue}                 <<<|
        |>>>                                         <<<|
        |>>>     _______________________________     <<<|
        |>>>     |                             |     <<<|
        |>>>     |{pink}online{blue}: {green}rubika.ir/PartyBaazi{blue} |     <<<|
        |>>>     |{pink}online{blue}: {green}rubika.ir/antiMMD{blue}    |     <<<|
        |>>>     |{pink}online{blue}: {green}t.me/creator_ryson{blue}   |     <<<|
        |>>>     |{pink}online{blue}: {green}shad.ir/creator_ryson{blue}|     <<<|
        |>>>     |{red}offline{blue}: rubika.ir/serverer  |     <<<|
        |>>>     |{red}offline{blue}: rubika.ir/alerter   |     <<<|
        |>>>     |{red}offline{blue}: rubika.ir/Spansor   |     <<<|
        |>>>     |{red}offline{blue}: rubika.ir/updatte   |     <<<|
        |>>>     |{green}channel{blue}: rubika.ir/caetorr   |     <<<|
        |>>>     |{green}channel{blue}: t.me/uupdatte       |     <<<|
        |>>>     |{green}channel{blue}: t.me/antiweak       |     <<<|
        |>>>     |im:Instagram.com/hazrat_ryson|     <<<|
        |>>>     |_____________________________|     <<<|
        |>>>                                         <<<|
        |>>>-----------------------------------------<<<|
        |>>>-----------------------------------------<<<|
        |>>>              {red}[githubs]{blue}                  <<<|
        |>>>                                         <<<|
        |>>>    __________________________________   <<<|
        |>>>    |                                 |  <<<|
        |>>>    |github.com/filtering-rubika-ryson|  <<<|
        |>>>    |    github.com/shobadeh          |  <<<|
        |>>>    |_________________________________|  <<<|
        |>>>                                         <<<|
        |>>>-----------------------------------------<<<|
        |>>>-----------------------------------------<<<|
        |>>>              {red}[spcial]{blue}                   <<<|
        |>>>                                         <<<|
        |>>>  ___________________________________    <<<|
        |>>>  |                                 |    <<<|
        |>>>  |{pink}mmd ryson bozorg + mr shobadehgar{blue}|    <<<|
        |>>>  |         [creatar.blog.ir]       |    <<<|
        |>>>  |         [creater.blog.ir]       |    <<<|
        |>>>  |_________________________________|    <<<|
        |>>>                                         <<<|
        |>>>-----------------------------------------<<<|
        |>>>-----------------------------------------<<<|
        —————————————————————————————————————————————————

        """)
            for r in s:
                sys.stdout.write(r)
                sys.stdout.flush()
                sleep(0.002)
            sleep(1)
            print ('\n\n')
            try:
                with open('mmd-ryson.dat', 'w') as _target_:
                    _target_.write (f'{s}')
                    print (f"\033[20;37minformation mmd ryson <SAVE> in \033[00;00m{blue}[mmd-ryson.dat]")
                sleep(2)
            except:
                pass
            try:
                if 'Linux' in typeSys  or 'Mac' in typeSys:
                    system('clear')
                else:
                    system('cls')
            except:
                pass
        #else:
            #print('\n\033[31m[!] \033[35msorry! method not found\n')
            #sleep(1)
            #try:
                #if 'Linux' in typeSys or 'Mac' in typeSys:
                    #system('clear')
                #else:
                    #system('cls')
            #except:
                #pass
            #run.insert()
    @staticmethod
    def reset():
        sleep(1)
        music : str  = input(f"\n\033[35m[?] {red}start {green}music {yellow}(y/n){red}──╼ ❯❯❯ {pink}")
        sleep(0.5)
        if music == "y".lower():
            print (f"\n{blue}start {green}music\n")
            try:
                system("play khalvat.mp3 &> /dev/null")
            except:
                print('\n\033[31m[!] \033[35msorry and please update repository')
                assert system('apt-get update')
        else:
            pass
        mr : str = input(f"""\033[20;37m
                ____________________
                |[T.me/creator_ryson]| > mmd rysoŋ
                ————————————————————

                _____________________
                |update script  [y] |
                |restart script [u] |
                |exit  script   [n] |
                —————————————————————

                {white}[{user}] \033[31m[?] \033[20;37mtype the option \033[31m──╼ ❯❯❯ {pink}""")
        if mr == "y".lower():
                sleep(0.5)
                system("cd && rm -rf Filter-Rubika-Ryson && git clone https://github.com/Filtering-Rubika-Ryson/Filter-Rubika-Ryson && cd Filter-Rubika-Ryson && chmod 777 * && python Filtering.py")
        elif mr == "u".lower():
                sleep(0.5)
                system("python Filtering.py")
        else:
            quit()
if __name__ == '__main__':
    run.main()
    run.insert()
    run.reset()
else:
    raise TypeError('\n\033[31m[!] \033[35mthe support \033[31m-> \033[35mt.me/creator_ryson')
