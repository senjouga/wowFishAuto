import time
from utils.audio import listen
from utils.action import fishing, jump, snatch
import psutil
import numpy as np

dev = False
checkPass = False
silentVolume=10 # below this volume keep fishing
gotVolume=1800 # higher than this volume hook a fish
maxCatch=500 # catch enough fish
def check_process():
    print('Checking WoW is running')
    wow_process_names = ["Wow.exe"]
    running = False
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if any(p.name() in s for s in wow_process_names):
            print(p.name())
            running = True
    if not running:
        print('WoW is not running')
        return False
    else:
        print('WoW is running')
        return True

def logout():
    print('logout')

def main():
    global checkPass
    global silentVolume
    global gotVolume
    while not check_process():
        print( "Waiting 2 seconds, so you can switch to WoW")
        time.sleep(2)
    catched = 0
    tries = 0
    print("Waiting 2 seconds, so you can switch to WoW")
    time.sleep(2)
    while not dev:
        tries += 1
        fishing()
        if not listen(silentVolume=silentVolume, gotVolume=gotVolume):
            print('If we didn\' hear anything, lets try againf')
            jump()
            time.sleep(3)
            continue
        else:
            print('I guess we snatched something')
            snatch()
            time.sleep(3)
        catched += 1
        print(f"current catched: {catched}")
        if catched == maxCatch:
            break
        time.sleep(3)
    print('catched ' + str(catched))
    logout()

if __name__ == "__main__":
    main()