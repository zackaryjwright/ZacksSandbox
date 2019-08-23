"""
nordvpn login - Log in.
nordvpn connect or nordvpn c - Connect to VPN. To connect to specific servers, use nordvpn connect <country_code server_number> (eg. nordvpn connect uk715)
nordvpn disconnect or nordvpn d - Disconnect from VPN.

nordvpn set or nordvpn s - Set a configuration option. Possible options:
nordvpn set cybersec on or off - Enable or disable CyberSec
nordvpn set killswitch on or off - Enable or disable Kill Switch
nordvpn set autoconnect on or off - Enable or disable Autoconnect. You can set a specific server for automatic connection using nordvpn set autoconnect on country_code+server_number. Example: nordvpn set autoconnect on us2435.
nordvpn set protocol udp or tcp - Switch between UDP and TCP protocols
nordvpn set obfuscate on or off - Enable or disable Obfuscated Servers.

nordvpn whitelist add port 22 - Open incoming port 22 (the port number can be different)
nordvpn whitelist remove port 22 - Remove the rule added with the above command
nordvpn settings - See the current settings.
nordvpn status - See the connection status.
nordvpn countries - See the country list.
nordvpn cities - See the city list.
nordvpn groups - See a list of available server groups.
nordvpn logout - Log out.
nordvpn help or nordvpn h - See the list of commands or help for one command.
"""


import subprocess


def main():
    choice = ''
    while choice != "q":
        choice = menu()
        if choice == "c":
            command = subprocess.run(['nordvpn', 'connect'])
        elif choice == "a":
            command = subprocess.run(['nordvpn', 'connect', 'au'])
        elif choice == "d":
            command = subprocess.run(['nordvpn', 'disconnect'])
        elif choice == "s":
            command = subprocess.run(['nordvpn', 'status'])
        else:
            print("Invalid Choice")
        print("\n\n")


def menu():
    choice = input("Please select one of the following:\n"
                   "(C)onnect \n"
                   "(A)ustralia - Connect to Australia\n"
                   "(D)isconnect\n"
                   "(S)tatus\n"
                   "(Q)uit\n"
                   ">>>").lower()
    return choice


main()
