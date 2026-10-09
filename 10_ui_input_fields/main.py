import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)

        self.button = QPushButton("Submit", self)

        self.label = QLabel("Hello!",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 300, 40)
        self.line_edit.setStyleSheet("font-size: 25px;")
        self.line_edit.setPlaceholderText("Enter Your name...")

        self.button.setGeometry(320, 10, 100, 40)
        self.button.setStyleSheet("font-size: 25px;")
        self.button.clicked.connect(self.submit)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")

    def submit(self):
        print("You clicked the button!")
        text = self.line_edit.text()
        print(f"Hello {text}!")
        self.label.setText(f"Hello {text}!")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
