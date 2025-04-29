# Import Modules
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

# Main App Objects and Setttings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Game")
main_window.resize(300, 200)

# Create All App Object
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

my_words = ["Hello", "GoodBye", "Test", "Python", "PyQt", "Code"]

# All Design Here
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Events
row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1, alignment=Qt.AlignCenter)
row3.addWidget(button2, alignment=Qt.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignCenter)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


# Add functions
def display_word1(): 
    word = choice(my_words)
    text1.setText(word)

def display_word2(): 
    word = choice(my_words)
    text2.setText(word)

def display_word3(): 
    word = choice(my_words)
    text3.setText(word)


button1.clicked.connect(display_word1)
button2.clicked.connect(display_word2)
button3.clicked.connect(display_word3)



# Show/Run App
main_window.show()
app.exec_()