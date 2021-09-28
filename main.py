from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show() 

#ACTION
        self.setWindowTitle("Notepad Clone")
        self.action12px_2.triggered.connect(lambda: self.change_size(12))
        self.action18px_2.triggered.connect(lambda: self.change_size(18))
        self.action24px_2.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close_file)
   
#FONT SIZE
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))


#OPEN FILE
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options=options)
        if filename != "":
            with open(filename, "r") as f: 
                self.plainTextEdit.setPlainText(f.read())

#SAVE FILE    
    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

#CLOSE FILE   
    def close_file(self, event):
        dialog = QMessageBox()
        dialog.setText("You don't want to lose your work, do you?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)#0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)#1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)#2

        answer = dialog.exec()

        if answer == 0:
            event.ignore()
        elif answer == 2:
            self.save_file()
            event.accept()
        

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

   
if __name__ == '__main__':
    main()
