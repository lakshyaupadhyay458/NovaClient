import os
import json

class NovaConfigManager:
    def __init__(self, nova_root_dir: str):
        """
        Constructor: Pinpoints where our local persistent configurations file should live.
        """
        self.config_filepath = os.path.join(nova_root_dir, "launcher_config.json")
        # Define default production configurations matching our PvP philosophy
        self.default_settings = {
            "game_directory": nova_root_dir,
            "allocated_ram_mb": 4096,          # 4GB RAM default: optimal for PvP/Survival
            "selected_profile": "Nova Core (Latest)",
            "java_path": "default",
            "fullscreen_enabled": True
        }
        # Run an initial health check to ensure our configuration file exists
        self.load_config()

    def load_config(self) -> dict:
        """
        Reads our custom JSON settings file from the disk. 
        If the file is missing or corrupted, it automatically generates a fresh one with safe defaults.
        """
        if not os.path.exists(self.config_filepath):
            print("UTILS CONFIG: Config file missing. Generating fresh defaults...")
            self.save_config(self.default_settings)
            return self.default_settings

        try:
            with open(self.config_filepath, "r") as file:
                data = json.load(file)
                print("UTILS CONFIG: Configuration data loaded successfully from storage disk.")
                return data
        except (json.JSONDecodeError, IOError) as e:
            print(f"UTILS CONFIG WARNING: Corrupted configurations file encountered. resetting defaults. Error: {e}")
            self.save_config(self.default_settings)
            return self.default_settings

    def save_config(self, settings_dict: dict) -> bool:
        """
        Takes a running settings configuration dictionary and serializes it out cleanly onto the physical drive disk.
        """
        try:
            with open(self.config_filepath, "w") as file:
                # json.dump takes our data, our target file pointer, and indents it by 4 spaces for elegant readability
                json.dump(settings_dict, file, indent=4)
                print("UTILS CONFIG: State file flushed and written to disk successfully.")
                return True
        except IOError as e:
            print(f"UTILS CONFIG ERROR: Failed to write custom configuration layout data to disk: {e}")
            return False