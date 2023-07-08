from PyQt5 import QtWidgets, QtCore, QtGui


class LeftGUI:
    def __init__(self, dialog):
        self.tableWidget = None
        self.lineEdit = None
        self.add = None

        self.dialog = dialog

    def setupUi(self):
        self.dialog.setObjectName("Dialog")

        _translate = QtCore.QCoreApplication.translate

        self.tableWidget = MyTableWidget(self.dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 280, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        # self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item.setText(_translate("Dialog", "Names"))
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setSpan(0, 0, 1, self.tableWidget.columnCount())

        self.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 450, 191, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.add = QtWidgets.QPushButton(self.dialog)
        self.add.setGeometry(QtCore.QRect(225, 455, 75, 24))
        self.add.setObjectName("add")
        self.add.setText(_translate("Dialog", "Add"))

        self.update_table_on_enter(self.lineEdit, self.tableWidget)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)

    def insert_row_with_string(self, string):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        item = QtWidgets.QTableWidgetItem(string)
        self.tableWidget.setItem(row_count, 0, item)

    def update_table_on_enter(self, line_edit, table_widget):
        """
        Function to add a name to the table widget's column after pressing Enter or clicking the Add button.
        :param line_edit: The QLineEdit widget to get the text from.
        :param table_widget: The QTableWidget to add the name to.
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
        self.add.clicked.connect(handle_enter)


class MyTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, position):
        row = self.rowAt(position.y())
        if row >= 0:
            menu = QtWidgets.QMenu(self)
            delete_action = menu.addAction("Delete")
            action = menu.exec_(self.mapToGlobal(position))
            if action == delete_action:
                self.removeRow(row)
