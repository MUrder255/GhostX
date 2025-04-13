import os
import sys

# Import modules from GhostX
from ai.assistant import Assistant
from hacking_tools.ip_scanner import IPScanner
from game_modding.roblox_modder import RobloxModder
from ui.main_ui import MainUI

def initialize_ghostx():
    """
    Initialize the GhostX system and its components.
    """
    print("Initializing GhostX...")
    
    # Initialize modules
    assistant = Assistant()
    ip_scanner = IPScanner()
    roblox_modder = RobloxModder()
    ui = MainUI()

    print("GhostX Initialized!")

    return {
        "assistant": assistant,
        "ip_scanner": ip_scanner,
        "roblox_modder": roblox_modder,
        "ui": ui
    }

def main():
    """
    Main entry point for GhostX.
    """
    print("Welcome to GhostX")
    print("Type 'help' for a list of commands.")

    # Initialize the system
    ghostx = initialize_ghostx()

    while True:
        try:
            user_input = input("GhostX> ").strip().lower()

            if user_input == "exit":
                print("Shutting down GhostX. Goodbye!")
                break
            elif user_input == "help":
                print("Available commands:")
                print("- scan_ip: Scan an IP address")
                print("- roblox_mod: Launch Roblox modder")
                print("- ui: Launch GhostX UI")
                print("- exit: Exit GhostX")
            elif user_input == "scan_ip":
                ghostx["ip_scanner"].scan()
            elif user_input == "roblox_mod":
                ghostx["roblox_modder"].start_modding()
            elif user_input == "ui":
                ghostx["ui"].launch()
            else:
                print("Invalid command. Type 'help' for a list of commands.")
        except KeyboardInterrupt:
            print("\nShutting down GhostX. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
