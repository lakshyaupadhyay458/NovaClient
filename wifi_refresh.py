import subprocess
import sys
import time

def run_command(command):
    """Utility function to run system commands and print output."""
    try:
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}", file=sys.stderr)

def refresh_network():
    print("⚡ Starting Wi-Fi Optimization & Refresh...\n")
    
    # 1. Flush DNS Cache (Fixes website loading drops)
    print("--- [1/3] Flushing DNS Cache ---")
    run_command(["ipconfig", "/flushdns"])
    
    # 2. Release current IP address
    print("--- [2/3] Releasing IP Address ---")
    run_command(["ipconfig", "/release"])
    
    # Small pause to let the system process
    time.sleep(2)
    
    # 3. Renew IP address (Grabs a fresh lease from your router)
    print("--- [3/3] Renewing IP Address ---")
    run_command(["ipconfig", "/renew"])
    
    print("✅ Network refresh complete! Your connection should feel snappier.")

if __name__ == "__main__":
    # Check if running on Windows
    if sys.platform.startswith("win"):
        refresh_network()
    else:
        print("❌ This specific script is tailored for Windows. macOS/Linux require different terminal commands.")