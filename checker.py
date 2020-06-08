import os
from colorama import Fore, Back, Style #importing style and color

#printing the name
print(Fore.WHITE+"Welome to VULPW - a password vulnerability checker")
print(Fore.MAGENTA+'''
|       | |      | |        /=======| |       |       |
 |     |  |      | |        |       |  |     | |     |
  |   |   |      | |        |_______/   |   |   |   |
   | |    |      | |        |            | |     | |
    |     \______/ \_______ |             |       |
-by Kushwanth
''')

#choosing an option
print("Choose your Option")
#available options
print(Fore.BLUE + Style.BRIGHT + "1.Password check\n2.Username check\n3.WiFi check\n4.Leaked Database check")
#user input option
option = int(input(Fore.RED+"Your Option: "))
#password checker
if option == 1:
   name = str(input(Fore.GREEN+Style.DIM+"Enter the password: "))
   pwd = open('password.txt') #opening passwords wordlist
   for line in pwd.read().rsplit(): #looping through passwords
       if name == line:
          print(Fore.CYAN + Style.BRIGHT+ "Your Password "+name+" is Vulnerble")
          break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

#username checker
if option == 2:
   name = str(input(Fore.GREEN+"Enter the username: "))
   user = open('usernames.txt') #opening username wordlist
   for line in user.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your username "+name+" is Vulnerble")
           break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

#wifi passwoord checker
if option == 3:
   name = str(input(Fore.GREEN+"Enter the password: "))
   wifi = open('wifipwd.txt') #opening passwords wordlist
   for line in wifi.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your WiFi password "+name+" is Vulnerble")
           break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

#dictionary of leaked Databases
leak = {1:'000webhost.txt',
2:'adobe100.txt',
3:'alleged-gmail-passwords.txt',
4:'Ashley-Madision.txt',
5:'bible.txt',
6:'carders.cc.txt',
7:'elitehacker.txt',
8:'facebook.txt',
9:'faithwriters.txt',
10:'hak5.txt',
11:'honeynet.txt',
12:'hotmail.txt',
13:'izmy.txt',
14:'Lizard-Squad.txt',
15:'md5decryptot-uk.txt',
16:'muslimMatch.txt',
17:'myspace.txt',
18:'phpbb.txt',
19:'porn-unknown.txt',
20:'rockyou.txt',
21:'singles.txt',
22:'tuscl.txt',
23:'youporn2012.txt'}

#leaked database checker
if option == 4:
   for k,v in leak.items():
       print(Fore.CYAN+Style.BRIGHT,k,""+v)
       #choosing a leaked database
   dboption = int(input("choose your database(enter database number): "))
   dbname = leak[dboption]
   name = str(input(Fore.GREEN+"Enter the password: "))
   dbpwd = open("Leaked-Databases/"+dbname)
   for line in dbpwd.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your password "+name+" has been Leaked")
       break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

#resetting all styles
print(Style.RESET_ALL+"Thank You for Using")
