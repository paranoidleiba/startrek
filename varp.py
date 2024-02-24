import random
import time
from tqdm import tqdm
from colorama import Fore, init

def dv_varp():
    init()

    COLORS = [Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    print("---------------------------------------")
    time.sleep(1.0)
    print("Initialization of the warp engine, activation of warp coils..")

    # A function that simulates a long process
    def long_process(n):
        with tqdm(total=n, bar_format="{l_bar}{bar} - {r_bar}") as pbar:
            for i in range(n):
                time.sleep(0.1)
                pbar.update()

    #Launching a function with a progress bar 
    long_process(100)

    def warp_drive():

        # Generating a random number for warp speed
        warp_factor = random.uniform(1, 10)

        # Displaying a message about warp speed
        print(f"Warp drive activated! Warp speed: {warp_factor}")

        # Simulating “flight” at warp speed
        with tqdm(total=10, unit="POWER") as pbar:
            for i in range(10):
                time.sleep(1)
                pbar.update()
                print(COLORS[i % len(COLORS)] + str(pbar), end="", flush=True)
                if i == 9:
                    print(f"\n{Fore.GREEN}Reaching Warp Speed")
                    pbar.__exit__(None, None, None)
                    while True:
                        user_input = input("To exit warp mode, dial \"Ext\": ")
                        if user_input.lower() == "ext":
                            print(f"\n{Fore.YELLOW}Exit from the Warp...")
                            time.sleep(2)
                            print(f"\n{Fore.GREEN}The ship has successfully left the Warp!")
                            break

    # Запускаем имитацию
    warp_drive()