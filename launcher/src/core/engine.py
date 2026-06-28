import os
import sys
from services.downloader import NovaDownloader
from utils.config import NovaConfigManager
from services.java_detector import NovaJavaDetector
from core.process import NovaProcessSpawner
# Import our final Minecraft Booter service
from core.minecraft_booter import NovaMinecraftBooter

class NovaGameEngine:
    def __init__(self):
        self.appdata_dir = os.getenv("APPDATA") or os.path.expanduser("~")
        self.nova_root = os.path.join(self.appdata_dir, ".novaclient")
        
        if not os.path.exists(self.nova_root):
            os.makedirs(self.nova_root)
            
        self.config_manager = NovaConfigManager(self.nova_root)
        self.downloader = NovaDownloader()
        self.java_detector = NovaJavaDetector()
        self.process_spawner = NovaProcessSpawner()
        
        # Instantiate our final Minecraft Booter service
        self.minecraft_booter = NovaMinecraftBooter(self.nova_root)

    def initialize_environment(self):
        print(f"CORE ENGINE: Verifying local storage directories at {self.nova_root}...")
        sub_folders = ["versions", "mods", "configs", "logs"]
        for folder in sub_folders:
            target_path = os.path.join(self.nova_root, folder)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
                print(f"CORE ENGINE: Created missing directory -> {folder}")
            else:
                print(f"CORE ENGINE: Verified folder structure -> {folder}")

    def prepare_launch(self, profile_name: str):
        print(f"CORE ENGINE: Commencing pre-flight sequence for profile: [{profile_name}]")
        
        # 1. Run folder verification
        self.initialize_environment()
        
        # 2. Check and ensure the game jar file wrapper exists
        file_check = self.minecraft_booter.verify_game_files()
        if not file_check:
            print("CORE ENGINE ERROR: Game asset validation failed. Aborting launch sequence.")
            return False
        
        # 3. Load configuration limits
        current_settings = self.config_manager.load_config()
        allocated_ram = current_settings.get("allocated_ram_mb", 4096)
        
        # 4. Target Java execution path
        java_path = self.java_detector.locate_java_runtime()
        if not java_path:
            print("CORE ENGINE ERROR: Aborting launch sequence. Java runtime is missing.")
            return False
            
        # 5. Build full Minecraft startup arguments dynamically!
        runtime_arguments = self.minecraft_booter.build_launch_arguments(profile_name, allocated_ram)
        
        # 6. Fire up the game process engine live!
        print("CORE ENGINE: System handshake complete. Spawning active game process layout window...")
        return self.process_spawner.launch_external_program(java_path, runtime_arguments)