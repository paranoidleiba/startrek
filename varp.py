import random
import time
import threading
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
                    # Start a new thread for the countdown
                    countdown_thread = threading.Thread(target=countdown)
                    countdown_thread.start()

                    # Wait for the countdown to finish or user input
                    countdown_thread.join()

    def countdown():
        print(f"\n{Fore.YELLOW}Waiting for one Earth minute before reaching destination...")
        for seconds_left in range(30, 0, -1):
            print(f"\r{seconds_left} seconds left", end="", flush=True)
            time.sleep(1)
        print(f"\n{Fore.GREEN}Exiting from Warp...The ship has successfully reached the destination!")

    # Запускаем имитацию
    warp_drive()