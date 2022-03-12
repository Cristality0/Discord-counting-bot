import pyautogui
import time
import pyperclip
import random
import sys

# for getting current position
# time.sleep(10)
# print(pyautogui.position())


# time.sleep(5)
# starting_num = 24595
# for _ in range(5):
#     starting_num += 1
#     pyautogui.typewrite(str(starting_num))
#     pyautogui.press("ENTER")
#     time.sleep(7)

# for laptop 640, 856
# for desktop 365, 945
laptop = False
if laptop:
    cord_x = 640
    cord_y = 856
else:
    cord_x = 365
    cord_y = 945

range_low = 28000
range_high = 32000
main_interval = 60
time.sleep(3)
while True:
    rd = random.randint(1, 5)
    pyautogui.moveTo(cord_x, cord_y)
    pyautogui.drag(350, 0, duration=0.17)
    pyautogui.hotkey('ctrl', 'c')
    # pyautogui.press('esc')
    result = pyperclip.paste().split(" ")
    result = result[1] if result[1][0] in '0123456789' else result[2]
    if range_low < int(result) < range_high:
        pyperclip.copy(str(int(result)+1))
    else:
        pyautogui.moveTo(cord_x, cord_y-26)
        pyautogui.drag(350, 0, duration=0.17)
        pyautogui.hotkey('ctrl', 'c')
        # pyautogui.press('esc')
        result = pyperclip.paste().split(" ")
        result = result[1] if result[1][0] in '123456789' else result[2]
        if range_low < int(result) < range_high:
            pyperclip.copy(str(int(result) + 1))
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(' What do you mean, cant even keep the count, low IQ move')
            pyautogui.press('enter')
        else:
            sys.exit()
        sys.exit()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(main_interval+rd)
