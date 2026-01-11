import time
import sys

def loading_screen():
    for percent in range(101):
        # At 99% show Outstron
        if percent == 99:
            sys.stdout.write("\rOutstron  99%")
        else:
            sys.stdout.write(f"\rLoading {percent}%")
        sys.stdout.flush()
        time.sleep(0.05)  # speed of loading

    # Finish
    time.sleep(0.5)
    print("\nDone! Game Started!")

def start_game():
    print("Welcome to the Game!")
    input("Press Enter to Start...")
    loading_screen()
    # Here you can add the rest of your game logic
    print("Game is running... (put your game code here)")

if __name__ == "__main__":
    start_game()
