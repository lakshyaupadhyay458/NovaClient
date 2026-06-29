import os
import subprocess
import minecraft_launcher_lib

class NovaMinecraftBooter:
    def __init__(self, nova_root: str):
        """
        Constructor: Connects your launcher folder directory paths to the real game files.
        """
        self.nova_root = nova_root
        self.versions_dir = os.path.join(nova_root, "versions")

    def verify_game_files(self) -> bool:
        # The launcher library will handle file health checks dynamically during launch
        return True

    def build_launch_arguments(self, profile_name: str, allocated_ram: int) -> list:
        """
        Downloads missing official Mojang files and assembles the exact command array.
        """
        # Ensure the clean version string format (e.g., "1.21")
        target_version = str(profile_name).strip()
        print(f"BOOTER SERVICE: Synchronizing official files for Minecraft {target_version}...")
        
        # 1. Automatically download missing game jars, libraries, and assets from Mojang safely
        # showing live console feedback
        callback = {
            "setStatus": lambda text: print(f"[DOWNLOAD STATUS]: {text}"),
            "setProgress": lambda progress: print(f"[DOWNLOAD PROGRESS]: {progress}%"),
            "setMax": lambda max_val: None
        }
        
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=target_version,
            minecraft_directory=self.nova_root,
            callback=callback
        )

        # 2. Configure our custom offline player login profiles parameters
        options = {
            "username": "EmberHydraX_Dev",
            "uuid": "00000000-0000-0000-0000-000000000000",
            "token": "0",
            "jvmArguments": [f"-Xmx{allocated_ram}M", f"-Xms{allocated_ram}M"]
        }

        # 3. Compile the true command arguments list from the library array engine
        print("BOOTER SERVICE: Compiling official startup arguments...")
        command = minecraft_launcher_lib.command.get_minecraft_command(
            version=target_version,
            minecraft_directory=self.nova_root,
            options=options
        )
        
        return command
    