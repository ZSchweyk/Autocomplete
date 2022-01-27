from pynput.keyboard import Key, Controller, HotKey, KeyCode
from pynput import keyboard
import time

c = Controller()

def press(button):
    c.press(button)
    c.release(button)

def shift_autocomplete(boolean, char):
    if boolean:
        with c.pressed(Key.shift_r):
            press(char)
    else:
        press(char)
    c.release(Key.shift_l)
    press(Key.left)

with keyboard.GlobalHotKeys(
        {
            "<shift>+9": lambda: shift_autocomplete(True, "0"),

            "<shift>+[": lambda: shift_autocomplete(True, "]"),
            "[": lambda: shift_autocomplete(False, "]"),

            "<shift>+'": lambda: shift_autocomplete(True, "'"),
            "'": lambda: shift_autocomplete(False, "'"),


        }
) as h:
    h.join()

# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)


