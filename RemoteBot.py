import telebot
from telebot import types
import os
import pyautogui
from pynput.keyboard import Controller, Key
import ctypes
from colorama import init, Fore, Style
from datetime import date, datetime


keyboard = Controller()
init(autoreset=True)
date_log = date.today()
time_log = datetime.now().strftime("%H:%M:%S")


TOKEN = "" #bot token
ADMIN_ID = 1234567  #your id




bot = telebot.TeleBot(TOKEN)
print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}bot was enabled{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")


def get_user_info(message):
    user_id = message.from_user.id
    username = message.from_user.username or "no_username"
    return user_id, username


@bot.message_handler(commands=['start'])
def start(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [start]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}", end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return
    bot.send_message(
        message.chat.id,
        "write /help for more commands\nCEO: @hidlow"
    )
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}command execute: /start{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")


@bot.message_handler(commands=['help'])
def help_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [help]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}", end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")

        return
    text = """
/help
/scr
/run
/write
/key
/notify
    """
    bot.reply_to(message, text)
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /help {Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")

@bot.message_handler(commands=['run'])
def run_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [run]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}", end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return

    cmd = message.text.replace("/run ", "").strip()
    if not cmd:
        bot.reply_to(message, "Укажи команду после /run.")
        return

    os.system(cmd)
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /run {cmd}{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")
    bot.reply_to(message, f"Команда выполнена: {cmd}")


# Команда для скриншота
@bot.message_handler(commands=['scr'])
def screenshot_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [scr]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}", end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return

    screenshot = pyautogui.screenshot()
    path = "screen.png"
    screenshot.save(path)

    with open(path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /scr{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")

    os.remove(path)

@bot.message_handler(commands=['write'])
def write_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [write]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}",end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return

    text = message.text.replace("/write ", "").strip()
    if not text:
        bot.reply_to(message, "Укажи текст после /write.")
        return

    keyboard.type(text)
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /write {text}{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")
    bot.reply_to(message, f"Написано: {text}")

@bot.message_handler(commands=['key'])
def key_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [key]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}",end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return

    key_text = message.text.replace("/key ", "").strip()
    if not key_text:
        bot.reply_to(message, "Укажи клавишу после /key.")
        return

    try:
        special_keys = {
            "enter": Key.enter,
            "space": Key.space,
            "tab": Key.tab,
            "shift": Key.shift,
            "ctrl": Key.ctrl,
            "alt": Key.alt,
            "backspace": Key.backspace,
            "esc": Key.esc,
            "up": Key.up,
            "down": Key.down,
            "left": Key.left,
            "right": Key.right,
            "f1": Key.f1,
            "f2": Key.f2,
            "f3": Key.f3,
            "f4": Key.f4,
            "f5": Key.f5,
            "f6": Key.f6,
            "f7": Key.f7,
            "f8": Key.f8,
            "f9": Key.f9,
            "f10": Key.f10,
            "f11": Key.f11,
            "f12": Key.f12,
        }

        if "+" in key_text:
            combo = key_text.split("+")
            keys = [special_keys.get(k.lower(), k) for k in combo]
            for k in keys:
                keyboard.press(k)
            for k in reversed(keys):
                keyboard.release(k)
        else:
            key = special_keys.get(key_text.lower(), key_text)
            keyboard.press(key)
            keyboard.release(key)

        bot.reply_to(message, f"нажата клавиша: {key_text}")
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /key {key_text}{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")

    except Exception as e:
        bot.reply_to(message, f"ошибка: {e}")
        print(e)


notify_icons = {
    "info": 0x40,      #Информация
    "warning": 0x30,   #Внимание
    "error": 0x10,     #Ошибка
    "question": 0x20   #Вопрос
}

@bot.message_handler(commands=['notify'])
def notify_command(message):
    user_id, username = get_user_info(message)
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}В доступе отказано: [notify]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}",end=" ")
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}|{Fore.RESET}{Fore.LIGHTCYAN_EX} id: {user_id} username: {username}")
        return

    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        bot.reply_to(message, "пример: /notify [info|warning|error|question] [текст]")
        return

    icon_type = parts[1].lower()
    text = parts[2]

    icon_code = notify_icons.get(icon_type, 0x10)

    # Создаём всплывающее окно
    bot.reply_to(message, f"уведомление показано: {text}")
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}выполнена команда: /notify {icon_type} {text} {Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} {date_log} {time_log}")
    ctypes.windll.user32.MessageBoxW(0, text, " ", icon_code)


bot.polling(none_stop=True)