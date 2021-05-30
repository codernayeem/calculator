from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PyQt5.QtGui import QTextCursor, QFontDatabase
import pyperclip, sys

from main_ui import Ui_MainWindow
from setup import setup
from tools import error, make_power, get_result, is_symbol, MONITOR_SYMBOLS, ERRORS, ADVANCED_KEYS, AFTER_0

app = ApplicationContext()

class History:
    history = []
    cursor = None

    def show(self, do, current_exp):
        # d = 0 : previous_history | d = 1 : next_history
        if self.cursor is None:
            if do == 0:
                self.history.append(current_exp)
                if len(self.history) > 1:
                    self.cursor = len(self.history)-2
                    return self.history[self.cursor]
        elif len(self.history) > self.cursor and ((do == 0 and self.cursor != 0) or (do == 1 and self.cursor+1 != len(self.history))):
            self.cursor += 1 if do == 1 else -1
            return self.history[self.cursor]

    def clear(self):
        self.history, self.cursor = [], None
    
    def out(self):
        if self.cursor is not None:
            self.cursor = None
            if len(self.history):
                self.history.pop()

class Expression():
    def reset(self):
        self.exp, self.pos, self.new_pos = '0', None, None
    
    def set_exp(self, exp, pos=None, change_pos=True):
        self.exp = '0' if not exp else exp
        if change_pos:
            self.new_pos = pos

    def put_data_on_exp(self, data):
        if self.exp == '0' and self.pos == 1:
            res, pos = data, None
        else:
            res, pos = self.exp[:self.start] + str(data) + self.exp[self.end:], self.start+len(data)
        self.set_exp(res, pos)

    def update(self, exp, cursor):
        self.exp = exp
        self.pos = cursor.position()
        self.new_pos = self.pos
        self.start = cursor.selectionStart()
        self.end = cursor.selectionEnd()

    def has_selection(self):
        return False if self.start == self.end else True

    def is_error(self):
        return error(self.exp)

