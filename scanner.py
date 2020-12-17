import socket
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED

finalR = ""

def is_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

port = 1
host = input("Enter the IP Address that you want to scan: ")
for port in range(1025):
    if(is_open(host, port)):
        print(f"{GREEN}[+] {host}:{port} is open        {RESET}")
        finalR += f"{GREEN}[+] {host}:{port} is open" + "\n"
        # print("{}".format(GREEN) + "[+] {}".format(host) + " : {}".format(port) + " is open        {}".format(RESET))
    else:
        # print("{}".format(GREEN) + "[!] {}".format(host) + " : {}".format(port) + "is closed       {}".format(RESET))
        print(f"{RED}[!] {host}:{port} is closed        {RESET}", end="\r")
