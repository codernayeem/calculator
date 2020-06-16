from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QSizePolicy, QStyleFactory,  QWidget, QToolButton, QShortcut)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
import sys

font = None


class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setWindowTitle("Calculator")
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        QApplication.setPalette(QApplication.style().standardPalette())

        global font
        font = self.font()
        font.setPointSize(font.pointSize() + 12)

        self.expression_entry = QLineEdit('')
        self.expression_entry.setFont(font)
        self.expression_entry.setReadOnly(True)
        self.expression_entry.setAlignment(Qt.AlignRight)
        self.expression_entry.setFocus()

        bt_c = self.create_button('C')
        bt_first_b = self.create_button('(')
        bt_last_b = self.create_button(')')
        bt_backspace = self.create_button('Back')
        bt_1 = self.create_button('1')
        bt_2 = self.create_button('2')
        bt_3 = self.create_button('3')
        bt_4 = self.create_button('4')
        bt_5 = self.create_button('5')
        bt_6 = self.create_button('6')
        bt_7 = self.create_button('7')
        bt_8 = self.create_button('8')
        bt_9 = self.create_button('9')
        bt_0 = self.create_button('0')
        bt_plus = self.create_button('+')
        bt_minus = self.create_button('-')
        bt_divide = self.create_button('/')
        bt_multiply = self.create_button('*')
        bt_equal = self.create_button('=')
        bt_dot = self.create_button('.')

        main_layout = QGridLayout()
        main_layout.addWidget(self.expression_entry, 0, 0, 1, 0)
        main_layout.addWidget(bt_c, 1, 0)
        main_layout.addWidget(bt_first_b, 1, 1)
        main_layout.addWidget(bt_last_b, 1, 2)
        main_layout.addWidget(bt_backspace, 1, 3)
        main_layout.addWidget(bt_1, 2, 0)
        main_layout.addWidget(bt_2, 2, 1)
        main_layout.addWidget(bt_3, 2, 2)
        main_layout.addWidget(bt_plus, 2, 3)
        main_layout.addWidget(bt_4, 3, 0)
        main_layout.addWidget(bt_5, 3, 1)
        main_layout.addWidget(bt_6, 3, 2)
        main_layout.addWidget(bt_minus, 3, 3)
        main_layout.addWidget(bt_7, 4, 0)
        main_layout.addWidget(bt_8, 4, 1)
        main_layout.addWidget(bt_9, 4, 2)
        main_layout.addWidget(bt_multiply, 4, 3)
        main_layout.addWidget(bt_dot, 5, 0)
        main_layout.addWidget(bt_0, 5, 1)
        main_layout.addWidget(bt_equal, 5, 2)
        main_layout.addWidget(bt_divide, 5, 3)
        self.setLayout(main_layout)

    def create_button(self, text, command=None, font=None):
        button = Button(text)
        if font is not None:
            button.setFont(font)
        else:
            button.setFont(globals()['font'])
        return button

    def show_result(self, exp):
        pass


if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = Calculator()
    window.resize(350, 350)
    window.show()
    sys.exit(appctxt.app.exec_())
