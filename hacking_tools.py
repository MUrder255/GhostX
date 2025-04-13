import socket

class IPScanner:z
    def start_scan(self):
        """
        Perform a basic IP scan on the local network.
        """
        print("IP Scanner: Starting scan...")
        target = "127.0.0.1"  # Replace with actual target IP or range
        try:
            print(f"Scanning target: {target}")
            for port in range(1, 1025):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    result = s.connect_ex((target, port))
                    if result == 0:
                        print(f"Port {port} is open.")
            print("IP Scanner: Scan complete!")
        except Exception as e:
            print(f"An error occurred during the scan: {e}")
