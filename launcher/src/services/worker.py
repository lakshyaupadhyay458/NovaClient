from PySide6.QtCore import QRunnable, QObject, Signal

class WorkerSignals(QObject):
    """
    Defines the signals available from a running background worker thread.
    We need this extra class because QRunnable cannot directly emit signals.
    """
    # Emits the clean list of parsed version strings when finished
    finished = Signal(list)
    # Emits an error message string if something goes wrong
    error = Signal(str)

class VersionFetchWorker(QRunnable):
    """
    A lightweight, dedicated worker instance that handles downloading and 
    parsing the Minecraft versions list completely in the background.
    """
    def __init__(self, downloader_instance, parser_class):
        super().__init__()
        self.downloader = downloader_instance
        self.parser = parser_class
        self.signals = WorkerSignals()

    def run(self):
        """
        The core logic execution loop that runs entirely on a background thread.
        """
        print("ASYNC WORKER: Starting background version data acquisition stream...")
        try:
            # 1. Reach out to the web network
            raw_manifest = self.downloader.fetch_available_versions()
            if raw_manifest:
                # 2. Parse the data strings
                clean_releases = self.parser.extract_release_versions(raw_manifest)
                # 3. Broadcast the results back to the main UI thread safely
                self.signals.finished.emit(clean_releases)
            else:
                self.signals.error.emit("Server manifest payload returned empty.")
        except Exception as e:
            # Safely trap exceptions so the entire client doesn't crash
            self.signals.error.emit(str(e))