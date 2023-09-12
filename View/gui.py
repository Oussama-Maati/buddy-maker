from PyQt5 import QtCore, QtGui, QtWidgets
from Model.leftgui import LeftGUI
from Model.rightgui import RightGUI


class MainGUI:
    def __init__(self, dialog):
        self.dialog = dialog
        self.left_gui = LeftGUI(dialog)
        self.right_gui = RightGUI(dialog)
        self.left_gui.setupUi()
        self.right_gui.setupUi()
        self.initial_names = ["Oussama", "Kurt", "Itab", "Alexandre", "Nicolay", "Stephan", "Bilal", "Gustavo",
                         "Alejandro", "Mituu", "Meylin", "Olga", "Tristan", "Gokkan", "Wouter", "Cédric"]

    def setupUi(self):
        self.dialog.setObjectName("Dialog")
        self.dialog.resize(620, 510)
        icon = QtGui.QIcon("study.png")
        self.dialog.setWindowIcon(icon)

        _translate = QtCore.QCoreApplication.translate

        item = self.left_gui.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Names"))

        item = QtWidgets.QTableWidgetItem()
        self.right_gui.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.right_gui.tableWidget_2.setHorizontalHeaderItem(1, item)

        self.right_gui.buddy.clicked.connect(self.buddy_button_clicked)

        self.right_gui.delete.clicked.connect(self.delete)

        # self.right_gui.buddies.clicked.connect()

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        self.right_gui.reset.clicked.connect(self.retranslateUi)

    def buddy_button_clicked(self):
        if self.left_gui.tableWidget.rowCount() > 1:
            self.right_gui.buddy_button_clicked(self.left_gui.tableWidget)
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Alert")
            msg_box.setIcon(QtWidgets.QMessageBox.Information)
            msg_box.setText("There is not enough people to make a pair of buddy")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec_()

    def delete(self):
        row_count = self.right_gui.tableWidget_2.rowCount()
        for row in range(row_count):
            self.right_gui.tableWidget_2.removeRow(0)

        row_count = self.left_gui.tableWidget.rowCount()
        for row in range(row_count):
            self.left_gui.tableWidget.removeRow(0)

    def remove_all_names(self):
        row_count = self.left_gui.tableWidget.rowCount()
        for row in range(row_count - 1, -1, -1):
            item = self.left_gui.tableWidget.item(row, 0)
            if item and item.text() != "Names":
                self.left_gui.tableWidget.removeRow(row)

    def retranslateUi(self):
        """
        Function used to initialise the table widget column name with also the names inside
        :param self: The GUI window
        """
        self.delete()

        self.remove_all_names()


        _translate = QtCore.QCoreApplication.translate

        item = self.right_gui.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Buddy 1"))
        self.right_gui.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        item = self.right_gui.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Buddy 2"))
        self.right_gui.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        for name in self.initial_names:
            self.left_gui.insert_row_with_string(name)
