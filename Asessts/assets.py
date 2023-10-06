from tabulate import tabulate
class colors:
     
     black="\033[1;30;20m"
     red="\033[1;31;20m"
     green = "\033[1;32m"
     yellow="\033[1;33;20m"
     blue="\033[1;34;20m"
     purple="\033[1;35;20m"
     cyan="\033[1;36;20m"
     white="\033[1;37;20m"
     RESET_COLOR_CODE="\033[38;2;255;255;255m"

class banner:
     banner=f"""
        {colors.yellow}
         _    ___ ___  _  _ _____ ___ ___  ___ ___ ___ _   _ ___ ___ _______   __
        | |  | __/ _ \| \| |_   _| __/ _ \/ __| __/ __| | | | _ \_ _|_   _\ \ / /
        | |__| _| (_) | .` | | | | _| (_) \__ \ _| (__| |_| |   /| |  | |  \ V / {colors.green}
        |____|___\___/|_|\_| |_| |___\__\_\___/___\___|\___/|_|_\___| |_|   |_|  
        {colors.cyan}
                     _   _   _   _   _   _   _   _   
                    / \ / \ / \ / \ / \ / \ / \ / \  
                   (SI | MU |  | P | H | I | S | H ) 
                    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  
        {colors.green}
        ________________________________________________________________________
        |                                                                      |{colors.red}
        |   [@]:Created by: Leon Martin                                        |
        |   [@]:Email:martinleontech23@gmail.com                               |
        |   [@]:Whatsapp:0719531573                                            |
        |   [@]:Website:https://www.leonteqsecurity.com                        |
        |   [@]:Github Account:https://github.com/leonTech254                  |{colors.green}
        |                                                                      |
        |______________________________________________________________________|
        """
   

class ToolInfo:
       info=""

class io:
    def  output(info,color):
        toOutput=f"{color}{info}{colors.RESET_COLOR_CODE}"
        print(toOutput)

class SocialMediaMenu:
    def __init__(self):
        self.platforms = {
            1: "Facebook",
            2: "Twitter",
            3: "Instagram",
            4: "LinkedIn",
            5: "Pinterest",
            6: "Snapchat",
            7: "reddit",
            8: "Tumblr",
            9: "YouTube",
            10: "WhatsApp",
            11: "Telegram",
            12: "Skype",
            13: "Discord",
            14: "Medium",
            15: "Quora",
            16: "Flickr",
            17: "Vimeo",
            18: "Twitch",
            19: "SoundCloud",
            20: "Behance"
        }

    def display_menu(self):
        table_data = [(f"{number}: {platform}") for number, platform in self.platforms.items()]
        rows = [table_data[i:i+2] for i in range(0, len(table_data), 2)]

        print("Social Media Platforms:")
        print(tabulate(rows, tablefmt="plain"))
