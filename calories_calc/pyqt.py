from PyQt5.QtWidgets import QApplication, QLabel,QWidget, QMainWindow,QPushButton
from PyQt5.QtGui import QFont
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,500,500,500)
        self.initUI()
        
        label = QLabel("Calories Calculator",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        
    def initUI(self):
        button = QPushButton("Calculate",self)
        button.setGeometry(150,150,150,150)
        
    def Calculate(self):
        
        
        
def main():
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()