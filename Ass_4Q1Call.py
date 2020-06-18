#GUI
import sys
from Ass4Q1 import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.countButton, QtCore.SIGNAL('clicked()'),self.dispCount)

    def dispCount(self):
        sport = self.ui.sportInput.text()
        character = self.ui.characterInput.text()
        count = sport.upper().count(character.upper())
        self.ui.displayLabel.setText('The number of occurence of that is character is: '+str(count))

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec())
