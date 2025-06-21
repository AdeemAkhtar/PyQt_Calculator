# All Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250,300)

# All object/widgets
text_box = QLineEdit()
grid = QGridLayout()


buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]
clear = QPushButton('C')
delete = QPushButton('<')

# Functions

def button_click():
    """
        Handles the logic for calculator button clicks in a PyQt GUI application.

        This function is triggered when any calculator button is clicked.
        It performs actions based on the button's label:
        
        - If the button is '=', it evaluates the expression in the text box using `eval()` and displays the result.
        If the expression is invalid, it displays an error message.
        - If the button is 'C', it clears the text box.
        - If the button is '<', it removes the last character from the current input.
        - Otherwise, it appends the button's label (digit/operator) to the current input.

        Assumes the use of a global or accessible `app.sender()` and a `text_box` object for UI interaction.
    """
    button = app.sender()
    text = button.text()

    if text == '=':
        symbol = text_box.text()

        if len(symbol) > 0:
            try:
                res = eval(symbol)
                text_box.setText(str(res))

            except Exception as e:
                text_box.setText('Error:' + str(e))
        else:
            text_box.setText('0')

    elif text == 'C':
        text_box.clear()

    elif text == '<':
        current_value = text_box.text()
        text_box.setText(current_value[:-1])

    else:
        current_value = text_box.text()
        text_box.setText(current_value + text)

# App Counters
row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)


master_layout.addLayout(button_row)
main_window.setLayout(master_layout)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

# Show/Run
main_window.show()
app.exec_()