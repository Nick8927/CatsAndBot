"""
 Мини-пианино на Python

Эта программа превращает клавиатуру в простое пианино.
Когда вы нажимаете клавиши A S D F G H J K,
программа проигрывает соответствующие ноты.

Работает на Windows, macOS и Linux.
Использует только стандартные библиотеки Python.
"""


import os
import sys
import keyboard  # нужно установить один раз: pip install keyboard

piano_keys = {
    "a": 261,  # До
    "s": 293,  # Ре
    "d": 329,  # Ми
    "f": 349,  # Фа
    "g": 392,  # Соль
    "h": 440,  # Ля
    "j": 493,  # Си
    "k": 523,  # До (выше)
}

print("🎹 Мини-пианино")
print("Нажимай клавиши A S D F G H J K, чтобы играть ноты. (ESC — выход)")


# Функция воспроизведения звука
def play_tone(freq, duration=0.3):
    """Проигрывает звук частоты (freq - (Гц) в течение duration(длительности) секунд"""
    if sys.platform.startswith("win"):  # проверка ОС
        # Для Windows — встроенный модуль winsound
        import winsound
        winsound.Beep(freq, int(duration * 1000))
    else:
        # Для macOS и Linux используем системный вызов afplay или play
        beep = f"play -nq -t alsa synth {duration} sine {freq}" if sys.platform.startswith("linux") \
            else f"afplay /System/Library/Sounds/Glass.aiff"
        os.system(beep)


# Цикл обработки событий клавиатуры (бесконечный цикл)
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name.lower()

        if key == "esc":
            print("Выход из пианино 🎵")
            break  # выход из цикла

        if key in piano_keys:
            play_tone(piano_keys[key])

# TODO На всякий случай, но вряд ли мы столкнемся с этим:)
# ( Для Linux требует утилиту sox, которая обычно уже установлена, или ставится через sudo apt install sox)
