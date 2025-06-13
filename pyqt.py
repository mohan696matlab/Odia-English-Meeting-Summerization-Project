from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget

class AnomalyDetectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anomaly Detection Desktop App")
        self.layout = QVBoxLayout()

        self.load_button = QPushButton("Load Object Class Folder")
        self.load_button.clicked.connect(self.load_folder)
        self.layout.addWidget(self.load_button)

        self.eval_button = QPushButton("Run Detection")
        self.eval_button.clicked.connect(self.run_detection)
        self.layout.addWidget(self.eval_button)

        self.status = QLabel("Status: Ready")
        self.layout.addWidget(self.status)

        self.setLayout(self.layout)

    def load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.status.setText(f"Selected: {folder}")
            # Store folder path, parse images, etc.

    def run_detection(self):
        self.status.setText("Running detection...")
        # Call your functions here
        # Update GUI or show results
        self.status.setText("Done")

app = QApplication([])
window = AnomalyDetectionApp()
window.show()
app.exec_()
