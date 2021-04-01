from PyQt5 import QtCore, QtGui, QtWidgets
from dialogs import Ui_AboutPage, Ui_ShortcutPage
import sys

def setup(self, backspace_ic):
    self.setWindowTitle("Calculator")
    self.about_page = None
    self.shortcut_page = None
    self.setFixedHeight(370)
    self.ui.bt_12.setIcon(QtGui.QIcon(backspace_ic))
    update_ui(self)
    set_menu_buttons(self)
    set_on_click_event(self)
    set_key_sequence(self)

def set_menu_buttons(self):
    self.ui.actionAdvance_Screen.toggled.connect(lambda: update_ui(self))
    self.ui.actionFullscreen.toggled.connect(lambda: update_ui(self))
    self.ui.actionShortcuts.triggered.connect(lambda: show_dialog(self, n=2))
    self.ui.actionExit.triggered.connect(sys.exit)
    self.ui.actionCopy.triggered.connect(self.copy)
    self.ui.actionCut.triggered.connect(self.cut)
    self.ui.actionPaste.triggered.connect(self.paste)
    self.ui.actionPrevious_History.triggered.connect(lambda: self.show_history(0))
    self.ui.actionNext_History.triggered.connect(lambda: self.show_history(1))
    self.ui.actionClear_History.triggered.connect(self.history.clear)
    self.ui.actionAbout_the_Author.triggered.connect(lambda: show_dialog(self, n=1))

def set_on_click_event(self):
    self.ui.bt_1.clicked.connect(lambda: self.on_ac_click())
    self.ui.bt_2.clicked.connect(lambda: self.on_ce_click())
    self.ui.bt_3.clicked.connect(lambda: self.on_all_m_click(3))
    self.ui.bt_4.clicked.connect(lambda: self.on_all_m_click(1))
    self.ui.bt_5.clicked.connect(lambda: self.on_all_m_click(2))
    self.ui.bt_6.clicked.connect(lambda: self.on_all_m_click(0))
    self.ui.bt_7.clicked.connect(lambda: self.on_c_click())

    self.ui.bt_8.clicked.connect(lambda: self.if_clicked('root2'))
    self.ui.bt_9.clicked.connect(lambda: self.if_clicked('root3'))
    self.ui.bt_10.clicked.connect(lambda: self.if_clicked("2", as_power=True))
    self.ui.bt_11.clicked.connect(lambda: self.on_power_click())
    self.ui.bt_12.clicked.connect(lambda: self.on_back_click())
    self.ui.bt_13.clicked.connect(lambda: self.if_clicked("1"))
    self.ui.bt_14.clicked.connect(lambda: self.if_clicked("2"))
    self.ui.bt_15.clicked.connect(lambda: self.if_clicked("3"))
    self.ui.bt_16.clicked.connect(lambda: self.if_clicked("("))
    self.ui.bt_17.clicked.connect(lambda: self.if_clicked(")"))
    self.ui.bt_18.clicked.connect(lambda: self.if_clicked("4"))
    self.ui.bt_19.clicked.connect(lambda: self.if_clicked("5"))
    self.ui.bt_20.clicked.connect(lambda: self.if_clicked("6"))
    self.ui.bt_21.clicked.connect(lambda: self.if_clicked("-"))
    self.ui.bt_22.clicked.connect(lambda: self.if_clicked("+"))
    self.ui.bt_23.clicked.connect(lambda: self.if_clicked("7"))
    self.ui.bt_24.clicked.connect(lambda: self.if_clicked("8"))
    self.ui.bt_25.clicked.connect(lambda: self.if_clicked("9"))
    self.ui.bt_26.clicked.connect(lambda: self.if_clicked("*"))
    self.ui.bt_27.clicked.connect(lambda: self.on_equal_click())
    self.ui.bt_28.clicked.connect(lambda: self.on_plus_minus_click())
    self.ui.bt_29.clicked.connect(lambda: self.if_clicked("0"))
    self.ui.bt_30.clicked.connect(lambda: self.if_clicked("."))
    self.ui.bt_31.clicked.connect(lambda: self.if_clicked("/"))
    self.ui.bt_32.clicked.connect(lambda: self.if_clicked("pi"))
    self.ui.bt_33.clicked.connect(lambda: self.if_clicked("e"))
    self.ui.bt_34.clicked.connect(lambda: self.if_clicked("^"))
    self.ui.bt_35.clicked.connect(lambda: self.if_clicked("!"))
    self.ui.bt_36.clicked.connect(lambda: self.if_clicked(","))
    self.ui.bt_37.clicked.connect(lambda: self.if_clicked("rootx"))
    self.ui.bt_38.clicked.connect(lambda: self.if_clicked("sin"))
    self.ui.bt_39.clicked.connect(lambda: self.if_clicked("cos"))
    self.ui.bt_40.clicked.connect(lambda: self.if_clicked("tan"))
    self.ui.bt_41.clicked.connect(lambda: self.if_clicked("asin"))
    self.ui.bt_42.clicked.connect(lambda: self.if_clicked("acos"))
    self.ui.bt_43.clicked.connect(lambda: self.if_clicked("atan"))
    self.ui.bt_44.clicked.connect(lambda: self.if_clicked("log"))
    self.ui.bt_45.clicked.connect(lambda: self.if_clicked("logx"))
    self.ui.bt_46.clicked.connect(lambda: self.if_clicked("ln"))
    self.ui.bt_47.clicked.connect(lambda: self.if_clicked("deg"))
    self.ui.bt_48.clicked.connect(lambda: self.if_clicked("rad"))
    self.ui.bt_49.clicked.connect(lambda: self.if_clicked("*10"))

