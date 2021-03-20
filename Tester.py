#RECODE AJA
#BY : DIMAS SATRIO
#SCRIPT UNTUK SENANG SENANG
#!/usr/bin/python2
# coding=utf-8

#Import Module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,base64
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
     import mechanize
except ImportError:
     os.system("pip2 install mechanize")
try:
     import bs4
except ImportError:
     os.system("pip2 install bs4")
try:
     import requests
except ImportError:
     os.system("pip2 install requests")
     os.system("python2 Tester.py")
from requests.exceptions import ConnectionError
from mechanize import Browser

def jalan(z):
    for  e in z + '\n':
         sys.stdout.write(e)
         sys.stdout.flush()
         time.sleep(0.20)

logo = """
\033[1;97m _______ _______ _______ _______ _______  ______
    |    |______ |______    |    |______ |_____/
    |    |______ ______|    |    |______ |    \_
"""

baner = """
\033[1;97m______ ___________________________   __
___  / __  __ \_  ____/___  _/__  | / /
__  /  _  / / /  / __  __  / __   |/ /
_  /___/ /_/ // /_/ / __/ /  _  /|  /
/_____/\____/ \____/  /___/  /_/ |_/
"""
x = "EAAAUZI8JKKzdM6fBK2K2U3JJA"

# KELUAR #
def keluar():
    print "Keluar Berhasil !, Bentar Follow IG gue dong bro"
    os.system("xdg-open https://instagram.com/dimasstr18_")
    os.sys.exit()
# LOGIN #
def login():
    os.system('clear')
    print baner
    print "\033[1;97m-----------------------------------------------------"
    print "      SALIN TOKEN : \033[1;93mEAAAUZI8JKKzdM6fBK2K2U3JJA"
    print "\033[1;97m-----------------------------------------------------"
    token = raw_input("\033[1;97mMasukan Token : ")
    if token ==x:
       print " \033[1;92mLogin Succes !"
       time.sleep(2)
       os.system('clear')
       main()
    else:
       print " \033[1;91mLogin Failed !"
       time.sleep(2)
       login()
       os.system('clear')
# PAYUDARA #
def payudara():
    print logo
    print "\033[1;97m-----------------------------------------------------"
    jalan("\033[1;97m                    LOADING ...")
    print "\033[1;97m-----------------------------------------------------"
# STOP COLI #
def stop():
    os.system('clear')
    payudara()
    print "\033[1;97mTunggu Anda Akan diarahkan Ke Crhome Untuk Mengetahui Tutorialnya.."
    os.system('xdg-open https://pastelink.net/2qqd0')
# TERUS COLI #
def terus():
    os.system('clear')
    payudara()
    print "\033[1;97mTunggu Anda Akan diarahkan Ke Crhome Untuk Mengetahui Tutorialnya..."
    os.system('xdg-open https://pastelink.net/2qqdl')
# KONTOL #
def kontol():
    os.system('clear')
    payudara()
    print "\033[1;97mTunggu Anda Akan diarahkan Ke Crhome Untuk Mengetahui Tutorialnya..."
    os.system('xdg-open https://pastelink.net/2qqeb')
# MEMEK #
def memek():
    os.system('clear')
    payudara()
    print  "\033[1;97mTunggu Anda Akan diarahkan Ke Crhome Untuk Mengetahui Tutorialnya.."
    os.system('xdg-open https://pastelink.net/2qqgd')
# PENIS #
def penis():
    os.system('clear')
    payudara()
    print "\033[1;97mAnda Akan Di Arahkan Ke Whatapp Author Untuk Melaporkan BUG / EROR"
    os.system('xdg-open http://api.whatsapp.com/send?phone=+6289601235125&text=AdaBUG')
# MENU #
def menu():
    os.system('clear')
    jalan("\033[1;97mHallo sahabat sahabat ku...")
    time.sleep(0.5)
    os.system('clear')
    login()
# MAIN #
def main():
    os.system('clear')
    print logo
    print "\033[1;97m-----------------------------------------------------"
    print " \033[1;97m[\033[1;92m<\>\033[1;97m] \033[1;97mAUTHOR : \033[1;97m DIMAS SATRIO"
    print "\033[1;97m-----------------------------------------------------"
    print " \033[1;97m[\033[1;94m01\033[1;97m] TUTORIAL UBAH SESI S7i JADI SESI TTL "
    print " \033[1;97m[\033[1;94m02\033[1;97m] TUTORIAL JEBOLIN SESI S7i "
    print " \033[1;97m[\033[1;94m03\033[1;97m] TUTORIAL LOGIN FB LUAR AGAR TIDAK CHEKPOINT"
    print " \033[1;97m[\033[1;94m04\033[1;97m] TUTORIAL MEMBUAT AKUN LOCKED/TERKUNCI"
    print " \033[1;97m[\033[1;94m05\033[1;97m] Laporkan Bug / Eror"
    print " \033[1;97m[\033[1;91m00\033[1;97m] Exit "
    print "\033[1;97m-----------------------------------------------------"
    pilih()

# PILIH #
def pilih():
    kk = raw_input("\033[1;97m<\> : ")
    if kk =="":
       print "\033[1;97mIsi yang benar goublok !"
       pilih()
    elif kk =="1" or kk =="01":
       stop()
       raw_input(" Back To Enter")
       main()
       payudara()
    elif kk =="2" or kk =="02":
       terus()
       raw_input(" Back To Enter")
       main()
       payudara()
    elif kk =="3" or kk =="03":
       kontol()
       raw_input(" Back To Enter")
       main()
       payudara()
    elif kk =="4" or kk =="04":
       memek()
       raw_input(" Back To Enter")
       main()
       payudara()
    elif kk =="5" or kk =="05":
       penis()
       raw_input(" Back To Enter")
       main()
       payudara()
    elif kk =="0" or kk =="00":
       keluar()
    else:
       print "\033[1;91mIsi yang benar goublok !"
       pilih()
       
if __name__=='__main__':
      menu()
      login()
      payudara()
      keluar()
