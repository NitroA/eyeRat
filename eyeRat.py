from tools import generator
from colorama import Back , Fore
from tools import launcher
from os import system
from platform import system as osType 
from subprocess import getoutput
def chdps():
  QModules=['opencv','numpy','pyaudio','pyautogui','cryptography','pymsgbox','pillow','psutil','colorama']
  ntInstall=[]
  pipList=getoutput(("pip list")).lower()
  for pkg in QModules:
    if not pkg in pipList:
      ntInstall.append(pkg)
  if len(ntInstall):
    for NTpkg in ntInstall:
      print(f"{Fore.LIGHTRED_EX}[ ! ] Module {NTpkg} not found !\nTry with : pip3 install {NTpkg}\n\n")
    exit()
def clear():
    if "windows" in osType().lower():
        system("cls")
    else :
        system("clear")
def main():
  clear()
  selection=input(f"""
         ____                                                               
        |{Back.RED} {Fore.BLACK}卐{Fore.RESET} {Back.RESET}|                                                              
        |{Back.RED}____{Back.RESET}|                                                              
       _|{Back.RED}____{Back.RESET}|_                                                             
      {Fore.LIGHTBLACK_EX}  /  @@`.                                                             
      .<     __O                                                            
     {Fore.LIGHTBLACK_EX}/\ \.-.' \     {Fore.CYAN}███████╗██╗   ██╗███████╗   ██████╗  █████╗ ████████╗{Fore.RESET}
    {Fore.LIGHTBLACK_EX}J  `.|`.\/ \    {Fore.CYAN}██╔════╝╚██╗ ██╔╝██╔════╝   ██╔══██╗██╔══██╗╚══██╔══╝{Fore.RESET}
    {Fore.LIGHTBLACK_EX}| |_.|  | | |   {Fore.CYAN}█████╗   ╚████╔╝ █████╗     ██████╔╝███████║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}\__.'`.|-' /   {Fore.CYAN}██╔══╝    ╚██╔╝  ██╔══╝     ██╔══██╗██╔══██║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}L   /|o`--'\   {Fore.CYAN}███████╗   ██║   ███████╗   ██║  ██║██║  ██║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}|  /\/\/\   \  {Fore.CYAN}╚══════╝   ╚═╝   ╚══════╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {Fore.RESET}
{Fore.LIGHTBLACK_EX}     J /      `.__\                                                         
{Fore.LIGHTBLACK_EX}     |/         /  \                                                        
      \\      .'`.  `.                                            .'         
    ____)_/\_(____`.  `-._______________________________________.'/         
   (___._/  \_.___) `-.________________________________________.-'          

                 {Fore.RED}[ {Fore.CYAN}1 {Fore.RED}]{Fore.CYAN}Client launcher{Fore.RED}    [ {Fore.CYAN}2 {Fore.RED}] {Fore.CYAN}Generate normal connection rat
                                                                                                   
                 {Fore.RED}[ {Fore.CYAN}3 {Fore.RED}]{Fore.CYAN}Server launcher{Fore.RED}    [ {Fore.CYAN}4 {Fore.RED}] {Fore.CYAN}Generate reverse connection rat 
                  
                  {Fore.LIGHTGREEN_EX}Enter your selection :{Fore.MAGENTA} """)
  clear()
  if selection=='1':
    try:
      launcher.main("client")
    except KeyboardInterrupt:
      pass
  elif selection == '2':
    try:
      generator.main("server")
    except KeyboardInterrupt:
      pass
  elif selection=='3':
    try:
      launcher.main("server")
    except KeyboardInterrupt:
      pass
  elif selection == '4':
    try:
      generator.main("client")
    except KeyboardInterrupt:
      pass
if __name__=='__main__':
  chdps()
  while 1:
    try:
      main()
    except KeyboardInterrupt:
      print(f"\n\n{Fore.RED}ヽ(･_･)/{Fore.CYAN} CTR-C {Fore.RED}\(･_･)/{Fore.RESET}")
      break