def set_key_sequence(self):
    QtWidgets.QShortcut(QtGui.QKeySequence('up'), self).activated.connect(lambda: self.ui.main_bar.moveCursor(QtGui.QTextCursor.Up))
    QtWidgets.QShortcut(QtGui.QKeySequence('down'), self).activated.connect(lambda: self.ui.main_bar.moveCursor(QtGui.QTextCursor.Down))
    QtWidgets.QShortcut(QtGui.QKeySequence('left'), self).activated.connect(lambda: self.ui.main_bar.moveCursor(QtGui.QTextCursor.Left))
    QtWidgets.QShortcut(QtGui.QKeySequence('right'), self).activated.connect(lambda: self.ui.main_bar.moveCursor(QtGui.QTextCursor.Right))
    QtWidgets.QShortcut(QtGui.QKeySequence('m'), self).activated.connect(lambda: self.on_all_m_click(0))
    QtWidgets.QShortcut(QtGui.QKeySequence('Shift+m'), self).activated.connect(lambda: self.on_all_m_click(1))
    QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+m'), self).activated.connect(lambda: self.on_all_m_click(3))
    QtWidgets.QShortcut(QtGui.QKeySequence('Alt+m'), self).activated.connect(lambda: self.on_all_m_click(2))
    QtWidgets.QShortcut(QtGui.QKeySequence('c'), self).activated.connect(lambda: self.on_c_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('alt+c'), self).activated.connect(lambda: self.on_ac_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+e'), self).activated.connect(lambda: self.on_ce_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('Backspace'), self).activated.connect(lambda: self.on_back_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('Delete'), self).activated.connect(lambda: self.on_back_click(delete=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self).activated.connect(lambda: self.on_equal_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('Return'), self).activated.connect(lambda: self.on_equal_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('='), self).activated.connect(lambda: self.on_equal_click())
    QtWidgets.QShortcut(QtGui.QKeySequence('1'), self).activated.connect(lambda: self.if_clicked('1'))
    QtWidgets.QShortcut(QtGui.QKeySequence('2'), self).activated.connect(lambda: self.if_clicked('2'))
    QtWidgets.QShortcut(QtGui.QKeySequence('3'), self).activated.connect(lambda: self.if_clicked('3'))
    QtWidgets.QShortcut(QtGui.QKeySequence('4'), self).activated.connect(lambda: self.if_clicked('4'))
    QtWidgets.QShortcut(QtGui.QKeySequence('5'), self).activated.connect(lambda: self.if_clicked('5'))
    QtWidgets.QShortcut(QtGui.QKeySequence('6'), self).activated.connect(lambda: self.if_clicked('6'))
    QtWidgets.QShortcut(QtGui.QKeySequence('7'), self).activated.connect(lambda: self.if_clicked('7'))
    QtWidgets.QShortcut(QtGui.QKeySequence('8'), self).activated.connect(lambda: self.if_clicked('8'))
    QtWidgets.QShortcut(QtGui.QKeySequence('9'), self).activated.connect(lambda: self.if_clicked('9'))
    QtWidgets.QShortcut(QtGui.QKeySequence('0'), self).activated.connect(lambda: self.if_clicked('0'))
    QtWidgets.QShortcut(QtGui.QKeySequence('+'), self).activated.connect(lambda: self.if_clicked('+'))
    QtWidgets.QShortcut(QtGui.QKeySequence('-'), self).activated.connect(lambda: self.if_clicked('-'))
    QtWidgets.QShortcut(QtGui.QKeySequence('*'), self).activated.connect(lambda: self.if_clicked('*'))
    QtWidgets.QShortcut(QtGui.QKeySequence('/'), self).activated.connect(lambda: self.if_clicked('/'))
    QtWidgets.QShortcut(QtGui.QKeySequence('('), self).activated.connect(lambda: self.if_clicked('('))
    QtWidgets.QShortcut(QtGui.QKeySequence(')'), self).activated.connect(lambda: self.if_clicked(')'))
    QtWidgets.QShortcut(QtGui.QKeySequence('.'), self).activated.connect(lambda: self.if_clicked('.'))
    QtWidgets.QShortcut(QtGui.QKeySequence(','), self).activated.connect(lambda: self.if_clicked(','))
    QtWidgets.QShortcut(QtGui.QKeySequence('!'), self).activated.connect(lambda: self.if_clicked('!'))
    QtWidgets.QShortcut(QtGui.QKeySequence('e'), self).activated.connect(lambda: self.if_clicked('e'))
    QtWidgets.QShortcut(QtGui.QKeySequence('^'), self).activated.connect(lambda: self.if_clicked('^'))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+0'), self).activated.connect(lambda: self.if_clicked('0', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+1'), self).activated.connect(lambda: self.if_clicked('1', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+2'), self).activated.connect(lambda: self.if_clicked('2', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+3'), self).activated.connect(lambda: self.if_clicked('3', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+4'), self).activated.connect(lambda: self.if_clicked('4', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+5'), self).activated.connect(lambda: self.if_clicked('5', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+6'), self).activated.connect(lambda: self.if_clicked('6', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+7'), self).activated.connect(lambda: self.if_clicked('7', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+8'), self).activated.connect(lambda: self.if_clicked('8', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+9'), self).activated.connect(lambda: self.if_clicked('9', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+.'), self).activated.connect(lambda: self.if_clicked('.', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl++'), self).activated.connect(lambda: self.if_clicked('+', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+-'), self).activated.connect(lambda: self.if_clicked('-', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+*'), self).activated.connect(lambda: self.if_clicked('*', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+/'), self).activated.connect(lambda: self.if_clicked('/', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+alt+9'), self).activated.connect(lambda: self.if_clicked('(', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('ctrl+alt+0'), self).activated.connect(lambda: self.if_clicked(')', as_power=True))
    QtWidgets.QShortcut(QtGui.QKeySequence('alt+2'), self).activated.connect(lambda: self.if_clicked('root2'))
    QtWidgets.QShortcut(QtGui.QKeySequence('alt+3'), self).activated.connect(lambda: self.if_clicked('root3'))

def update_ui(self):
    i1, i2 = self.ui.actionAdvance_Screen.isChecked(), self.ui.actionFullscreen.isChecked()
    width, part_1, part_2, strech = 470, True, False, (2, 2, 4)

    if i1 and i2:
        part_1 = False
        strech = (0, 0, 0)
    elif i1:
        part_2 = True
    elif i2:
        part_1 = False
        width = 250
        strech = (0, 0, 0)
    else:
        width = 250
    
    self.setFixedWidth(width)
    self.ui.widget_box_1.setVisible(part_1)
    self.ui.widget_box_2.setVisible(part_1)
    self.ui.widget_box_3.setVisible(part_2)
    self.ui.widget_box_4.setVisible(part_2)
    for i in range(0, 3):
        self.ui.gridLayout.setRowStretch(i, strech[i])

def show_dialog(self, n):
    if n == 1:
        if self.about_page is None:
            self.about_page = QtWidgets.QWidget()
            ui = Ui_AboutPage()
            ui.setupUi(self.about_page)
            self.about_page.setFixedWidth(350)
            self.about_page.setFixedHeight(215)
            ui.icon.setPixmap(QtGui.QPixmap(self.main_ic))
            ui.name.setText('Calculator')
            ui.version.setText('v' + self.version)
            QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self.about_page).activated.connect(self.about_page.close)
        self.about_page.destroy()
        self.about_page.show()
    else:
        if self.shortcut_page is None:
            self.shortcut_page = QtWidgets.QWidget()
            ui = Ui_ShortcutPage()
            ui.setupUi(self.shortcut_page)
            self.shortcut_page.setFixedWidth(370)
            self.shortcut_page.setFixedHeight(360)
            self.shortcut_page.setWindowTitle('Shortcuts')
            ui.app_name.setText('Calculator')
            ui.version.setText(f'v{self.version}')
            QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self.shortcut_page).activated.connect(lambda: self.shortcut_page.close())
        self.shortcut_page.destroy()
        self.shortcut_page.show()
