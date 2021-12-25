## no system is safe
# programmer / dev /
# HACKERS TECH 

import os
os.system('clear')
os.system('gem install lolcat')

import sys
import time
print('starting hackers tech black hat python framework',end="  ")
for _ in range(10):
    for j in '/-\\|':

        sys.stdout.write("\b"+j)
        sys.stdout.flush()
        time.sleep(.08)
os.system('clear')

banner="""\033[1;32m
______________________________________________________
|\033[31m   insta id - hackers__tech       (queries and etc)\033[32m |
|\033[33m id may be offline because of privacy issues like  \033[32m |
|\033[32m \033[34m instagram cookies etc\033[32m                             |
|_\033[1;31muse_duck_duck_go_or_tor_browser\033[32m____________________|"""
print(banner)
import os
try:
    pri=os.environ['OS']
    if 'Windows' in pri:
        print("not supported in window run in linux ")
  
except:
    print("")
    print("""\033[31m 
│1)--> antivirus ivasion \033[32m
│2)--> bash utility tools for hackers \033[33m
│3)--> nmap scan (-A)\033[34m
│4)--> exif photo metadata gather\033[37m
│5)--> encrypter for python files""")
    os.system('bash about.sh')
   
    try:
        print('└──=',end='')
        i=int(input("\033[47m ──=>\033[1;33m->> \033[1;32m =\033[1;34m=>\033[0m"))
    except:
        print('\033[31m error occured invalid input') 
    if i==6:
        print("""hi thanks for using this tool \n
        and get me on instagram id -\033[38;5;44m hackers__tech 
         \033[0m or telegram id - \033[31m hackers_tech_001
         \n """)  
    if i ==1:
        os.system('python3 encoder.py > main.txt')
        hck=open('main.txt','r')
        kx=input('\033[38;5;22m enter name for output payload file with .py')
        with open(kx,'w') as main:
            main.write('binascii.unhexlify('+hck.read()+')')
    if i ==2 or i==int('02'):
        os.system('git clone https://github.com/hackerstech/crispy-bash-utilities')
        os.chdir('crispy-bash-utilities')
        os.system('bash b.sh')
    if i==3:
        ip=input('enter ip')
        os.system(f'nmap -sV -A {ip}')
    if i==4 or i==int('04'):
        os.system('sudo apt-get install exif')
        print('file should be in working directory')
        img=input('enter image file ')
        os.system(f'exif {img} ')
    if i==5 or i==int('05'):
        os.system('clear')
        print('choose type')
        print('|1)-> binascii encoding')
        print('|2)-> chr and ord encoding ')
        k=input("|_-\033[34m]>>")
        if k=='1' or k=='01':
            
            os.system('python3 encoder.py > main.txt')
            hacker=open('main.txt','r')
            output_file=input('\033[38;5;22m enter name for output file with .py')
            with open(output_file,'w') as main_file:
                main_file.write('import binascii \n')
                main_file.write('binascii.unhexlify('+hacker.read()+')')

            print('\033[31m file is ready',output_file,'file is saved in ',os.system('pwd'))

        if k=='2' or k=='02':
            for _ in range(10):
                for j in '/-\\|':
                    sys.stdout.write("\b"+j)
                    sys.stdout.flush()
                    time.sleep(.08)
                    os.system('clear')

            os.system('python3 crypt.py')



        
print('want to use again y/n',end='')

j=input('')
if j =='Y' or j=='y' or j=='' or j.isspace()==True or j=='Yes' or j=='yes' or j=='YES':
    os.system('python3 script.py')

