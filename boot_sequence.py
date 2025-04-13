import time
import sys
from colorama import init, Fore

init(autoreset=True)


class BootSequence:
    def __init__(self):
        self.lines = [
            "Initializing GhostX Core Modules...",
            "Loading AI Assistant...",
            "Scanning Network Interfaces...",
            "Launching IP Scanner...",
            "Setting up Game Modding Tools...",
            "Finalizing UI Components...",
            "System Integrity Verified ✅",
            "GhostX Boot-Up Complete!"
        ]

    def animate_text(self, text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")

    def show_progress_bar(self, total_steps=8):
        for step in range(total_steps):
            time.sleep(0.5)  # Simulate work
            progress = int((step + 1) / total_steps * 50)
            bar = f"[{'#' * progress}{'.' * (50 - progress)}]"
            sys.stdout.write(f"\r{Fore.LIGHTGREEN_EX}{bar} {step + 1}/{total_steps} steps complete")
            sys.stdout.flush()
        sys.stdout.write("\n")

    def display_boot_sequence(self):
        print(Fore.GREEN + """
  ██████╗  ██████╗  ███████╗████████╗██╗  ██╗
 ██╔═══██╗██╔════╝  ██╔════╝╚══██╔══╝██║  ██║
 ██║   ██║██║  ███╗█████╗     ██║   ███████║
 ██║   ██║██║   ██║██╔══╝     ██║   ██╔══██║
 ╚██████╔╝╚██████╔╝███████╗   ██║   ██║  ██║
  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝
        """)

        print(Fore.LIGHTCYAN_EX + "Welcome to GhostX - The Ultimate AI Toolkit\n")
        time.sleep(1)

        for line in self.lines:
            self.animate_text(Fore.LIGHTGREEN_EX + line)
            time.sleep(0.5)

        print("\nLoading Progress:")
        self.show_progress_bar()
        print(Fore.LIGHTCYAN_EX + "\nLaunching the Main Interface...\n")


if __name__ == "__main__":
    boot = BootSequence()
    boot.display_boot_sequence()
