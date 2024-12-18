from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
import sys


def background_change(background: str):
    if "." in background:
        background_img = "QMainWindow {background-image: url("+background+")}"
        window.setStyleSheet(background_img)
    else:
        background_color = "QMainWindow {background-color: "+background+"}"
        window.setStyleSheet(background_color)


app = QApplication(sys.argv)

window = QMainWindow()
layout = QVBoxLayout()
central_widget = QWidget()

button = QPushButton("Изменить фон")
line_edit = QLineEdit("")

central_widget.setLayout(layout)

button.clicked.connect(lambda: background_change(line_edit.text()))

layout.addWidget(line_edit)
layout.addWidget(button)

window.setCentralWidget(central_widget)

window.show()
app.exec()
