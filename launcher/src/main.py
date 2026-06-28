#a test comment
#i am making it async so that the UI can load instantly and then the background thread can fetch the data without locking up the interface
#some of the code is based on the PySide6 documentation and examples, but I have modified it to fit my needs

import sys
print("DEBUG: Step 1 - Asynchronous main.py has started.")

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThreadPool # Import the master thread engine pool
from ui.mainwindow import NovaMainWindow
from services.downloader import NovaDownloader
from services.worker import VersionFetchWorker
from utils.parser import NovaDataParser

class NovaLauncher:
    def __init__(self):
        print("DEBUG: Step 2 - Instantiating background thread pools...")
        self.app = QApplication(sys.argv)
        
        # Instantiate our core background systems
        self.downloader = NovaDownloader()
        
        # Open the UI window instantly with default local profiles so the app feels incredibly fast
        initial_placeholders = ["Loading profiles..."]
        print("DEBUG: Step 3 - Spawning visual UI window instantly...")
        self.main_window = NovaMainWindow(initial_placeholders)
        self.main_window.show()
        
        # Start the background data network stream task immediately after boot
        self.trigger_background_version_check()

    def trigger_background_version_check(self):
        """
        Spawns a background thread task to query Mojang's metadata servers
        without locking up the user interface.
        """
        # Create an instance of our background worker
        worker = VersionFetchWorker(self.downloader, NovaDataParser)
        
        # Connect the worker signals to our internal UI update managers
        worker.signals.finished.connect(self.on_versions_loaded_successfully)
        worker.signals.error.connect(self.on_versions_load_failed)
        
        # Hand the job over to the global system ThreadPool engine
        print("DEBUG: Step 4 - Delegating network execution job to QThreadPool worker...")
        QThreadPool.globalInstance().start(worker)

    def on_versions_loaded_successfully(self, clean_versions):
        """
        Triggered automatically when the background thread completes its task.
        Injects the real data straight into the live running interface dropdown.
        """
        print("DEBUG: Background thread finished. Updating UI container layout elements...")
        # Direct call to our main window view container to refresh items
        self.main_window.home_page.launch_bar.update_version_list(clean_versions)

    def on_versions_load_failed(self, error_msg):
        """
        Triggered if the background network operation breaks down.
        """
        print(f"LAUNCHER WARNING: Async profile loading failed: {error_msg}")
        fallback_list = ["Nova Core (Latest)", "Vanilla Stable (Offline)"]
        self.main_window.home_page.launch_bar.update_version_list(fallback_list)

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    launcher = NovaLauncher()
    launcher.run()