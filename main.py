import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simple PyQt5 App")
        
        #buat widget
        self.label = QLabel("Halo algonova, ini aplikasi pyqt pertama kita!", self)
        self.button = QPushButton("Klik Saya", self)
        self.button.clicked.connect(self.show_message)
        
        #buat layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def show_message(self):
        QMessageBox.information(self, "Pesan", "Tombol telah diklik!")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())