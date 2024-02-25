import colorama
import time
from colorama import Fore
from varp import dv_varp
import threading
message = "Enterprise ship initialization sheet NCC1701"
colorama.init()

#-----------------------------------------------------
#this is the countdown for pulse motor operation, this function will be used below
def countdown():
    print(f"\n{Fore.YELLOW}Waiting for one Earth minute before reaching destination...")
    for seconds_left in range(60, 0, -1):
        print(f"\r{seconds_left} seconds left", end="", flush=True)
        time.sleep(1)
    print(f"\n{Fore.GREEN}Stopping the impulse engine...The ship has successfully reached the destination!")

#---------------------------------------------------------------
print(Fore.GREEN + """
__________________           __
\_________________|)____.---'--`---.____
              ||    \----.________.----/
              ||     / /    `--'
            __||____/ /_
           |___________/


""")



print("")
print("")
def activate_systems():
    print("Life support systems:")
    print("")
    systems = [
        "Atmosphere control",
        "Recirculation system",
        "Recycling system",
        "Control systems: navigation, communications, flight control",
        "Security systems: protection, fire extinguishing, emergency warning",
        "Scientific systems and scanners",
    ]

    # Creating a list of activations
    activations = []

    # Searching systems
    for system in systems:
        # Activation request
        user_input = input(f"Activate {system}? (Y/N): ")

        # Input validation
        if user_input.lower() in ("y", "n"):
            activations.append(user_input.lower() == "y")
        else:
            print(f"Invalid command.")
            return

        # Adding visual padding
        print("\n")

    # Checking activation of all systems
    if not activations:
        print(f"{Fore.RED}**Entering incorrect data. Try again.**{Fore.RESET}")
        return
    elif all(activations):
        print(f"{Fore.GREEN}**Systems activated!**{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}**Not all systems are activated!**{Fore.RESET}")


def check_systems():
    systems = [
        "Impulse engines",
        "Warp drive",
        "Reactors",
    ]

    # Creating a list of statuses
    statuses = []

    # Searching systems
    for system in systems:
        # Review request
        user_input = input(f"Check {system}? (Y/N): ")

        # Input validation
        if user_input.lower() in ("y", "n"):
            statuses.append(user_input.lower() == "y")
        else:
            print(f"Invalid command.")
            return

        # Adding visual padding
        print("\n")

    # Displaying test results
    for system, status in zip(systems, statuses):
        if status:
            print(f"{Fore.GREEN}{system}: works fine.{Fore.RESET}")
        else:
            print(f"{Fore.RED}{system}: does not work.{Fore.RESET}")

    # Undocking request
    while True:
        # Undocking request
        user_input = input("Undock from the station? (Y/N): ")

        # input validation
        if user_input.lower() not in ("y", "n"):
            print(f"Invalid command.")
            continue

        # Undocking from the station
        if user_input.lower() == "y":
            print("Undocking from the station...")
            print(Fore.GREEN + """
                               ___
      ___....-----'---'-----....___
=========================================   
       ___'---..._______...---'___          
      (___)      _|_|_|_      (___)                      
        \\____.-'_.---._'-.____//         
          cccc'.__'---'__.'cccc                          
                  ccccc

            
            

      
                  .:.
                 .:::.
                .:::::.
            ***.:::::::.***
       *******.:::::::::.*******       
     ********.:::::::::::.********     
    ********.:::::::::::::.********    
    *******.::::::'***`::::.*******    
    ******.::::'*********`::.******    
     ****.:::'*************`:.****
       *.::'*****************`.*
       .:'  ***************    .
      .
            """)
            break
        else:
            print("Flight is not possible. Try again.")
print("")
print("")

# Running functions


def select_destination():
    print("")
    print("Select your destination:")
    print("a) Alpha Centauri")
    print("b) Andromeda's nebula")
    print("c) Tau Ceti system")
    print("d) Planet Romulus")
    print("")
    # Request to select a destination
    user_input = input("Enter a, b, c or d:")

    # Input validation
    if user_input not in ("a", "b", "c", "d"):
        print("Wrong choice.")
        return None

    # Returning the selected destination
    selected_destination = None
    if user_input == "a":
        print(f"Destination selected: **Alpha Centauri star system**\nAlpha Centauri star system", "A star system located at a distance of 4.37 light years from the Sun.")
        selected_destination = "a"
        
    elif user_input == "b":
        print(f"Destination selected: **Andromeda Galaxy**\nGalaxy Andromeda Nebula", "Galaxy closest to the Milky Way, 2.5 million light years away")
        selected_destination = "b"
        
    elif user_input == "c":
        print(f"Selected destination: **Tau Ceti star system**\nTau Ceti star system", "Star system located 11.9 light years from the Sun")
        selected_destination = "c"
        
    elif user_input == "d":
        print(f"Destination selected: **Planet Romulus**\nHome planet of the Romulans, a hostile race. be careful")
        selected_destination = "d"
    
    return selected_destination

def select_engine(selected_destination):
    print("")
    print("Select engine type:")
    print("a) Impulse engines")
    print("b) Warp drive")
    print("")
    # Request to select engine type
    user_input = input("Enter a or b: ")

    # Input validation
    if user_input not in ("a", "b"):
        print("Wrong choice.")
        return None

    if user_input == "a":
        print(f"Impulse engines is selected. Let's start the flight")
        countdown()  # Запускаем отсчет
        print("You have arrived at your destination.")

    elif user_input == "b":
        #we fly on a varp engine for 1 minutes, start dv_varp() from file varp.py
        dv_varp()
    if selected_destination == "d":
        
        def romulan_warbird():
            print(Fore.GREEN + """
                                      [=========]
                           -==++""" + " .  /. . .  \\ .  " + """++==-
                    -+""   \\   .. . .  | ..  . |  . .  .   /   ""+-
                 /\\  +-""   `-----=====\    /=====-----'   ""-+  /\\
                / /                      ""=""                      \\ \\
              / /                                                     \\ \\
             //                                                         \\\\
            /")                                                         ("\\
            \\o\\                                                         /o/
             \\ )                                                       ( /") 
            """)  

        


            
            print("")
            print("You are greeted by the Romulan Warbird. This is bad news, choose, we will either shoot back or try to escape:")
            print("a) shoot back")
            print("b) try to escape")

            print("")
            
            user_input = input("Enter a or b: ")
            print("")
            # Input validation
            if user_input not in ("a", "b"):
                print("Wrong choice.")
                return None

            # Returning the selected destination
            selected_destination = None
            if user_input == "a":
                print(f"You have damaged an enemy ship and can continue the mission")
            elif user_input == "b":
                print(f"You managed to get away. Congratulations")

        romulan_warbird()        
    else:    
        print("Choose a mission")    

activate_systems()
check_systems()
selected_destination = select_destination()
select_engine(selected_destination)
# nameste()

