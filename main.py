from PyQt5 import QtCore, QtGui, QtWidgets
from gui import MainGUI


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = MainGUI(dialog)
    ui.setupUi()
    dialog.show()

    sys.exit(app.exec_())
