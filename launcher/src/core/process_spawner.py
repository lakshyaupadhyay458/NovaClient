import subprocess
import shlex
import threading

class NovaProcessSpawner:
    def __init__(self):
        pass

    def launch_game(self, command_array: list) -> bool:
        """
        Executes the Java client process arrays and attaches a live log reading thread.
        """
        print("PROCESS SPAWNER: Assembling execution command arrays...")
        
        # Flatten command array safely for Windows systems
        command_string = " ".join(command_array)
        print(f"PROCESS SPAWNER: Executing system command -> {command_string}")

        try:
            # 1. Attach standard output redirect pipes (stdout & stderr)
            process = subprocess.Popen(
                command_array,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True, # Forces the text pipe to decode into strings automatically
                bufsize=1 # Line-buffered streaming
            )
            
            print(f"PROCESS SPAWNER SUCCESS: Independent process spawned with System PID: {process.pid}")

            # 2. Spawn a background thread to prevent reading logs from freezing your main launcher UI window
            output_thread = threading.Thread(
                target=self._stream_logs, 
                args=(process,), 
                name="Nova-LogStream-Thread",
                daemon=True
            )
            output_thread.start()
            return True

        except Exception as e:
            print(f"PROCESS SPAWNER ERROR: Failed to execute system shell binaries: {str(e)}")
            return False

    def _stream_logs(self, process):
        """
        Continuously captures line readouts from our active running Java client container.
        """
        # Read lines sequentially as the Java client emits them
        for line in iter(process.stdout.readline, ''):
            if line:
                print(f"[JAVA CLIENT]: {line.strip()}")
                
        # Handle error stream logs if something crashes inside the JVM
        for error_line in iter(process.stderr.readline, ''):
            if error_line:
                print(f"[JAVA ENGINE CRITICAL]: {error_line.strip()}")
                
        process.stdout.close()
        process.stderr.close()