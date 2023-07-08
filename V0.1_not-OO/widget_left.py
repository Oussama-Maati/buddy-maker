from PyQt5 import QtCore, QtGui, QtWidgets

def setupUi_left(self, Dialog):
    """
    Function to implement the left part of the GUI
    :param self: The GUI window
    :param Dialog:
    """
    Dialog.setObjectName("Dialog")
    Dialog.resize(599, 493)

    _translate = QtCore.QCoreApplication.translate


    self.tableWidget = QtWidgets.QTableWidget(Dialog)
    self.tableWidget.setGeometry(QtCore.QRect(30, 30, 211, 411))
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(1)
    self.tableWidget.setRowCount(0)

    self.lineEdit = QtWidgets.QLineEdit(Dialog)
    self.lineEdit.setGeometry(QtCore.QRect(30, 450, 191, 31))
    self.lineEdit.setObjectName("lineEdit")

    self.add = QtWidgets.QPushButton(Dialog)
    self.add.setGeometry(QtCore.QRect(225, 455, 75, 24))
    self.add.setObjectName("add")
    self.add.setText(_translate("Dialog", "Add"))

    update_table_on_enter(self.lineEdit, self.tableWidget)

    item = QtWidgets.QTableWidgetItem()
    font = QtGui.QFont()
    font.setBold(True)
    item.setFont(font)
    self.tableWidget.setHorizontalHeaderItem(0, item)


def update_table_on_enter(line_edit, table_widget):
    """
    Function to add a neames to the right column after pressing enter
    :param line_edit:
    :param table_widget:
    :return:
    """
    def handle_enter():
        text = line_edit.text()
        if text:
            row_count = table_widget.rowCount()
            table_widget.insertRow(row_count)
            item = QtWidgets.QTableWidgetItem(text)
            table_widget.setItem(row_count, 0, item)
            line_edit.clear()

    line_edit.returnPressed.connect(handle_enter)


def insert_row_with_string(self, string):
    row_count = self.tableWidget.rowCount()
    self.tableWidget.insertRow(row_count)
    item = QtWidgets.QTableWidgetItem(string)
    self.tableWidget.setItem(row_count, 0, item)
