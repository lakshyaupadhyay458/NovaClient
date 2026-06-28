import os
import shutil
import subprocess

class NovaJavaDetector:
    def __init__(self):
        """
        Constructor: Prepares standard fallback search paths common on Windows systems.
        """
        self.common_windows_paths = [
            r"C:\Program Files\Java",
            r"C:\Program Files\Eclipse Adoptium",
            r"C:\Program Files\Microsoft\Jdk"
        ]

    def locate_java_runtime(self) -> str:
        """
        Scans the operating system to find a valid, executable Java path.
        Returns the full path string if found, or an empty string if completely missing.
        """
        print("JAVA DETECTOR: Commencing system-wide runtime scanning...")

        # 1. First Check: Look inside the user's global system PATH shortcuts
        global_java = shutil.which("java")
        if global_java:
            print(f"JAVA DETECTOR: Found globally registered runtime execution path -> {global_java}")
            return global_java

        # 2. Second Check: Look inside standard installation folders (Windows focus)
        print("JAVA DETECTOR: Global path check empty. Scanning common file system directories...")
        for base_path in self.common_windows_paths:
            if os.path.exists(base_path):
                # Walk through the folder structure looking for 'java.exe'
                for root, dirs, files in os.walk(base_path):
                    if "java.exe" in files:
                        full_path = os.path.join(root, "java.exe")
                        print(f"JAVA DETECTOR: Located valid local runtime binary -> {full_path}")
                        return full_path

        print("JAVA DETECTOR ERROR: No valid Java installation found on this machine.")
        return ""