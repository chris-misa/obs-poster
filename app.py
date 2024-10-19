import sys

from PySide6.QtCore import QSize
import PySide6.QtWidgets as QW

class MainWindow(QW.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("OBS Post Creator")
    self.setGeometry(100, 100, 500, 400)

    self.title = QW.QTextEdit()
    self.title.setPlaceholderText("Enter post title here...")
    sizePolicy = QW.QSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Expanding)
    sizePolicy.setVerticalStretch(1)
    self.title.setSizePolicy(sizePolicy)
    self.title.setTabChangesFocus(True)

    self.descr = QW.QTextEdit()
    self.descr.setPlaceholderText("Enter post description here...")
    sizePolicy = QW.QSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Expanding)
    sizePolicy.setVerticalStretch(10)
    self.descr.setSizePolicy(sizePolicy)
    self.descr.setTabChangesFocus(True)

    
    self.create_btn = QW.QPushButton("Create Post")
    self.create_btn.pressed.connect(self.showText)

    create_layout = QW.QVBoxLayout()
    create_layout.addWidget(self.title)
    create_layout.addWidget(self.descr)
    create_layout.addWidget(self.create_btn)

    widget = QW.QWidget()
    widget.setLayout(create_layout)
    self.setCentralWidget(widget)
    self.show()

  def showText(self):
    dlg = QW.QMessageBox(self)
    dlg.setWindowTitle("Info")
    dlg.setText(f""" Read the form values:
    title: {self.title.toPlainText()}
    descr: {self.descr.toPlainText()}
    """)
    dlg.exec()
    

app = QW.QApplication(sys.argv)
w = MainWindow()
app.exec()
