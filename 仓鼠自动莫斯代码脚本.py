import pyautogui
import time

# 摩斯密码字典
morse_code = {
    'a': '.-',  # A
    'b': '-...',  # B
    'c': '-.-.',  # C
    'd': '-..',  # D
    'e': '.',  # E
    'f': '..-.',  # F
    'g': '--.',  # G
    'h': '....',  # H
    'i': '..',  # I
    'j': '.---',  # J
    'k': '-.-',  # K
    'l': '.-..',  # L
    'm': '--',  # M
    'n': '-.',  # N
    'o': '---',  # O
    'p': '.--.',  # P
    'q': '--.-',  # Q
    'r': '.-.',  # R
    's': '...',  # S
    't': '-',  # T
    'u': '..-',  # U
    'v': '...-',  # V
    'w': '.--',  # W
    'x': '-..-',  # X
    'y': '-.--',  # Y
    'z': '--..',  # Z
}

# 指定点击的坐标
x, y = 159, 511  # 请替换为你的坐标

# 时间参数
dot_duration = 0.2  # 短音持续时间
dash_duration = 1.0  # 长音持续时间
inter_letter_gap = 2.0  # 字母之间的停顿

# 模拟点击函数
def click_morse_letter(letter):
    if letter in morse_code:
        for symbol in morse_code[letter]:
            if symbol == '.':
                pyautogui.click(x, y)  # 短音
                time.sleep(dot_duration)  # 点与点之间的停顿
            elif symbol == '-':
                pyautogui.mouseDown(x, y)  # 长音
                time.sleep(dash_duration)  # 按住
                pyautogui.mouseUp(x, y)  # 释放
            time.sleep(0.2)  # 点与线之间的停顿
        time.sleep(inter_letter_gap)  # 字母之间的停顿
    else:
        print(f"警告：'{letter}' 不在摩斯密码字典中。")

# 模拟"BYBIT"的摩斯密码
for letter in 'okx':
    click_morse_letter(letter)
