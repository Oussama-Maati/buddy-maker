import random

from PyQt5 import QtCore, QtGui, QtWidgets


def setupUi_right(self, Dialog):
    """
    Function used to implements all the widgets on the Right
    to be displayed on the main GUI
    :param self: the GUI window
    :param Dialog: The Dialog of the setupUI
    """
    self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
    self.tableWidget_2.setGeometry(QtCore.QRect(275, 31, 301, 411))
    self.tableWidget_2.setObjectName("tableWidget_2")
    self.tableWidget_2.setColumnCount(2)
    self.tableWidget_2.setRowCount(0)

    self.buddy = QtWidgets.QPushButton(Dialog)
    self.buddy.setGeometry(QtCore.QRect(340, 460, 75, 24))
    self.buddy.setObjectName("buddy")

    self.reset = QtWidgets.QPushButton(Dialog)
    self.reset.setGeometry(QtCore.QRect(420, 460, 75, 24))
    self.reset.setObjectName("reset")
    self.pushButton = QtWidgets.QPushButton(Dialog)
    self.pushButton.setGeometry(QtCore.QRect(500, 460, 75, 24))
    self.pushButton.setObjectName("pushButton")

    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "Buddy Maker ! (Made by Oussama Maati @becode)"))
    self.buddy.setText(_translate("Dialog", "Make buddy"))
    self.reset.setText(_translate("Dialog", "Reset"))
    self.pushButton.setText(_translate("Dialog", "Delete"))



def buddy_button_clicked(self):
    """
    Function for create a buddy,
    Look in the left tableWidget the column Names and get all of the strings into a var
    Then randomnly takes 2 names that are not the same and put them in the right tableWidget
    One is put under buddy 1 and the other under buddy 2
    :param self: the GUI window
    """
    print("Buddy button clicked!")
    names = []
    row_count = self.tableWidget.rowCount()
    for row in range(row_count):
        item = self.tableWidget.item(row, 0)
        name = item.text()
        names.append(name)
    print(names)
    buddy1 = random.choice(names)
    buddy2 = random.choice(names)
    while buddy2 == buddy1:
        buddy2 = random.choice(names)

    row_count = self.tableWidget_2.rowCount()
    self.tableWidget_2.insertRow(row_count)
    item = QtWidgets.QTableWidgetItem(buddy1)
    self.tableWidget_2.setItem(row_count, 0, item)

    remove_string_from_table(self.tableWidget, buddy1)

    item = QtWidgets.QTableWidgetItem(buddy2)
    self.tableWidget_2.setItem(row_count, 1, item)

    remove_string_from_table(self.tableWidget, buddy2)





def remove_string_from_table(table_widget, string):
    """
    Function to remove in a tableWidget a given name as string
    :param table_widget
    """
    items = table_widget.findItems(string, QtCore.Qt.MatchExactly)
    for item in items:
        if item.column() == 0:
            row = item.row()
            table_widget.removeRow(row)
