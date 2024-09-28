import subprocess
import sys
import os

def is_program_running(program_name):
    try:
        # Using the tasklist command to get the list of running processes
        output = subprocess.check_output(['tasklist']).decode()
        return program_name.lower() in output.lower()
    except subprocess.CalledProcessError:
        return False

# Ensure the script is running on Windows
if os.name != 'nt':
    print("This script is designed to run on Windows.")
    sys.exit()

program_name = 'cs2.exe'  # Change this to the name of the program you want to check
if is_program_running(program_name):
    print(f"{program_name} is running.")
else:
    print(f"{program_name} is not running.")
    sys.exit()

print("Type 1 to enable aimhack")
print("Type 0 to disable aimhack")

while True:
    hack = input("Aimhack: ")
    if hack.isdigit():
        hack = int(hack)
        if hack == 1:
            print("Aimhack enabled. Relaunch script to disable")
            break
        elif hack == 0:
            print("Aimhack disabled.")
            break
        else:
            print("Invalid input. Please enter 1 or 0.")
    else:
        print("Invalid input. Please enter a number.")

sys.exit()