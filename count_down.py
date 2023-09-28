import sevseg
import sys, time

# Modify the seconds if you want
secondsleft = 10

# the loop print the countdown
while True:
    print("\n" * 60)
    print("COUNT DOWN START...")
    # calculating the hours
    hours = str(secondsleft // 3600)
    # calculating the minutes
    minutes  = str((secondsleft % 3600) // 60)
    # calculating the seconds
    seconds = str(secondsleft % 60)
    # spliting the string into layers
    htop, hmiddle, hbottom = sevseg.getSevSegStr(hours, 2).splitlines()
    mtop, mmiddle, mbottom = sevseg.getSevSegStr(minutes, 2).splitlines()
    stop, smiddle, sbottom = sevseg.getSevSegStr(seconds, 2).splitlines()
    # printing the countdown layer by layer
    print(f"{htop}   {mtop}   {stop}")
    print(f"{hmiddle} * {mmiddle} * {smiddle}")
    print(f"{hbottom} * {mbottom} * {sbottom}")
    # checking for the timeup
    if secondsleft == 0:
        print()
        print("******BOOM******")
        print()
        sys.exit()
    print("Ctl+c to Quit the program...")
    time.sleep(1)
    secondsleft -= 1
