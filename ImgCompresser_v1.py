from tkinter import StringVar
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QFileDialog,QWidget, QApplication,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QLineEdit,QButtonGroup,QTextEdit,QGroupBox,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PIL import Image

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('imgc.ui', self)
        self.setWindowTitle("ImgCompresser")
        self.values()
        self.connects()
        self.show()

    def values(self):
        self.dirlist = ""
        self.filenames = []
        self.quality = (20,40,60)
        self.quality_numb = 0
        
    def connects(self):
        self.SelectDir_btn.clicked.connect(self.select_directory)
        self.SelectFile_btn.clicked.connect(self.select_file)
        self.ResetFiles_btn.clicked.connect(self.reset_file)
        self.ResetDir_btn.clicked.connect(self.reset_dir)
        self.EditQuality_btn.clicked.connect(self.edit_quality)
        self.StartBtn.clicked.connect(self.launch)


    def select_directory(self):
        self.dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        self.dirname = self.dirlist[self.dirlist.rfind("/")+1:]
        self.directory_title.setText(self.dirname)

    def select_file(self):
        self.filenames, ok = QFileDialog.getOpenFileNames(self,
                            "Выберите несколько файлов",
                             ".",
                             "All Files(*.*)")
        self.amount_title.setText(f"{len(self.filenames)}")
        
    
    def reset_file(self):
        self.filenames = []
        self.amount_title.setText(f"{len(self.filenames)}")

    def reset_dir(self):
        self.dirlist = ""
        self.directory_title.setText("не выбрано")
    
    def edit_quality(self):
        if self.quality_numb != 2:
            self.quality_numb+=1
        else:
            self.quality_numb=0
        self.ValueQuality.setText(f"{self.quality[self.quality_numb]}%")

    def launch(self):
        try:
            if self.filenames == []:
                QMessageBox.critical(self, "Ошибка ", "Не выбран файл", QMessageBox.Ok)
            elif self.dirlist == "":
                QMessageBox.critical(self, "Ошибка ", "Не выбрана папка сохранения", QMessageBox.Ok)
            else:
                for i in self.filenames:
                    self.savefilename = i[i.rfind('/')+1:i.rfind('.')]
                    convertImage = Image.open(f"{i}")
                    convertImage.save(f"{self.dirlist}/{self.savefilename}_convert.jpg",optimize=True,quality=self.quality[self.quality_numb])
                QMessageBox.information(self,"Статус", "Успешно")
        except:
            QMessageBox.critical(self, "Ошибка ", "Формат файла не поддерживается", QMessageBox.Ok) 

def main():
    app = QApplication([])
    win = MainWindow()
    app.exec_()
main()