class Calculator(QMainWindow):
    QFontDatabase.addApplicationFont(app.get_resource('font'))
    ui, version, main_ic = Ui_MainWindow(), app.build_settings['version'], app.get_resource('icon.png')
    history = History()
 
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.make_power_enabled = False
        self.ui.setupUi(self)
        setup(self, app.get_resource('backspace.png'))
        self.exp = Expression()
        self.on_ac_click()

    def show_history(self, do):
        self.update_expression()
        if not self.exp.is_error():
            exp = self.history.show(do, self.exp.exp)
            if exp:
                self.exp.set_exp(exp)
                self.update_monitor()
        else:
            self.history.out()

    def copy(self):
        self.update_expression()
        if not self.exp.is_error():
            exp = self.exp.exp[self.exp.start:self.exp.end] if self.exp.has_selection() else self.exp.exp
            for k, v in ADVANCED_KEYS.items():
                if k not in ['^', 'π', '√', '∛', 'Ŷ']:
                    exp = exp.replace(k, v)
            exp = exp.replace('Ŷ', 'rootx(')
            if exp:
                pyperclip.copy(exp)
                return True
        return False

    def cut(self):
        if self.copy():
            self.history.out()
            if self.exp.has_selection():
                self.on_back_click()
            else:
                self.exp.reset()
                self.update_monitor()

    def paste(self):
        paste = pyperclip.paste()
        self.update_expression()
        if paste and not self.exp.is_error():
            self.history.out()
            paste = paste.replace('sin⁻¹', 'asin').replace('cos⁻¹', 'acos').replace('tan⁻¹', 'atan').replace('rootx(', 'Ŷ').replace(' ', '')
            for k, v in ADVANCED_KEYS.items():
                if k not in ['^', 'π', '√', '∛', 'Ŷ']:
                    paste = paste.replace(v, k)
            for i in paste:
                if not is_symbol(i):
                    self.last_invalid_exp = self.exp.exp
                    self.exp.set_exp(ERRORS[5])
                    self.update_monitor()
                    return
            self.exp.put_data_on_exp(paste)
            self.update_monitor()

    def on_power_click(self):
        if self.make_power_enabled:
            self.ui.bt_11.setStyleSheet("QToolButton {background: #80bfff}")
            self.make_power_enabled = False
        else:
            self.ui.bt_11.setStyleSheet("QToolButton {background: orange; border:3px outset red;} QToolButton:pressed {background: orange; border:3px inset red;}")
            self.make_power_enabled = True

    def if_clicked(self, bt, as_power=False):
        self.update_expression()
        if not self.exp.is_error():
            self.history.out()
            if self.make_power_enabled or as_power:
                bt = make_power(bt)
            bt = MONITOR_SYMBOLS.get(bt, bt)
            self.exp.put_data_on_exp('0' + bt if self.exp.exp == '0' and self.exp.pos == 1 and bt in AFTER_0 else bt)
            self.update_monitor()

    def on_plus_minus_click(self):
        self.update_expression()
        if not self.exp.is_error():
            self.history.out()
            if self.exp.exp.startswith('-'):
                self.exp.set_exp(self.exp.exp[1:], self.exp.pos-1)
            elif self.exp.exp.startswith('+'):
                self.exp.set_exp('-' + self.exp.exp[1:], change_pos=False)
            else:
                self.exp.set_exp('-' + self.exp.exp, self.exp.pos+1)
            self.update_monitor()

    def on_back_click(self, delete=False):
        self.update_expression()
        if not self.exp.is_error() and self.exp.exp != '0':
            self.history.out()
            change_pos, pos = True, None
            if self.exp.has_selection():
                res, pos = self.exp.exp[:self.exp.start] + self.exp.exp[self.exp.end:], self.exp.start
            elif delete:
                res, change_pos = self.exp.exp[:self.exp.pos] + self.exp.exp[self.exp.pos+1:], False
            else:
                res, pos = self.exp.exp[:self.exp.pos-1] + self.exp.exp[self.exp.pos:], self.exp.pos-1
            if res:
                self.exp.set_exp(res, pos, change_pos)
            else:
                self.exp.reset()
        self.update_monitor()
    
    def on_ac_click(self):
        self.memory = 0.0
        self.history.clear()
        self.on_c_click()

    def on_c_click(self):
        self.history.out()
        if self.make_power_enabled:
            self.on_power_click()
        self.last_invalid_exp = None
        self.exp.reset()
        self.update_monitor()

    def on_all_m_click(self, do=0):
        # 0 = get current memory or 1 = plus memory or 2 = minus memory or 3 = clear memory
        if do == 3:
            self.memory = 0.0
        elif not self.exp.is_error():
            self.update_expression()
            if do == 0:
                self.history.out()
                r = str(self.memory)
                if r.endswith('.0'):
                    r = r.replace('.0', '')
                self.exp.put_data_on_exp(r)
                self.update_monitor()
            elif do in (1, 2):
                res = get_result(self.exp.exp, self.ui.radio_bt_1.isChecked())
                if error(res):
                    self.history.out()
                    self.last_invalid_exp = self.exp.exp
                    self.exp.set_exp(res)
                    self.update_monitor()
                else:
                    try:
                        exp_float = float(res)
                        self.memory += exp_float if do == 1 else -exp_float
                    except:
                        self.history.out()
                        self.last_invalid_exp = self.exp.exp
                        self.exp.set_exp(ERRORS[2])
                        self.update_monitor()

    def on_ce_click(self):
        self.update_expression()
        if self.exp.is_error():
            self.history.out()
            self.exp.set_exp(self.last_invalid_exp)
            self.update_monitor()

    def on_equal_click(self):
        self.update_expression()
        if not self.exp.is_error():
            self.history.out()
            res = get_result(self.exp.exp, self.ui.radio_bt_1.isChecked())
            if self.make_power_enabled:
                self.on_power_click()
            if error(res):
                self.last_invalid_exp = self.exp.exp
            else:
                self.history.history.append(self.exp.exp)
            self.exp.set_exp(res)
            self.update_monitor()

    def update_expression(self):
        self.exp.update(str(self.ui.main_bar.toPlainText()), self.ui.main_bar.textCursor())
    
    def update_monitor(self):
        self.ui.main_bar.setText(self.exp.exp)
        if self.exp.new_pos is None:
            self.ui.main_bar.moveCursor(QTextCursor.End)
        else:
            self.ui.main_bar.moveCursor(QTextCursor.Start)
            for _ in range(0, self.exp.new_pos):
                self.ui.main_bar.moveCursor(QTextCursor.Right)

if __name__ == '__main__':
    window = Calculator()
    window.show()
    sys.exit(app.app.exec_())
