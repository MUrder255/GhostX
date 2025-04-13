import os
import sys
from ai.assistant import Assistant
from hacking_tools.ip_scanner import IPScanner
from game_modding.roblox_modder import RobloxModder
from ui.main_ui import MainUI
from ui.boot_sequence import BootSequence


def handle_command(user_input, ghostx):
    """
    Handle user commands and execute corresponding actions.
    """
    if user_input == "help":
        print("Available commands: help, scan, mod, exit")
    elif user_input == "scan":
        print("Launching IP Scanner...")
        ghostx["ip_scanner"].start_scan()
    elif user_input == "mod":
        print("Launching Roblox Modding Tool...")
        ghostx["roblox_modder"].mod_game()
    elif user_input == "exit":
        print("Exiting GhostX... Goodbye!")
        sys.exit(0)
    else:
        print(f"Unknown command: {user_input}. Type 'help' for a list of commands.")


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
        "ui": ui,
    }


def main():
    """
    Main entry point for GhostX.
    """
    # Display the boot-up sequence
    boot = BootSequence()
    boot.display_boot_sequence()

    # Initialize GhostX system
    ghostx = initialize_ghostx()

    print("Type 'help' for a list of commands.")

    while True:
        try:
            user_input = input("GhostX> ").strip().lower()
            handle_command(user_input, ghostx)
        except KeyboardInterrupt:
            print("\nExiting GhostX. Goodbye!")
            break


if __name__ == "__main__":
    main()
