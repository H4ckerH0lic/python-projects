import requests
from colorama import Fore,Style,init

init(autoreset=True)

def subdomai_enum(domain,wordlist_file):
    try:
        with open(wordlist_file,"r") as f:
            subdomains= f.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + f"\nwordlist file {wordlist_file} not found")
        return
    print(Fore.MAGENTA + f"\n[*] Statrting Subdomain enum for domain : {domain}")

    for sub in subdomains:
        url = f"https://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                print(Fore.GREEN + f"[+] found: {url}")
        except requests.ConnectionError:
            pass
        except requests.Timeout:
            pass

if __name__ == "__main__":
    target_domain = input(Fore.CYAN + " Enter your Domain : ")
    wordlist = "n0kovo_subdomains_small.txt"
    subdomai_enum(target_domain,wordlist)