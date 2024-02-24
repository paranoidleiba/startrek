import colorama
from colorama import Fore
from varp import dv_varp
message = "Enterprise ship initialization sheet NCC1701"
colorama.init()


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
        "Shunting engines",
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
    if user_input == "a":
        print(f"Destination selected: **Alpha Centauri star system**\nAlpha Centauri star system", "A star system located at a distance of 4.37 light years from the Sun.")
        
    elif user_input == "b":
        print(f"Destination selected: **Andromeda Galaxy**\nGalaxy Andromeda Nebula", "Galaxy closest to the Milky Way, 2.5 million light years away")
        
    elif user_input == "c":
        print(f"Selected destination: **Tau Ceti star system**\nTau Ceti star system", "Star system located 11.9 light years from the Sun")
        
    elif user_input == "d":
        print(f"Destination selected: **Planet Romulus**\nHome planet of the Romulans, a hostile race. be careful")
        
def select_engine():
    print("")
    print("Select engine type:")
    print("a) Conventional engine")
    print("b) Warp drive")
    print("")
    # Request to select engine type
    user_input = input("Enter a or b: ")

    # Input validation
    if user_input not in ("a", "b"):
        print("Wrong choice.")
        return None

    if user_input == "a":
        print(f"A conventional engine is selected. Let's start the flight")
    if user_input == "b":
        dv_varp()

            
def nameste():
    print("You have arrived at your destination")
    return



activate_systems()
check_systems()
select_destination()
select_engine()
nameste()

