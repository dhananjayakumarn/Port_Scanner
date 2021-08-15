from math import exp
import socket
from IPy import IP
import termcolor
import random
import string
import pyfiglet

pyfiglet.print_figlet("Z_SECURITY")

termcolor.cprint(("Tools available to use "),'red')
termcolor.cprint(("1. PortScanner "),'green')
termcolor.cprint(("2. Strong Password generator "),'green')

choose = int(input("Enter the tool You like to use:--"))  


if choose == 1:

    targets = input('[+]Enter Target To scan:--')  #input target host

    def service(port):
        return socket.getservbyport(port)  # gets server by port
    
    def check_ip(ip):
        try:
            IP(ip)
            return(ip)
        except ValueError:
            return socket.gethostbyname(ip)  #get host name by ip

    def machine(targets):
            return socket.gethostbyaddr(targets) # get on which server the service is hosted

    machine_hostname = machine(targets)

    def scan(target):
        converted_ip = check_ip(target)

        print(f'\n scanning target [{target}]------->{str(machine_hostname)}')
        for port in range(1,200):
            scan_port(converted_ip,port)


    def get_banner(s):
        return s.recv(1024)           #banner grabbing


    def scan_port(ipaddress,port):     #port scanner
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ipaddress,port))
            try:
                banner = get_banner(sock)
                services = service(port)
                termcolor.cprint((f"[+] Port {port} is open     --service running in {port} is {services}:--" + str(banner.decode().strip('\n'))),'red')
            except:
                services = service(port)
                print(f"[+] Port {port} is open     --service running in {port} is {services} " )    
        except:
            pass


    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
        exit(0)
        

#password generator

elif choose == 2:
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

plen = int(input("[+] Enter the length of password:---"))
if plen<=8:
    print("[-] Your password cannot be less than 8 characters.....")
    exit(0)
    
elif plen>8:
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
random.shuffle(s)
print("" .join(s[0:plen]))    







            