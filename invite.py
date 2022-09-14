import requests
from colorama import Fore, Back, Style

def main():
    print(Fore.YELLOW+"Discord Invite Code Info (only end part of invite)")
    choice = input(Fore.BLUE+"Choose an option:"+"\n"+Fore.CYAN+"1) Get Invite Info"+"\n"+Fore.LIGHTMAGENTA_EX+"2) Exit"+"\n"+"Choice: ")
    if choice == "1":
        serverinfo()
    elif choice == "2":
        exit()

def serverinfo():
    url = "https://discord.com/api/v9/invites/"+input('Enter the invite code: ')
    r = requests.get(url).json()
    invitecode = r['code']
    guildname = r['guild']['name']
    guildid = r['guild']['id']
    inviter = r['inviter']['username'] + '#' + r['inviter']['discriminator']
    boostlevel = r['guild']['verification_level']
    vanitylevel = r['guild']['premium_subscription_count']
    expire = r['expires_at']
    print(Fore.RED+"Guild Invite Code -> "+Fore.YELLOW+invitecode)
    print(Fore.RED+"Guild Name -> "+Fore.YELLOW+guildname)
    print(Fore.RED+"Guild Id -> "+Fore.YELLOW+guildid)
    print(Fore.RED+"Guild Inviter -> "+Fore.YELLOW+inviter)
    print(Fore.RED+"Guild Boost Level -> "+Fore.YELLOW+boostlevel.__str__())
    print(Fore.RED+"Guild # Of Boosts -> "+Fore.YELLOW+vanitylevel.__str__())
    print(Fore.RED+"Guild Invite Expires -> "+Fore.YELLOW+expire)



    
main()