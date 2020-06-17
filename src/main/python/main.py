from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QLabel, QGridLayout, QLineEdit, QSizePolicy, QStyleFactory,  QWidget, QToolButton, QShortcut, QPushButton)
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QKeySequence, QFont
import sys


class Calculator(QWidget):
    all_key_that_can_entered = '1234567890-+*x/.()'
    errors = ['ZeroDivisionError', 'SyntaxError', 'Error']

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setWindowTitle("Calculator")
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        QApplication.setPalette(QApplication.style().standardPalette())

        font = self.font()
        font.setPointSize(font.pointSize() + 12)

        QShortcut(QKeySequence('Return'), self).activated.connect(lambda: self.if_clicked('='))
        QShortcut(QKeySequence('='), self).activated.connect(lambda: self.if_clicked('='))
        QShortcut(QKeySequence('1'), self).activated.connect(lambda: self.if_clicked('1'))
        QShortcut(QKeySequence('2'), self).activated.connect(lambda: self.if_clicked('2'))
        QShortcut(QKeySequence('3'), self).activated.connect(lambda: self.if_clicked('3'))
        QShortcut(QKeySequence('4'), self).activated.connect(lambda: self.if_clicked('4'))
        QShortcut(QKeySequence('5'), self).activated.connect(lambda: self.if_clicked('5'))
        QShortcut(QKeySequence('6'), self).activated.connect(lambda: self.if_clicked('6'))
        QShortcut(QKeySequence('7'), self).activated.connect(lambda: self.if_clicked('7'))
        QShortcut(QKeySequence('8'), self).activated.connect(lambda: self.if_clicked('8'))
        QShortcut(QKeySequence('9'), self).activated.connect(lambda: self.if_clicked('9'))
        QShortcut(QKeySequence('0'), self).activated.connect(lambda: self.if_clicked('0'))
        QShortcut(QKeySequence('+'), self).activated.connect(lambda: self.if_clicked('+'))
        QShortcut(QKeySequence('-'), self).activated.connect(lambda: self.if_clicked('-'))
        QShortcut(QKeySequence('*'), self).activated.connect(lambda: self.if_clicked('*'))
        QShortcut(QKeySequence('/'), self).activated.connect(lambda: self.if_clicked('/'))
        QShortcut(QKeySequence('('), self).activated.connect(lambda: self.if_clicked('('))
        QShortcut(QKeySequence(')'), self).activated.connect(lambda: self.if_clicked(')'))
        QShortcut(QKeySequence('.'), self).activated.connect(lambda: self.if_clicked('.'))
        QShortcut(QKeySequence('Backspace'), self).activated.connect(lambda: self.if_clicked('Back'))
        QShortcut(QKeySequence('c'), self).activated.connect(lambda: self.if_clicked('C'))

        self.set_ui()

    def set_ui(self):
        self.setStyleSheet('QPushButton {background: #e6ffff} QPushButton:pressed {background: #e6ffe6} QLabel {background: #e6ffff; padding: 5px;}')

        self.expression_entry = QLabel(self)
        self.expression_entry.setGeometry(QRect(0, 0, 241, 61))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.expression_entry.setFont(font)
        self.expression_entry.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(12)

        self.bt_c = QPushButton(self)
        self.bt_c.setGeometry(QRect(0, 60, 61, 61))
        self.bt_c.setFont(font)
        self.bt_c.setStyleSheet('QPushButton {background: red}')

        self.bt_back = QPushButton(self)
        self.bt_back.setGeometry(QRect(60, 60, 121, 61))
        self.bt_back.setFont(font)
        self.bt_back.setStyleSheet('QPushButton {background: #ffffe6} QPushButton:pressed {background: #e6ffe6}')

        self.bt_plus = QPushButton(self)
        self.bt_plus.setGeometry(QRect(180, 60, 61, 61))
        self.bt_plus.setFont(font)
        self.bt_plus.setStyleSheet('QPushButton {background: #ffd11a} QPushButton:pressed {background: #ffcc00}')

        self.bt_3 = QPushButton(self)
        self.bt_3.setGeometry(QRect(120, 119, 61, 61))
        self.bt_3.setFont(font)

        self.bt_1 = QPushButton(self)
        self.bt_1.setGeometry(QRect(0, 119, 61, 61))
        self.bt_1.setFont(font)

        self.bt_2 = QPushButton(self)
        self.bt_2.setGeometry(QRect(60, 119, 61, 61))
        self.bt_2.setFont(font)

        self.bt_minus = QPushButton(self)
        self.bt_minus.setGeometry(QRect(180, 119, 61, 61))
        self.bt_minus.setFont(font)
        self.bt_minus.setStyleSheet('QPushButton {background: #ffd11a} QPushButton:pressed {background: #ffcc00}')

        self.bt_6 = QPushButton(self)
        self.bt_6.setGeometry(QRect(120, 179, 61, 61))
        self.bt_6.setFont(font)

        self.bt_4 = QPushButton(self)
        self.bt_4.setGeometry(QRect(0, 179, 61, 61))
        self.bt_4.setFont(font)

        self.bt_5 = QPushButton(self)
        self.bt_5.setGeometry(QRect(60, 179, 61, 61))
        self.bt_5.setFont(font)

        self.bt_multiply = QPushButton(self)
        self.bt_multiply.setGeometry(QRect(180, 179, 61, 61))
        self.bt_multiply.setFont(font)
        self.bt_multiply.setStyleSheet('QPushButton {background: #ffd11a} QPushButton:pressed {background: #ffcc00}')

        self.bt_9 = QPushButton(self)
        self.bt_9.setGeometry(QRect(120, 239, 61, 61))
        self.bt_9.setFont(font)

        self.bt_7 = QPushButton(self)
        self.bt_7.setGeometry(QRect(0, 239, 61, 61))
        self.bt_7.setFont(font)

        self.bt_8 = QPushButton(self)
        self.bt_8.setGeometry(QRect(60, 239, 61, 61))
        self.bt_8.setFont(font)

        self.bt_divide = QPushButton(self)
        self.bt_divide.setGeometry(QRect(180, 239, 61, 61))
        self.bt_divide.setFont(font)
        self.bt_divide.setStyleSheet('QPushButton {background: #ffd11a} QPushButton:pressed {background: #ffcc00}')

        self.bt_equal = QPushButton(self)
        self.bt_equal.setGeometry(QRect(180, 299, 61, 61))
        self.bt_equal.setFont(font)
        self.bt_equal.setStyleSheet('QPushButton {background: #ffd11a} QPushButton:pressed {background: #ffcc00}')

        self.bt_0 = QPushButton(self)
        self.bt_0.setGeometry(QRect(0, 299, 121, 61))
        self.bt_0.setFont(font)

        self.bt_dot = QPushButton(self)
        self.bt_dot.setGeometry(QRect(120, 299, 61, 61))
        self.bt_dot.setFont(font)
        self.bt_dot.setStyleSheet('QPushButton {background: #ffffe6} QPushButton:pressed {background: #ccffcc}')

        self.expression_entry.setText("0")
        self.bt_c.setText("C")
        self.bt_back.setText("Backspace")
        self.bt_plus.setText("+")
        self.bt_3.setText("3")
        self.bt_1.setText("1")
        self.bt_2.setText("2")
        self.bt_minus.setText("-")
        self.bt_6.setText("6")
        self.bt_4.setText("4")
        self.bt_5.setText("5")
        self.bt_multiply.setText("x")
        self.bt_9.setText("9")
        self.bt_7.setText("7")
        self.bt_8.setText("8")
        self.bt_divide.setText("/")
        self.bt_equal.setText("=")
        self.bt_0.setText("0")
        self.bt_dot.setText(".")

        self.set_onclick_event()

    def set_onclick_event(self):
        self.bt_c.clicked.connect(lambda: self.if_clicked("C"))
        self.bt_back.clicked.connect(lambda: self.if_clicked("Back"))
        self.bt_plus.clicked.connect(lambda: self.if_clicked("+"))
        self.bt_3.clicked.connect(lambda: self.if_clicked("3"))
        self.bt_1.clicked.connect(lambda: self.if_clicked("1"))
        self.bt_2.clicked.connect(lambda: self.if_clicked("2"))
        self.bt_minus.clicked.connect(lambda: self.if_clicked("-"))
        self.bt_6.clicked.connect(lambda: self.if_clicked("6"))
        self.bt_4.clicked.connect(lambda: self.if_clicked("4"))
        self.bt_5.clicked.connect(lambda: self.if_clicked("5"))
        self.bt_multiply.clicked.connect(lambda: self.if_clicked("*"))
        self.bt_9.clicked.connect(lambda: self.if_clicked("9"))
        self.bt_7.clicked.connect(lambda: self.if_clicked("7"))
        self.bt_8.clicked.connect(lambda: self.if_clicked("8"))
        self.bt_divide.clicked.connect(lambda: self.if_clicked("/"))
        self.bt_equal.clicked.connect(lambda: self.if_clicked("="))
        self.bt_0.clicked.connect(lambda: self.if_clicked("0"))
        self.bt_dot.clicked.connect(lambda: self.if_clicked("."))

    def if_clicked(self, bt=None):
        old = str(self.expression_entry.text()).replace('x', '*')
        if bt:
            if bt == "C":
                self.set_text_on_board('0')
            elif bt == "Back":
                if old[:len(old)-1] == '':
                    self.set_text_on_board('0')
                elif old != '0':
                    self.set_text_on_board(old[:len(old)-1])

            if bt == "=":
                if old != '':
                    self.show_result(old)
            else:
                if bt != 'C':
                    for a_char in old:
                        if a_char not in Calculator.all_key_that_can_entered:
                            self.set_text_on_board('0')
                if bt not in ['C', 'Back']:
                    if old == '0' and bt != '.':
                        self.set_text_on_board(str(bt))
                    else:
                        self.set_text_on_board(old + str(bt))

    def set_text_on_board(self, text):
        self.expression_entry.setText(str(text).replace('*', 'x'))

    def show_result(self, exp):
        ex = str(exp)
        if ex == '()':
            ans = Calculator.errors[1]
        elif ex in Calculator.errors:
            ans = '0'
        else:
            try:
                ans = eval(ex)
            except ZeroDivisionError:
                ans = Calculator.errors[0]
            except SyntaxError:
                ans = Calculator.errors[1]
            except:
                ans = Calculator.errors[2]
        self.set_text_on_board(str(ans))


if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = Calculator()
    window.resize(241, 361)
    window.show()
    sys.exit(appctxt.app.exec_())