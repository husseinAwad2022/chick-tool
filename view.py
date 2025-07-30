import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QGridLayout, QLabel
from PyQt5.QtGui import  QColor, QPalette

class View:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.grid = QGridLayout()
        self.edit1 = QTextEdit()
        self.edit2 = QTextEdit()
        self.label1 = QLabel()
        self.label2 = QLabel()

    def show(self, file1, file2, results):
        self._setup_window(file1, file2)
        self._populate_edits(results)
        self.window.show()
        sys.exit(self.app.exec_())

    def _setup_window(self, file1, file2):
        self.window.setWindowTitle('Diff Tool')
        self.window.setLayout(self.grid)
        self.label1.setText(file1)
        self.label2.setText(file2)
        self.grid.addWidget(self.label1, 0, 0)
        self.grid.addWidget(self.label2, 0, 1)
        # Add labels for the app text
        note_label1 = QLabel("The words in red have been deleted from the second file")
        note_label2 = QLabel("The words in green have been added to the second file")
        self.grid.addWidget(note_label1, 2, 0)
        self.grid.addWidget(note_label2, 2, 1)
        self.grid.addWidget(self.edit1, 1, 0)
        self.grid.addWidget(self.edit2, 1, 1)
        self.edit1.setReadOnly(True)
        self.edit2.setReadOnly(True)
        palette = QPalette()
        palette.setColor(QPalette.Base, QColor('#f0f0f0'))
        self.edit1.setPalette(palette)
        self.edit2.setPalette(palette)
        self.window.resize(1200, 700)  # set the window size to 1200x700 pixels

    def _populate_edits(self, results):

        for diff in results:
            for word in diff:
                if word.startswith('-'):
                    self.edit1.setTextColor(QColor('red'))
                    self.edit1.insertPlainText(word[2:]+' ')
                elif word.startswith('+'):
                    self.edit2.setTextColor(QColor('green'))
                    self.edit2.insertPlainText(word[2:]+' ')
                elif word.startswith(' '):
                    self.edit1.setTextColor(QColor('black'))
                    self.edit2.setTextColor(QColor('black'))
                    self.edit1.insertPlainText(word[2:]+' ')
                    self.edit2.insertPlainText(word[2:]+' ')
