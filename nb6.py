import os
import random
import time
from concurrent.futures import ThreadPoolExecutor

GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

def linex():
    print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def ____banner____():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{GREEN}
        
               ░█████╗░  ██╗░░██╗  ██████╗░
               ██╔══██╗  ██║░░██║  ██╔══██╗
               ███████║  ███████║  ██████╦╝
               ██╔══██║  ██╔══██║  ██╔══██╗
               ██║░░██║  ██║░░██║  ██████╦╝
               ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═════╝░
{RESET}""")

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       {RED}Old Code {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f'       {RED}METHOD 1{RESET}')
    print(f'       {RED}METHOD 2{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2009-2010{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}TOTAL ID COUNT {GREEN}: {RESET}")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

# Dummy login methods for demonstration
def login_1(uid):
    print(f"{GREEN}Login method 1 for UID: {uid} [SAN9]{RESET}")
def login_2(uid):
    print(f"{RED}Login method 2 for UID: {uid} [SAN9]{RESET}")

def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} OLD CLONE{RESET}')
    linex()
    choice = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if choice in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {RED}Choose Valid Option...{RESET}")
        time.sleep(2)
        BNG_71_()

def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} ALL SERIES{RESET}')
    linex()
    print(f'       {RED}(B){GREEN} 100003/4 SERIES{RESET}')
    linex()
    print(f'       {RED}(C){GREEN} 2009 series{RESET}')
    linex()
    _input = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n{RED}Choose Value Option...{RESET}")
        BNG_71_()

if __name__ == '__main__':
    BNG_71_()import os
import random
import time
from concurrent.futures import ThreadPoolExecutor

GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

def linex():
    print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def ____banner____():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{GREEN}
        
               ░█████╗░  ██╗░░██╗  ██████╗░
               ██╔══██╗  ██║░░██║  ██╔══██╗
               ███████║  ███████║  ██████╦╝
               ██╔══██║  ██╔══██║  ██╔══██╗
               ██║░░██║  ██║░░██║  ██████╦╝
               ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═════╝░
{RESET}""")

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       {RED}Old Code {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f'       {RED}METHOD 1{RESET}')
    print(f'       {RED}METHOD 2{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2009-2010{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}TOTAL ID COUNT {GREEN}: {RESET}")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

# Dummy login methods for demonstration
def login_1(uid):
    print(f"{GREEN}Login method 1 for UID: {uid} [SAN9]{RESET}")
def login_2(uid):
    print(f"{RED}Login method 2 for UID: {uid} [SAN9]{RESET}")

def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} OLD CLONE{RESET}')
    linex()
    choice = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if choice in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {RED}Choose Valid Option...{RESET}")
        time.sleep(2)
        BNG_71_()

def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} ALL SERIES{RESET}')
    linex()
    print(f'       {RED}(B){GREEN} 100003/4 SERIES{RESET}')
    linex()
    print(f'       {RED}(C){GREEN} 2009 series{RESET}')
    linex()
    _input = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n{RED}Choose Value Option...{RESET}")
        BNG_71_()

if __name__ == '__main__':
    BNG_71_()import os
import random
import time
from concurrent.futures import ThreadPoolExecutor

GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

def linex():
    print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def ____banner____():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{GREEN}
        
               ░█████╗░  ██╗░░██╗  ██████╗░
               ██╔══██╗  ██║░░██║  ██╔══██╗
               ███████║  ███████║  ██████╦╝
               ██╔══██║  ██╔══██║  ██╔══██╗
               ██║░░██║  ██║░░██║  ██████╦╝
               ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═════╝░
{RESET}""")

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       {RED}Old Code {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f'       {RED}METHOD 1{RESET}')
    print(f'       {RED}METHOD 2{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2010-2014{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"       {RED}OLD CODE {GREEN}2009-2010{RESET}")
    ask = input(f"       {RED}SELECT {GREEN}: {RESET}")
    linex()
    ____banner____()
    print(f"       {RED}EXAMPLE {GREEN}20000 / 30000 / 99999{RESET}")
    limit = input(f"       {RED}TOTAL ID COUNT {GREEN}: {RESET}")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {RED}METHOD A{RESET}')
    print(f'       {RED}METHOD B{RESET}')
    linex()
    meth = input(f"       {RED}CHOICE (A/B): {GREEN}").strip().upper()
    with ThreadPoolExecutor(max_workers=30) as pool:
        ____banner____()
        print(f"       {RED}TOTAL ID FROM CRACK {GREEN}{limit}{RESET}")
        print(f"       {RED}USE AIRPLANE MOD FOR GOOD RESULT{GREEN}{RESET}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"{RED}[!] INVALID METHOD SELECTED{RESET}")
                break

# Dummy login methods for demonstration
def login_1(uid):
    print(f"{GREEN}Login method 1 for UID: {uid} [SAN9]{RESET}")
def login_2(uid):
    print(f"{RED}Login method 2 for UID: {uid} [SAN9]{RESET}")

def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} OLD CLONE{RESET}')
    linex()
    choice = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if choice in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {RED}Choose Valid Option...{RESET}")
        time.sleep(2)
        BNG_71_()

def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print(f'       {RED}(A){GREEN} ALL SERIES{RESET}')
    linex()
    print(f'       {RED}(B){GREEN} 100003/4 SERIES{RESET}')
    linex()
    print(f'       {RED}(C){GREEN} 2009 series{RESET}')
    linex()
    _input = input(f"       {RED}CHOICE {GREEN}: {RESET}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n{RED}Choose Value Option...{RESET}")
        BNG_71_()
        

if __name__ == '__main__':
    import os
    import sys
    import time

    BNG_71_()        
