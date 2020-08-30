from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PyQt5.QtGui import QTextCursor, QFontDatabase
from main_ui import Ui_MainWindow
from setup import setup
from math import pi, e, degrees as deg, radians as rad
import pyperclip, sys, math

app = ApplicationContext()

ERRORS = ('ZeroDivisionError', 'SyntaxError', 'Error', 'MathError', 'NotANumberError', 'PasteError')
ROOTS = ['\u221a', '\u221b']
ADVANCED_KEYS = {'ŭ': 'asin(', 'Ů': 'acos(', 'ů': 'atan(', 'Ű': 'log(','Ū': 'sin(', 'ū': 'cos(', 'Ŭ': 'tan(', 'ű': 'In(', 'Ų': 'logx(', 'ų': 'deg(', 'Ŵ': 'rad(', 'ŵ': 'fact(', 'Ŷ': 'rootx('}
EXTRA_SYMBOLS = {'pi': '\u03c0', 'asin': '\u016d', 'acos': '\u016e', 'atan': '\u016f', 'sin': '\u016a', 'cos': '\u016b', 'tan': '\u016c', 'log': '\u0170', 'ln': '\u0171', 'logx': '\u0172', 'deg': '\u0173','rad': '\u0174', '!': '\u0175', 'rootx': '\u0176'}
POWERS = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '.': '\u02d9', '*': '\u02df', '(': '\u207d', ')': '\u207e', '+': '\u207a', '-': '\u207b', '/': '\ua719'}
POWER_VALUES = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '\u02d9': '.', '\u02df': '*', '\u207d': '(', '\u207e': ')', '\u207a': '+', '\u207b': '-', '\ua719': '/'}
POWER_LIST = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '\u02d9', '\u02df', '\u207d', '\u207e', '\u207a','\u207b', '\ua719']

def fact(n):
    return math.factorial(n)
def log(n):
    return math.log10(n)
def logx(base, n):
    return math.log(n, base)
def ln(n):
    return math.log(n, math.e)
def root(exp, r=2):
    return exp ** (1/r)
def rootx(base, exp):
    return root(exp, base)
def cube_root(exp):
    return root(exp, 3)

class ExpCursor:
    def __init__(self, cursor):
        self.pos = cursor.position()
        self.start = cursor.selectionStart()
        self.end = cursor.selectionEnd()

    def has_selection(self):
        if self.start == self.end:
            return False
        return True

