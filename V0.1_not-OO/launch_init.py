from PyQt5 import QtCore

import widget_left


def retranslateUi(self, Dialog):
    """
    Function used to initialise the table widget column name with also the names inside
    :param self: The GUI window
    """
    _translate = QtCore.QCoreApplication.translate
    # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    # self.buddy.setText(_translate("Dialog", "Make buddy"))
    # self.reset.setText(_translate("Dialog", "Reset"))
    # self.pushButton.setText(_translate("Dialog", "Delete"))

    item = self.tableWidget_2.horizontalHeaderItem(0)
    item.setText(_translate("Dialog", "Buddy 1"))
    item = self.tableWidget_2.horizontalHeaderItem(1)
    item.setText(_translate("Dialog", "Buddy 2"))

    initial_names = ["Oussama", "Kurt", "Itab", "Alexandre", "Nicolay", "Stephan", "Bilal", "Gustavo",
                     "Alejandro", "Mituu", "Meylin", "Olga", "Tristan", "Gokkan", "Wouter", "Cédric"]
    for name in initial_names:
        widget_left.insert_row_with_string(self, name)