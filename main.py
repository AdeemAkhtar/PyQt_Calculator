# All Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

# Class CalculatorApp
class CalculatorApp(QWidget):
    """
        A simple PyQt5 calculator application window.
        This class sets up the main window, initializes the display text box,
        and prepares a grid layout for calculator buttons.
    """
    def __init__(self):
        super().__init__()

        # App Settings
        self.setWindowTitle("Calculator App")
        self.resize(250,300)

        # All object/widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.grid = QGridLayout()


        self.buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '+', '='
        ]

        # App Counters
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding:10px; margin:10px}")
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton('C')
        self.delete = QPushButton('<')

        self.left_para = QPushButton('(')
        self.right_para = QPushButton(')')

        self.clear.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px; margin:10px}")
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px; margin:10px}")
        self.left_para.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px; margin:10px}")
        self.right_para.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px; margin:10px}")

        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        # Paranthesis Buttons
        button_para_row = QHBoxLayout()
        button_para_row.addWidget(self.left_para)
        button_para_row.addWidget(self.right_para)
        master_layout.addLayout(button_para_row)

        # Clear and Delet Buttons
        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)
        self.left_para.clicked.connect(self.button_click)
        self.right_para.clicked.connect(self.button_click)
        
    # Functions
    def button_click(self):
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
            symbol = self.text_box.text()

            if len(symbol) > 0:
                try:
                    res = eval(symbol)
                    self.text_box.setText(str(res))

                except Exception as e:
                    self.text_box.setText('Error:' + str(e))
            else:
                self.text_box.setText('0')

        elif text == 'C':
            self.text_box.clear()

        elif text == '<':
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

# Show/Run
if __name__ in "__main__":
    app = QApplication([])
    main_window = CalculatorApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8}")
    main_window.show()
    app.exec_()