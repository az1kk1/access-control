import os
import sys
import json
import requests
import hashlib
import time
import socket
import pwinput
from colorama import Fore, Style, init

# ⚡️ GitHub sozlamalari
ACCESS_CODES_FILE = "access_codes.json"
GITHUB_REPO = "az1kk/access-control"
GITHUB_TOKEN = "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"

# 📡 IP manzilni olish
def get_real_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    return response.json()["ip"]

# 📦 Access Code-larni yuklash
def load_access_codes():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{ACCESS_CODES_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        content = json.loads(response.json()["content"])
        return content
    return {}

# 🔐 Access Code-larni GitHub-ga saqlash
def save_access_codes(codes):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{ACCESS_CODES_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    sha = response.json().get("sha") if response.status_code == 200 else None

    payload = {
        "message": "Access kod yangilandi",
        "content": json.dumps(codes, indent=4).encode("utf-8").hex(),
        "sha": sha
    }
    
    requests.put(url, json=payload, headers=headers)

# 🎟 Yangi Access Code yaratish
def generate_access_code(ip):
    code = hashlib.sha256(ip.encode()).hexdigest()[:6].upper()
    codes = load_access_codes()
    codes[code] = ip
    save_access_codes(codes)
    return code

# ✅ Kirishda Access Code tekshirish
def verify_access_code(code, current_ip):
    codes = load_access_codes()
    if code in codes:
        registered_ip = codes[code]
        if registered_ip == current_ip:
            print(Fore.GREEN + "✅ Kirish muvaffaqiyatli!" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "❌ Xatolik: Noto‘g‘ri IP! Bloklandi." + Style.RESET_ALL)
            send_alert_to_github(code, current_ip)
            return False
    else:
        print(Fore.RED + "❌ Xato kod!" + Style.RESET_ALL)
        return False

# ⚠️ GitHub Issues orqali xabar yuborish
def send_alert_to_github(code, ip):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    payload = {
        "title": f"⚠️ Noto‘g‘ri kirish urinishlari! {code}",
        "body": f"Access Code: {code}\nIP: {ip}",
        "labels": ["security"]
    }
    
    requests.post(url, json=payload, headers=headers)

# 🚀 Kirishdan oldin IP Access Code tekshirish
def start_access_control():
    user_ip = get_real_ip()
    access_code = generate_access_code(user_ip)
    print(f"🔑 Sizning Access Code: {Fore.YELLOW}{access_code}{Style.RESET_ALL}")

    entered_code = input("Access Code-ni kiriting: ")
    if not verify_access_code(entered_code, get_real_ip()):
        print(Fore.RED + "❌ Kirish taqiqlangan!" + Style.RESET_ALL)
        sys.exit()
    print(Fore.GREEN + "✅ Kirish tasdiqlandi! Tizim yuklanmoqda..." + Style.RESET_ALL)
    time.sleep(2)

# 🔥 Avval Access Code tekshirish, keyin asosiy kodni ishga tushirish
start_access_control()

# UI functions
ip_response = requests.get("https://api64.ipify.org?format=json")
ip = ip_response.json()["ip"]
local_ip = socket.gethostbyname(socket.gethostname())

geo_response = requests.get(f"https://ipapi.co/{ip}/json/")
geo_data = geo_response.json()

def print_colored_text(text, hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    ansi_code = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(ansi_code)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')') 
def success():
    print_colored_text("Success ☆", "#FFDD33")
#Service functions
import socket
import time
def register(email, password):
    clear_screen()
    print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
    print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
    print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
    print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
    print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
    print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
    print_colored_text("│                    CPM AKKAUNT YARATISH                     │","#787672")
    print_colored_text("├─────────────────────────────────────────────────────────────┤","#9e9e9e")
    print_colored_text("│              EMAIL VA PAROLNI TO'G'RI KIRITING!             │","#787672")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
    print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252"),
    email=input(Fore.LIGHTWHITE_EX+"Email │ "+Fore.WHITE+"")
    print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
    print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252")
    password=pwinput.pwinput(prompt="Parol │ "+Fore.WHITE+"")
    print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        if response.status_code == 200 and "idToken" in response_data:
            print("✅ Ro'yxatdan o'tish muvaffaqiyatli!")
            return response_data.get('idToken', None)
        else:
            print(f"❌ Xatolik: {response_data.get('error', {}).get('message', 'Noma’lum xatolik')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Serverga so‘rov jo‘natishda xatolik: {e}")
        return None
    register(email, password)
    xtoken = register(email, password)
API_KEY = "AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA"
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
def login(email, password):
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('idToken', None)
    return None  
#add_money
def add_money(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "money": 50000000
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#addcoin
def add_coin(request):
    coin = input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  COIN MIQDORI: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": coin,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
def add_fcoin(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": 30000,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#get_king
def get_king(request):
    url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"
    url_2 = "https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating4_AppI"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    }
    dd = {
    "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"treasure\" : 2000000000,\"cars\" : 2000000000,\"race_win\" : 999,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"}
    data = {
        "data":"{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\": 2000000000,\"gifts\": 2000000000,\"treasure\": 2000000000,\"cars\": 137,\"race_win\" : 999,\"levels\": 82,\"drift\": 2000000000,\"run\": 2000000000,\"police\": 2000000000,\"block_post\": 2000000000,\"real_estate\": 12,\"fuel\": 2000000000,\"car_trade\": 2000000000,\"car_exchange\": 2000000000,\"burnt_tire\": 2000000000,\"car_fix\": 2000000000,\"car_wash\": 2000000000,\"offroad\": 2000000000,\"passanger_distance\": 2000000000,\"reactions\": 2000000000,\"drift_max\": 2000000000,\"texi\": 2000000000,\"delivery\": 2000000000,\"cargo\": 2000000000,\"push_ups\": 2000000000,\"slicer_cut\":1,\"car_collided\":2000,\"new_type\": 2000}"
    }
    clear_screen()
    a = requests.post(url, headers=headers, json=dd)
    return a.text
#custom_id
def custom_id(request):
    custom_input = input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  YANGI ID: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "LocalID": custom_input,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
def get_all(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "content-length": "4686",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    } 
 xx = {"data":"{"allData":"ios7","boughtFsos":[1],"floats":[169.0,188.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"integers":[1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,15,0,0,0,0,0,0],"wheels":[-1,73,74,79,88,84,87,97,98,101]}"}

a = requests.post(url, headers=headers, json=xx)

    return a
def delete_account(id_token):
    """ Firebase orqali akkauntni o‘chirish """
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:delete?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'idToken': id_token}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Akkaunt muvaffaqiyatli o‘chirildi!")
            return True
        else:
            error_message = response.json().get('error', {}).get('message', 'Noma’lum xatolik')
            print(f"❌ Xatolik: {error_message}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Serverga so‘rov jo‘natishda xatolik: {e}")
        return False

# Задаем пароль
clear_screen()
correct_password = "CPMTool"
print("CPM Tool v1.0"+Fore.LIGHTWHITE_EX+" | "+Fore.WHITE+"EGA: "+Fore.GREEN+"@CPMToolTeam")
print(Fore.WHITE+"IP: "+Fore.GREEN+get_real_ip())
password = pwinput.pwinput(prompt=""+Fore.WHITE+"PAROLNI KIRITING: "+Fore.LIGHTCYAN_EX, mask="•")
loader()
if password != correct_password:
    clear_screen()
    print("Parol xato!\nDastur yakunlandi. ❌")
    sys.exit()
else:
    print("Successful ✅")
    clear_screen()
# Проверяем пароль

if password != correct_password:
    clear_screen()
    print("Parol xato!\nDastur yakunlandi. ❌")
    sys.exit()  # Завершаем выполнение скрипта
else:
    print("Successful ✅")
    clear_screen()
""""""
""""""
#Main functions
while True:
 print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
 print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
 print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
 print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
 print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
 print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
 print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
 print_colored_text("│                    CPM AKKAUNTGA KIRISH                     │","#787672")
 print_colored_text("├─────────────────────────────────────────────────────────────┤","#9e9e9e")
 print_colored_text("│              EMAIL VA PAROLNI TO'G'RI KIRITING!             │","#787672")
 print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252"),
 email=input(Fore.LIGHTWHITE_EX+"Email │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252")
 password=pwinput.pwinput(prompt="Parol │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 token = login(email, password)
 time.sleep(2)
 clear_screen()
 print(Fore.LIGHTWHITE_EX+"Akkauntga kirilmoqda! \n")
 loader()
 
 if not token:
        clear_screen()
        print(Fore.RED+"Kirish xatosi!"+Fore.LIGHTWHITE_EX+"\nQaytadan urinib ko'ring.")
        time.sleep(1.5)
        clear_screen()
 else:
        print(Fore.GREEN+"Akkauntga muvaffaqiyatli kirdingiz! ✅")
        break
clear_screen()

balance = Fore.GREEN+"Unlimited"
status = Fore.GREEN+"Active"
while True:
    clear_screen()
    print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
    print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
    print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
    print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
    print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
    print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
    print_colored_text(f" - Email: {email}","#c2c2be")
    print_colored_text(f" - Parol: {password}","#c2c2be")
    print(Fore.LIGHTWHITE_EX+" - Sizning real IP manzilingiz:",Fore.GREEN + get_real_ip())
    print_colored_text(f" - Mamlakat: {geo_data.get('country_name', 'NaN')}"+f", {geo_data.get('city','NaN')}", "#c2c2c2")
    print_colored_text(f" - Balance: {balance} │ Status: {status}","#c2c2be")
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
    print_colored_text("│                        CPM SERVICES                         │","#787672")
    print_colored_text("├──────────────────────────────┬┬─────────────────────────────┤","#9e9e9e")
    print_colored_text("│ [1] ➤ PUL SOLISH             ││  [2] ➤ COIN SOLISH          │","#c2c2be")
    print_colored_text("│ [3] ➤ KING RANK              ││  [4] ➤ ID O'ZGARTIRISH      │","#c2c2be")
    print_colored_text("│ [5] ➤ $ NARSANI OCHISH       ││  [6] ➤ FULL REGISTER        │","#9e9e9d")
    print_colored_text("│ [7] ➤ AKKAUNTNI O'CHIRISH    ││  [0] ➤ CHIQISH              │","#9e9e9d")
    print_colored_text("├──────────────────────────────┴┴─────────────────────────────┤","#9e9e9e")
    print_colored_text("│                    MASHINALAR OCHILMAYDI!                   │","#787672")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
    command=input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  TANLOVINGIZ: ")
    if command.lower() == "0":
        print(Fore.RED + "Programm finished")
        clear_screen()
        break
    if command.lower() == "1":
        add_money(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "2":
        add_coin(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "3":
        get_king(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "4":
        custom_id(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "5":
        get_all(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "6":
        xtoken = register(email,password)
        add_money(xtoken)
        add_fcoin(xtoken)
        get_king(xtoken)
        get_all(xtoken)
    if command.lower() == "7":
        delete_account(token)
        success()