from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox, QPushButton
from PySide6.QtCore import Qt
from core.engine import NovaGameEngine

class NovaLaunchBar(QWidget):
    def __init__(self, version_list: list):
        super().__init__()
        self.engine = NovaGameEngine()
        self.version_list = version_list
        self.init_component()

    def init_component(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 20)
        layout.setSpacing(15)
        self.setLayout(layout)
        
        self.version_selector = QComboBox()
        self.version_selector.setFixedWidth(180)
        self.version_selector.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.version_selector.addItems(self.version_list)
        layout.addWidget(self.version_selector)
        
        self.launch_button = QPushButton("PLAY")
        self.launch_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.launch_button.clicked.connect(self.on_launch_clicked)
        layout.addWidget(self.launch_button)
        
        self.setStyleSheet("""
            QComboBox {
                background-color: #2D2D2D; color: #FFFFFF;
                border: 1px solid #3D3D3D; border-radius: 6px;
                padding: 10px; font-size: 14px; font-weight: bold;
            }
            QComboBox::drop-down { border: none; padding-right: 10px; }
            QPushButton {
                background-color: #2ECC71; color: #FFFFFF; border: none;
                padding: 12px 40px; border-radius: 6px;
                font-size: 18px; font-weight: bold; text-align: center;
            }
            QPushButton:hover { background-color: #27AE60; }
            QPushButton:pressed { background-color: #1E8449; }
        """)

    def update_version_list(self, new_versions: list):
        """
        Clears out old or placeholder dropdown options and loads fresh targets.
        Called cleanly from the main thread thread-pool callback manager.
        """
        # Block signals temporarily to prevent accidental trigger loops while modifying elements
        self.version_selector.blockSignals(True)
        self.version_selector.clear()
        self.version_selector.addItems(new_versions)
        self.version_selector.blockSignals(False)
        print(f"UI CONTROL: Successfully hydrated dropdown menu with {len(new_versions)} entries.")

    def on_launch_clicked(self):
        selected_profile = self.version_selector.currentText()
        self.engine.prepare_launch(selected_profile)