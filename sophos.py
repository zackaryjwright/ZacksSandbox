"""
Sophos commandline shortcuts menu

Status - /opt/sophos-av/bin/savdstatus
Scan Home - savscan /home
logs (las 24hrs) - /opt/sophos-av/bin/savlog --today --utc
update  - /opt/sophos-av/bin/savupdate
Stop - /opt/sophos-av/bin/savdctl disable
Start - /opt/sophos-av/bin/savdctl enable
"""
import subprocess


def main():
    choice = ''
    while choice != "q":
        choice = menu()
        if choice == "s":
            command = subprocess.run(['/opt/sophos-av/bin/savdstatus'])
        elif choice == "h":
            command = subprocess.run(['/opt/sophos-av/bin/savscan', '/home'])
        elif choice == "l":
            command = subprocess.run(['/opt/sophos-av/bin/savlog', '--today', '--utc'])
        elif choice == "u":
            command = subprocess.run(['/opt/sophos-av/bin/savupdate'])
        elif choice == "d":
            command = subprocess.run(['/opt/sophos-av/bin/savdctl', 'disable'])
        elif choice == "e":
            command = subprocess.run(['/opt/sophos-av/bin/savdctl', 'enable'])
        else:
            print("Invalid Choice")
        print("\n\n")


def menu():
    choice = input("Please select one of the following:\n"
                   "(S)tatus - Display the status\n"
                   "(H)ome - Scan the home folder scan\n"
                   "(L)ogs - Display logs for the previous 24Hrs\n"
                   "(U)pdate - Update Sophos immediately\n"
                   "(D)isable - Stop Sophos\n"
                   "(E)nable - Start Sophos\n"
                   ">>>").lower()
    return choice


main()

# completed = subprocess.run(['ls', '-1'])
# print('returncode:', completed.returncode)

# subprocess.check_output("sudo -i -u " + str(username) + " ls -l", shell=True).decode("utf-8").strip()