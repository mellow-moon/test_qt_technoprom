import os

from PySide2 import QtWidgets, QtCore

from ui import file_browser


class FileBrowser(file_browser.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(FileBrowser, self).__init__()
        self.setupUi(self)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(
                                                    os.getcwd()
                                                    ))
        self.treeView.setSortingEnabled(True)

        self.treeView.setColumnWidth(0, 350)

        self.treeView.doubleClicked.connect(self.open_file)

        # self.showMaximized()

    def open_file(self):
        item = self.treeView.selectedIndexes()[0]
        file_path = self.model.filePath(item)

        if not os.path.isdir(file_path):
            os.startfile(file_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    file_browser = FileBrowser()
    file_browser.show()
    app.exec_()
