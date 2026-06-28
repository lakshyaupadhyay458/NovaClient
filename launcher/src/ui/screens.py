from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from ui.launch_bar import NovaLaunchBar

class HomeScreen(QWidget):
    def __init__(self, version_list: list):
        """
        Constructor accepts the version array list parameters passed down from Main Window.
        """
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        layout.addStretch(1)
        
        title = QLabel("Nova Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold;")
        layout.addWidget(title)
        
        subtitle = QLabel("Select a profile from the sidebar to begin your session.")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #888888; font-size: 14px;")
        layout.addWidget(subtitle)
        
        layout.addStretch(1)
        
        # Instantiate launch bar panel, feeding it the targeted versions
        self.launch_bar = NovaLaunchBar(version_list)
        layout.addWidget(self.launch_bar)

class PvPProfileScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        title = QLabel("PvP Profile Configuration")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

class SettingsScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        title = QLabel("Launcher Settings")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)