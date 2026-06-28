from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from ui.sidebar import NovaSidebar
from ui.screens import HomeScreen, PvPProfileScreen, SettingsScreen

class NovaMainWindow(QMainWindow):
    def __init__(self, version_list: list):
        """
        Constructor now accepts a computed dynamic version list parameter from core.
        """
        super().__init__()
        self.setWindowTitle("Nova Client Launcher - Alpha v0.1.0")
        self.resize(800, 500)
        
        # Store our version list directly inside the instance memory space
        self.version_list = version_list
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        master_layout = QHBoxLayout()
        master_layout.setContentsMargins(0, 0, 0, 0)
        master_layout.setSpacing(0)
        central_widget.setLayout(master_layout)
        
        self.sidebar = NovaSidebar()
        master_layout.addWidget(self.sidebar)
        self.sidebar.navigation_requested.connect(self.change_screen)
        
        self.screen_container = QStackedWidget()
        
        # Pass the global version list explicitly to the Home Screen setup code block
        self.home_page = HomeScreen(self.version_list)
        self.pvp_page = PvPProfileScreen()
        self.survival_page = HomeScreen(self.version_list) 
        self.settings_page = SettingsScreen()
        
        self.screen_container.addWidget(self.home_page)       
        self.screen_container.addWidget(self.pvp_page)        
        self.screen_container.addWidget(self.survival_page)   
        self.screen_container.addWidget(self.settings_page)   
        
        master_layout.addWidget(self.screen_container)
        
        self.setStyleSheet("""
            QMainWindow { background-color: #121212; }
        """)

    def change_screen(self, index):
        self.screen_container.setCurrentIndex(index)