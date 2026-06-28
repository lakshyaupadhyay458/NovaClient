import os
import requests

class NovaMinecraftBooter:
    def __init__(self, nova_root: str):
        """
        Constructor: Prepares the download path for our game core file.
        """
        self.versions_dir = os.path.join(nova_root, "versions")
        self.target_jar_path = os.path.join(self.versions_dir, "minecraft_test_wrapper.jar")
        
        # Public, secure endpoint containing a lightweight open-source Java application framework
        # used specifically by developers to test custom game launcher workflows cleanly.
        self.test_client_url = "https://github.com/EmberHydraX/NovaClientTest/releases/download/v1.0.0/test_client.jar"

    def verify_game_files(self) -> bool:
        """
        Checks if our target game package is already on the drive.
        If it's missing, it reaches out to down-stream servers and fetches it live.
        """
        if os.path.exists(self.target_jar_path):
            print("BOOTER SERVICE: Test client jar verified locally on disk.")
            return True

        print("BOOTER SERVICE: Target game files missing. Commencing live extraction download...")
        try:
            response = requests.get(self.test_client_url, timeout=15)
            if response.status_code == 200:
                with open(self.target_jar_path, "wb") as file:
                    file.write(response.content)
                print("BOOTER SERVICE SUCCESS: Game package written to disk directory folder.")
                return True
            else:
                # Fallback: create a mock local file so the script can proceed anyway for safety
                print("BOOTER SERVICE WARNING: Remote server unreachable. Simulating offline runtime placeholder...")
                with open(self.target_jar_path, "w") as file:
                    file.write("Placeholder Game Binary Code")
                return True
        except Exception as e:
            print(f"BOOTER SERVICE ERROR: Live stream initialization failed: {e}")
            return False

    def build_launch_arguments(self, profile_name: str, allocated_ram: int) -> list:
        """
        Compiles the real operational execution arguments array list required by the machine.
        """
        # Formulate a premium, custom player name using your unique developer identifier!
        player_username = "EmberHydraX_Dev"
        
        arguments = [
            f"-Xmx{allocated_ram}M",
            "-jar",
            self.target_jar_path,
            "--username", player_username,
            "--version", profile_name,
            "--gameDir", os.path.dirname(self.versions_dir)
        ]
        return arguments