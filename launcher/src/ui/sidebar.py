from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal # Import Signal to broadcast event updates

class NovaSidebar(QWidget):
    # Create a custom Event Signal that transmits an integer (the screen index number)
    # when a user clicks a button.
    navigation_requested = Signal(int)

    def __init__(self):
        super().__init__()
        self.init_component()

    def init_component(self):
        self.setFixedWidth(180)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setSpacing(15)
        self.setLayout(layout)
        
        nav_items = ["Home", "PvP Profile", "Survival", "Settings"]
        
        for index, item in enumerate(nav_items):
            btn = QPushButton(item)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            
            # This complex-looking line connects the button click event to a function.
            # It uses a 'lambda' function to send that button's specific position number (index)
            btn.clicked.connect(lambda checked=False, i=index: self.on_button_clicked(i))
            
            layout.addWidget(btn)
            
        layout.addStretch()

        self.setStyleSheet("""
            QWidget { background-color: #1E1E1E; }
            QPushButton {
                background-color: #2D2D2D; color: #E0E0E0;
                border: none; padding: 10px; border-radius: 5px;
                font-size: 14px; font-weight: bold; text-align: left;
            }
            QPushButton:hover { background-color: #3D3D3D; color: #FFFFFF; }
            QPushButton:pressed { background-color: #4D4D4D; }
        """)

    def on_button_clicked(self, index):
        """
        Triggered whenever any sidebar button is pressed.
        Broadcasts the requested index upward to the main window.
        """
        # Emit our navigation signal with the page index number
        self.navigation_requested.emit(index)