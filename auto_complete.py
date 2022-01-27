from pynput.keyboard import Key, Controller, HotKey, KeyCode
from pynput import keyboard
import time
# import keyboard


def on_press(key):
    print(key.code)
    if key == KeyCode("l"):
        print("Close parans")
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))



# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        ) as listener:
    listener.join()





















# c = Controller()
#
# def press(button):
#     c.press(button)
#     c.release(button)
#
#
# def parenthesis_autocomplete():
#     with c.pressed(Key.shift):
#         press("9")
#         press("0")
#
#     # c.press(Key.shift)
#     # press("9")
#     # press("0")
#     # c.release(Key.shift)
#     press(Key.left)
#
#
#
# with keyboard.GlobalHotKeys({'shift+9': parenthesis_autocomplete}) as h:
#     h.join()













# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)


