from PyQt5 import QtCore, QtGui, QtWidgets

import launch_init
import widget_left
import widget_right

"Main function of the GUI"


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 493)

        widget_left.setupUi_left(self, Dialog)

        widget_right.setupUi_right(self, Dialog)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Names"))

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)

        self.buddy.clicked.connect(self.buddy_button_clicked)

        launch_init.retranslateUi(self, Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    """
    Function to check if there is enough people to make a pair
    If there is the method is called to make a buddy pair,
    Otherwise a popup message is throw to the user
    :param self: the GUI
    """

    def buddy_button_clicked(self):
        if self.tableWidget.rowCount() > 1:
            widget_right.buddy_button_clicked(self)
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Alert")
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("There is not enough people to make a pair of buddy")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())
