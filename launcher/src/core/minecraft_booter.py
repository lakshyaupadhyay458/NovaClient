import os

class NovaMinecraftBooter:
    def __init__(self, nova_root: str):
        """
        Constructor: Points directly to our compiled custom Java client build directory.
        """
        self.versions_dir = os.path.join(nova_root, "versions")
        
        # Point the path directly to your newly compiled Java Client development package!
        self.target_jar_path = r"C:\Users\Lakshya\NovaClient\client\build\libs\client-1.0.0-Alpha.jar"

    def verify_game_files(self) -> bool:
        """
        Ensures our custom client jar exists in the build directory before launching.
        """
        if os.path.exists(self.target_jar_path):
            print("BOOTER SERVICE: Custom Nova Client compiled jar verified in build directory.")
            return True
        else:
            print("BOOTER SERVICE ERROR: Compiled client-1.0.0-Alpha.jar missing! Run '.\\gradlew.bat jar' first.")
            return False

    def build_launch_arguments(self, profile_name: str, allocated_ram: int) -> list:
        """
        Compiles execution arguments telling Java to run our custom NovaCore master class.
        """
        arguments = [
            f"-Xmx{allocated_ram}M",
            "-cp", self.target_jar_path,        # Classpath flag: points Java to our archive
            "com.novaclient.NovaCore"            # Main-Class path: tells Java which file to execute first
        ]
        return arguments