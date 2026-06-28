import subprocess

class NovaProcessSpawner:
    def __init__(self):
        """
        Constructor: Prepares our process tracking reference variable.
        """
        self.active_game_process = None

    def launch_external_program(self, executable_path: str, argument_list: list) -> bool:
        """
        Takes an executable target (like Java) and a list of structural arguments,
        then boots the application as an independent child process.
        """
        print("PROCESS SPAWNER: Assembling execution command arrays...")
        
        # Combine the executable path and arguments into one master command array
        master_command = [executable_path] + argument_list
        
        print(f"PROCESS SPAWNER: Executing system command -> {' '.join(master_command[:4])} ...")
        
        try:
            # Spawn the process asynchronously
            # stdout/stderr extraction flags will allow us to read game logs later
            self.active_game_process = subprocess.Popen(
                master_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=subprocess.CREATE_NEW_CONSOLE # Opens a dedicated terminal window for the game process
            )
            
            print(f"PROCESS SPAWNER SUCCESS: Independent process spawned with System PID: {self.active_game_process.pid}")
            return True
            
        except Exception as e:
            print(f"PROCESS SPAWNER ERROR: Operating system rejected execution layout assembly: {e}")
            return False