class Calculator(QMainWindow):
    QFontDatabase.addApplicationFont(app.get_resource('font'))
    ui = Ui_MainWindow()
    version, main_ic = app.build_settings['version'], app.get_resource('icon.png')

    history = []
    history_cursor = None
    last_invalid_exp = None
    memory = 0.0
    make_power_enabled = False
 
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")
        setup(self, app.get_resource('backspace.png'))
        self.reset_exp()

    def clear_history(self):
        self.history = []
        self.history_cursor = None

    def off_history(self):
        if self.history_cursor is not None:
            self.history_cursor = None
            try:
                self.history.pop()
            except IndexError:
                pass

    def show_history(self, do):
        if self.history_cursor is None:
            if do == 0:    # previous_history
                self.history_cursor = len(self.history)-1
                self.history.append(self.get_exp())
                try:
                    if self.history_cursor < 0:
                        raise IndexError
                    self.set_exp(self.history[self.history_cursor])
                except IndexError:
                    self.history_cursor = self.history_cursor + 1
        else:
            try:
                if do == 0:    # previous_history
                    self.history_cursor = self.history_cursor - 1
                else:          # next_history
                    self.history_cursor = self.history_cursor + 1
                if self.history_cursor < 0:
                    raise IndexError
                self.set_exp(self.history[self.history_cursor])
            except IndexError:
                if do == 0:    # previous_history
                    self.history_cursor = self.history_cursor + 1
                else:          # next_history
                    self.history_cursor = self.history_cursor - 1

    def copy(self):
        exp = self.get_exp()
        if exp not in ERRORS:
            c = ExpCursor(self.get_cursor())
            if c.has_selection():
                exp = exp[c.start:c.end]
            for k, v in ADVANCED_KEYS.items():
                exp = exp.replace(k, v)
            exp = exp.replace('asin', 'sin⁻¹').replace('acos', 'cos⁻¹').replace('atan', 'tan⁻¹')
            pyperclip.copy(exp)

    def cut(self):
        exp = self.get_exp()
        c = ExpCursor(self.get_cursor())
        if exp not in ERRORS:
            self.copy()
            if c.has_selection():
                self.on_back_click()
            else:
                self.reset_exp()

    def paste(self):
        paste = pyperclip.paste()
        if paste != '':
            exp = self.get_exp()
            got_error = False
            paste = paste.replace('sin⁻¹', 'asin').replace('cos⁻¹', 'acos').replace('tan⁻¹', 'atan')
            for k, v in ADVANCED_KEYS.items():
                paste = paste.replace(v, k)
            self.off_history()
            for a_char in paste:
                if not (a_char in '0123456789.+-*/()^,\u03c0e' or a_char in POWER_LIST or a_char in ROOTS or a_char in EXTRA_SYMBOLS):
                    got_error = True
            if got_error:
                if exp in ERRORS:
                    self.last_invalid_exp = 0.0
                else:
                    self.last_invalid_exp = exp
                self.set_exp(ERRORS[5])
            else:
                c = ExpCursor(self.get_cursor())
                if c.has_selection():
                    if exp not in ERRORS:
                        res = exp[:c.start] + paste + exp[c.end:]
                        self.set_exp(res, c.start+len(paste))
                else:
                    if exp in ERRORS or exp == '0':
                        if c.pos== 0:
                            self.set_exp(exp + paste, len(paste))
                        else:
                            self.set_exp(paste)
                    else:
                        self.set_exp(exp[:c.pos] + paste + exp[c.pos:], c.pos+len(paste))

    def on_power_click(self):
        if self.make_power_enabled:
            self.ui.bt_11.setStyleSheet("QToolButton {background: #80bfff}")
            self.make_power_enabled = False
        else:
            self.ui.bt_11.setStyleSheet("QToolButton {background: orange; border:5px outset red;} QToolButton:pressed {background: orange; border:4px inset red;}")
            self.make_power_enabled = True

    def if_clicked(self, bt, as_power=False):
        exp = self.get_exp()
        c = ExpCursor(self.get_cursor())
        self.off_history()
        if exp not in ERRORS:
            if self.make_power_enabled or as_power:
                bt = self.make_power(bt)
            bt_ = EXTRA_SYMBOLS.get(bt, bt)
            if c.has_selection():
                self.set_exp(exp[:c.start] + str(bt_) + exp[c.end:], c.start+len(bt_))
            else:
                if exp == '0' and c.pos == 1:
                    if not (bt in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', 'pi', '^', 'rootx', '!', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'logx', 'ln', 'deg', 'rad', '(') or bt in ROOTS):
                        bt_ = '0' + bt_
                    self.set_exp(bt_)
                else:
                    self.set_exp(exp[:c.pos] + str(bt_) + exp[c.pos:], c.pos+len(bt_))

    def make_power(self, bt):
        return POWERS.get(bt, bt)

    def on_plus_minus_click(self):
        cursor_pos = ExpCursor(self.get_cursor()).pos
        exp = self.get_exp()
        self.off_history()
        if exp not in ERRORS:
            if exp.startswith('-'):
                self.set_exp(exp[1:], cursor_pos-1)
            if exp.startswith('+'):
                self.set_exp('-' + exp[1:], cursor_pos)
            else:
                self.set_exp('-' + exp, cursor_pos+1)

    def on_root_click(self, n):
        self.if_clicked(ROOTS[n])

    def on_back_click(self, delete=False):
        exp = self.get_exp()
        c = ExpCursor(self.get_cursor())
        self.off_history()

        if exp not in ERRORS and exp != '0':
            if c.has_selection():
                r = exp[:c.start] + exp[c.end:]
                c.pos = c.start
            elif delete:
                r = exp[:c.pos] + exp[c.pos+1:]
            else:
                r = exp[:c.pos-1] + exp[c.pos:]
                c.pos = c.pos-1
            if r != '':
                self.set_exp(r, c.pos)
            else:
                self.reset_exp()
        elif c.has_selection():
            self.set_exp(exp)

    def on_ac_click(self):
        self.off_history()
        if self.make_power_enabled:
            self.on_power_click()
        self.history = []
        self.last_invalid_exp = None
        self.memory = 0.0
        self.reset_exp()

    def on_c_click(self):
        self.off_history()
        if self.make_power_enabled:
            self.on_power_click()
        self.last_invalid_exp = None
        self.reset_exp()

    # 0 = get current memory or 1 = plus memory or 2 = minus memory or 3 = clear memory
    def on_all_m_click(self, do=0):
        exp = self.get_exp()
        if do == 3:
            self.memory = 0.0
        elif exp not in ERRORS:
            if do == 0:
                r = str(self.memory)
                if r.endswith('.0'):
                    r = r.replace('.0', '')
                c = ExpCursor(self.get_cursor())
                if c.has_selection():
                    self.set_exp(exp[:c.start] + r + exp[c.end:], c.pos)
                else:
                    if exp == '0' and c.start == 1:
                        self.set_exp(r, len(r))
                    else:
                        self.set_exp(exp[:c.pos] + r + exp[c.pos:], c.pos+len(r))
            elif do in (1, 2):
                res = self.get_result(exp)
                if res in ERRORS:
                    self.last_invalid_exp = exp
                    self.set_exp(res)
                try:
                    exp_float = float(res)
                    if do == 1:
                        self.memory += exp_float
                    else:
                        self.memory -= exp_float
                except:
                    self.last_invalid_exp = exp
                    self.set_exp(ERRORS[4])

    def on_ce_click(self):
        exp = self.get_exp()
        if exp in ERRORS and self.last_invalid_exp:
            self.set_exp(self.last_invalid_exp)

    def on_equal_click(self):
        self.off_history()
        exp = self.get_exp()
        if exp in ERRORS:
            return
        res = self.get_result(exp)
        if self.make_power_enabled:
            self.on_power_click()
        if res in ERRORS:
            self.last_invalid_exp = exp
        self.set_exp(res)
        self.history.append(exp)

    def check_exp_and_get_standard(self, exp):
        has_power = False
        for a_char in exp:
            if a_char in POWER_LIST:
                has_power = True
                break

        old_char = None
        new_exp = ''
        got_root = False
        for a_char in exp:
            if old_char is not None:
                if got_root:
                    if a_char in '123456789.0\u03c0e' or a_char in POWER_LIST:
                        new_exp += a_char
                    else:
                        new_exp += ')' + a_char
                        got_root = False
                elif old_char in ROOTS and a_char in '123456789.0\u03c0e':
                    got_root = True
                    new_exp += '(' + a_char
                else:
                    new_exp += a_char
                old_char = a_char
            else:
                old_char = a_char
                new_exp += a_char
        if got_root:
            new_exp += ')'
        exp = new_exp

        old_char = None
        new_exp = ''
        got_cap = False
        for a_char in exp:
            if old_char is not None:
                if got_cap:
                    if a_char in '123456789.0\u03c0e' or a_char in POWER_LIST:
                        new_exp += a_char
                    else:
                        new_exp += ')' + a_char
                        got_cap = False
                elif old_char == '^' and a_char in '123456789.0\u03c0e':
                    got_cap = True
                    new_exp += f'({a_char}'
                else:
                    new_exp += a_char
                old_char = a_char
            else:
                old_char = a_char
                new_exp += a_char
        if got_cap:
            new_exp += ')'
        exp = new_exp

        old_char = None
        new_exp = ''
        for a_char in exp:
            if old_char is not None:
                if (a_char in ROOTS and (old_char in '1234567890.)e\u03c0' or old_char in POWER_LIST)) or (a_char == '(' and (old_char in '1234567890.)e\u03c0' or old_char in POWER_LIST)) or (old_char == ')' and (a_char in '1234567890.(e\u03c0' or a_char in EXTRA_SYMBOLS)):
                    new_exp += f'*{a_char}'
                else:
                    new_exp += a_char
                old_char = a_char
            else:
                old_char = a_char
                new_exp += a_char
        exp = new_exp

        old_char = None
        new_exp = ''
        for a_char in exp:
            if old_char is not None:
                if ((a_char in '\u03c0e' or a_char in EXTRA_SYMBOLS) and (old_char in '1234567890.)e\u03c0' or old_char in POWER_LIST)) or (old_char in '\u03c0e' and a_char in '1234567890.\u03c0e'):
                    new_exp += f'*{a_char}'
                else:
                    new_exp += a_char
                old_char = a_char
            else:
                old_char = a_char
                new_exp += a_char
        exp = new_exp

        if has_power:
            last_char = None
            for a_char in exp:
                if last_char is not None:
                    if ((last_char in '+-*/(^' or last_char in ROOTS or last_char in EXTRA_SYMBOLS) and a_char in POWER_LIST) or (last_char in POWER_LIST and a_char in '1234567890.(\u03c0e'):
                        return ERRORS[1]
                last_char = a_char
        res = ''
        if has_power:
            last_was_power = False
            for a_char in exp:
                if last_was_power and a_char not in POWER_LIST:
                    res += ')'
                if a_char in POWER_LIST:
                    if last_was_power:
                        res += POWER_VALUES[a_char]
                    else:
                        res += '**(' + POWER_VALUES[a_char]
                    last_was_power = True
                else:
                    res += a_char
                    last_was_power = False
            if last_was_power:
                res += ')'
            return res
        return exp

    def get_result(self, exp):
        if '()' in exp or '**' in exp:
            return ERRORS[1]
        # fixing exp
        exp = self.check_exp_and_get_standard(exp)
        if exp in ERRORS:
            return exp
        for k, v in ADVANCED_KEYS.items():
            if v in ['log(', 'logx(', 'In(', 'deg(', 'rad(', 'fact(', 'rootx(']:
                exp = exp.replace(k, v)
            else:
                exp = exp.replace(k, f'self.{v}')
        exp = exp.replace(f'{ROOTS[0]}(', 'root(').replace(f'{ROOTS[1]}(', 'cube_root(').replace('\u03c0', 'pi').replace('^', '**')
        
        try:
            ans = str(eval(exp))
            if ans.endswith('.0'):
                ans = ans.replace('.0', '')
            elif ans.endswith('j)'):
                return ERRORS[3]
            if 'e' in ans:
                r = ''
                e_got = False
                for a_char in ans:
                    if e_got:
                        if a_char != '+':
                            r += self.make_power(a_char)
                    elif a_char == 'e':
                        e_got = True
                        r += '\u00d710'
                    else:
                        r += a_char
                ans = r
            return str(ans)
        except ZeroDivisionError:
            return ERRORS[0]
        except SyntaxError:
            return ERRORS[1]
        except Exception as e:
            print(e)
            if str(e) == 'math domain error':
                return ERRORS[3]
            return ERRORS[2]

    def set_exp(self, text, cursor_pos=None):
        self.ui.main_bar.setText(str(text).replace('*', '\u00d7').replace('/', '\u00f7'))
        if cursor_pos is None:
            self.ui.main_bar.moveCursor(QTextCursor.End)
        else:
            self.ui.main_bar.moveCursor(QTextCursor.Start)
            for i in range(0, cursor_pos):
                self.ui.main_bar.moveCursor(QTextCursor.Right)

    def get_exp(self):
        return str(self.ui.main_bar.toPlainText()).replace('\u00d7', '*').replace('\u00f7', '/').replace('\n', '')

    def get_cursor(self):
        return self.ui.main_bar.textCursor()

    def reset_exp(self):
        self.set_exp('0')

    def sin(self, n):
        return math.sin(math.radians(n)) if self.degree_enabled() else math.sin(n)
    def cos(self, n):
        return math.cos(math.radians(n)) if self.degree_enabled() else math.cos(n)
    def tan(self, n):
        return math.tan(math.radians(n)) if self.degree_enabled() else math.tan(n)
    def asin(self, n):
        return math.degrees(math.asin(n)) if self.degree_enabled() else math.asin(n)
    def acos(self, n):
        return math.degrees(math.acos(n)) if self.degree_enabled() else math.acos(n)
    def atan(self, n):
        return math.degrees(math.atan(n)) if self.degree_enabled() else math.atan(n)
    def degree_enabled(self):
        return self.ui.radio_bt_1.isChecked()

if __name__ == '__main__':
    window = Calculator()
    window.show()
    sys.exit(app.app.exec_())
