import socket
import argparse
from colorama import Fore, Style

parser = argparse.ArgumentParser(description="Simple Port scanner")
parser.add_argument("host", help="Target IP or Hostname")
parser.add_argument("-p","--ports", help="ports to scan (e.g. 1-1024", default="1-1024")
args = parser.parse_args()

start, end = map(int, args.ports.split("-"))

for port in range(start, end+1):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((args.host, port))
    if result == 0:
        print(f"{Fore.GREEN}[+] Port {port} is OPEN{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] Port {port} is CLOSED{Style.RESET_ALL}")
    sock.close()