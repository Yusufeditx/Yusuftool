from platform import system
import sys
import os
import datetime   
from time import sleep
import getpass
url = 'https://m.facebook.com/login.php'
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import getpass
import subprocess 
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
ugen2=['User Agent: Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36']
ugen=['User Agent: Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36']



def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import getpass
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from getpass import getpass
import getpass
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
khushi = "majnudon"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"





def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   



       ██╗  ██╗ █████╗ ███╗   ███╗███████╗███████╗███╗   ██╗ █████╗ 
██║ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔════╝████╗  ██║██╔══██╗
█████╔╝ ███████║██╔████╔██║█████╗  █████╗  ██╔██╗ ██║███████║
██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══╝  ██║╚██╗██║██╔══██║
██║  ██╗██║  ██║██║ ╚═╝ ██║███████╗███████╗██║ ╚████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                             
                                                         
                                                         
                                          
                                                          
  
██╗   ██╗██╗   ██╗███████╗██╗   ██╗███████╗
╚██╗ ██╔╝██║   ██║██╔════╝██║   ██║██╔════╝
 ╚████╔╝ ██║   ██║███████╗██║   ██║█████╗  
  ╚██╔╝  ██║   ██║╚════██║██║   ██║██╔══╝  
   ██║   ╚██████╔╝███████║╚██████╔╝██║     
   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     
                                           

                                                          
                                                          
                                                                                                                   
                                                          
                                                          
                                                            
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()

print('''\033[1;33m---------------------------------------------------------------------\n''')


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


def message_on_messenger(message):
    for index, i in enumerate(ns):
        try:
            message = str(mn) + ' ' + i
            url ="https://graph.facebook.com/v15.0/{0}/".format('t_' + str(thread_id))
            parameters = {'access_token': access_tokens[index % len(access_tokens)], 'message': message}
            s = requests.post(url, data=parameters, headers=headers)
            tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

            if s.ok:
                e =datetime.now()
                print("\033[1;32;40m", end = "")
                print('\033[1;34m[✓] Y3 T3R1 1D K9 N9M3 :: \033[1;35m', get_profile_name(access_tokens[index % len(access_tokens)]), '\n')
                print("\033[1;32;40m", end = "")               
                print("--> T9TT9 C09V0 1D  :--", thread_id)
                print (e.strftime("--> L3G3ND FT YUSUF D09 9L1V3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> M9SS9G3 S3NT BY YUSUF T00L :D ::-->> ", message)
                print('\n')
                time.sleep(timm)
            else:
                print('\033[1;32m[x] Message Block ' + tt, '\n[×] Token Error\n')
                time.sleep(30)
        except Exception as e:
            print("\033[1;31;40m", end = "")
            print(e , '\n')           
            time.sleep(30)


def get_profile_name(access_token):
    payload = {'access_token': access_token}
    a = "https://graph.facebook.com/v15.0/me"
    b = requests.get(a, params=payload)
    d = json.loads(b.text)
    if 'name' not in d:
        print(BOLD + RED + '\n[x] Token Invalid..!!')
        sys.exit()
    return d['name']

def get_profile_name2(access_token):
    payload = {'access_token': access_token}
    a = "https://graph.facebook.com/v15.0/me"
    b = requests.get(a, params=payload)
    d = json.loads(b.text)
    if 'id' not in d:
        print(BOLD + RED + '\n[x] Token Invalid..!!')
        sys.exit()
    return d['id']


def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")

print('''\033[1;36m---------------------------------------------------------------------\n''')
print('''\033[1;35m-=[ Facebook Tool Ka owner YUSUF KHAN BLACK MAFIA RULEX  ]=-''')
print('''\033[1;33m-=[ Contact Us :: thew YUSUF PAPA inside  /]=-\n''')
i = datetime.now()
print('''\033[1;36m---------------------------------------------------------------------\n''')
print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
print('''\033[1;32m[#] _ Tool Fucker == > [ YUSUF D09  ]\n''')
print("\033[1;36;40m", end = "")        
password = input("\033[1;36m[+] P9SS D9L T00L K9  :: ")

if password == kameena0:

    token_file = input("[+] T0K39 F1L3 D9L :: ")
    print('\n')

    with open(token_file, 'r') as f2:
        access_tokens = f2.read().splitlines()

    print("\nList of Access Tokens and their Profile Names:")

    for index, access_token in enumerate(access_tokens, 1):
        profile_name = get_profile_name(access_token)
        print(f"{index}. All Profile Name : {profile_name}")
        

    for access_token in access_tokens:
        
        print('\n')      
             
  
        thread_id = input(BOLD + CYAN + "\033[1;36m[+] Enter C09V0 ID :: \033[1;32;1m")
        mn = input(BOLD + CYAN + "\033[1;36m[+] Enter T9TT9 Name :: \033[1;32;1m")
        ms = input(BOLD + CYAN + "\033[1;36m[+] Enter G9L1 B9L1 File :: \033[1;32;1m")
        repeat = int(input(BOLD + CYAN + "\033[1;36m[+] ISME 99999999 DAL :: \033[1;32;1m"))
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
        print('\n')               
        
        ns = open(ms, 'r').readlines()

        for i in range(repeat):
            messenger = get_messages()
            message_on_messenger(thread_id)
else:
    print(BOLD + RED + '[-] <==> Your Number Is Wrong Please Take Approval From Owner')
