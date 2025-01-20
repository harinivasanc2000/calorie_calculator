# This Python file uses the following encoding: utf-8
import sys
import string
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow  # Assuming ui_form.py is generated from form.ui


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the "Calculate" button to a method
        self.ui.pushButton.clicked.connect(self.calculate_calories)

    def tokenize_rulebased(self, text):
        prev_c = ' '  # Keep track of the previous character (set as space initially)
        tokens = []

        # Loop through each character in the text
        for c in text:
            if c not in string.whitespace:
                if prev_c in string.whitespace:
                    is_new_token = True
                elif c in string.ascii_letters and prev_c not in string.ascii_letters:
                    is_new_token = True
                elif c in string.punctuation and prev_c not in string.punctuation:
                    is_new_token = True
                elif c in string.digits and prev_c not in string.digits:
                    is_new_token = True
                else:  # Continuation of a token
                    is_new_token = False
                if is_new_token:
                    tokens.append(c)
                else:
                    tokens[-1] += c
            prev_c = c
        return tokens

    def get_text(self):
        # Get the input text from the QTextEdit widget
        return self.ui.textEdit.toPlainText()

    def calorie_splitter(self, text):
        # Tokenize the input text
        food_list = self.tokenize_rulebased(text)

        # Extract and sum up calorie values
        calories = [int(food) for food in food_list if food.isdigit()]
        total_calories = sum(calories)
        return total_calories

    def calculate_calories(self):
        try:
            # Get text from the input box
            input_text = self.get_text()

            # Pass the text to calorie_splitter and calculate the total
            total_calories = self.calorie_splitter(input_text)

            # Display the result on the LCD display
            self.ui.lcdNumber.display(total_calories)
        except Exception as e:
            print(f"Error: {e}")  # For debugging purposes


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
