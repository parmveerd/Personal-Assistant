import pyautogui
import time
import psutil

# open iTunes (can also just do it using the file path)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('iTunes')
time.sleep(1)
pyautogui.press('enter')

name = 'iTunes.exe'

# timeout 2 minutes
timeout = time.time() + 120

while True:
    # check if iTunes is open
    for process in psutil.process_iter():
        try:
            if process.name() == name:
                # application is now open and can break out of loops
                print("iTunes is open")
                break
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    else:
        # if iTunes is not open, check timeout
        if time.time() > timeout:
            print("Timed out")
            break
        else:
            time.sleep(1)
            continue
    break

# sleep so iTunes can start up before playing music
time.sleep(6)
pyautogui.press('space')

