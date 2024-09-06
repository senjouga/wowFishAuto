import time
from utils.audio import listen, randomWait, randomIntNum
from utils.action import fishing, jump, snatch
import psutil
import numpy as np

dev = False
checkPass = False
silentVolume=1000 # below this volume keep fishing
gotVolume=1800 # higher than this volume hook a fish
maxCatch=randomIntNum(100, 200) # catch enough fish
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
        randomWait(2,  3)
        if not listen(silentVolume=silentVolume, gotVolume=gotVolume):
            print('If we didn\' hear anything, lets try againf')
            randomWait(1, 3)
            jump()
            randomWait(1, 3)
            continue
        else:
            print('I guess we snatched something')
            snatch()
            randomWait(0, 2)
        catched += 1
        print(f"current catched: {catched}/{maxCatch}")
        if catched == maxCatch:
            break
        randomWait(2, 5)
    print('catched ' + str(catched))
    logout()

if __name__ == "__main__":
    main()