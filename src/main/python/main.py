from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PyQt5.QtGui import QTextCursor
import sys
from ui_set import set_ui, set_key_sequence


appctxt = ApplicationContext()


class Calculator(QMainWindow):
    errors = ['ZeroDivisionError', 'SyntaxError', 'Error', 'MathError', 'NotANumberError', 'PasteError']
    operators = ['+', '-', '*', '/']
    last_invalid_exp = None
    memory = 0.0
    in_full_screen = False
    about_page = None
    shortcut_page = None

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        set_ui(self, globals()['appctxt'].get_resource('backspace.png'), globals()['appctxt'].get_resource('icon.png'))
        set_key_sequence(self)

    def if_clicked(self, bt):
        if bt in '1234567890.()+-*/':
            exp = self.get_exp()
            if bt in Calculator.operators:
                if exp not in Calculator.errors:
                    self.set_exp(exp + str(bt))
            elif exp not in Calculator.errors:
                if exp == '0' and bt != '.':
                    self.set_exp(str(bt))
                else:
                    self.set_exp(exp + str(bt))
            else:
                if bt == '.':
                    bt = '0.'
                self.set_exp(str(bt))

    def on_plus_minus_click(self):
        exp = self.get_exp()
        if exp not in Calculator.errors:
            if exp.startswith('-'):
                self.set_exp(exp[1:])
            else:
                self.set_exp('-' + exp)

    def on_square_or_cube(self, s):
        if str(s) in '23456789':
            exp = self.get_exp()
            if exp not in Calculator.errors:
                res = self.get_result(f'({exp})**{s}', double_star_allow=True)
                if res:
                    if res in Calculator.errors:
                        self.last_invalid_exp = exp
                    self.set_exp(str(res))

    def on_root_click(self, root):
        if str(root) in '23456789':
            exp = self.get_exp()
            if exp not in Calculator.errors:
                res = self.get_result(exp)
                if res:
                    if res in Calculator.errors:
                        self.last_invalid_exp = exp
                        self.set_exp(res)
                    else:
                        if root in range(0, 10, 2) and res.startswith('-'):
                            self.last_invalid_exp = exp
                            self.set_exp(Calculator.errors[3])
                        else:
                            res = self.get_result(f'{res}**(1/{root})', double_star_allow=True)
                            if res:
                                if res in Calculator.errors:
                                    self.last_invalid_exp = exp
                                    self.set_exp(exp)
                                else:
                                    if str(res).endswith('.0'):
                                        res = str(res).replace('.0', '')
                                    self.set_exp(res)

    def on_back_click(self):
        exp = self.get_exp()
        if exp not in Calculator.errors and exp != '0':
            if exp[:len(exp) - 1] != '':
                self.set_exp(exp[:len(exp) - 1])
            else:
                self.set_exp('0')

    def on_ac_click(self):
        self.last_invalid_exp = None
        self.memory = 0.0
        self.set_exp('0')

    def on_c_click(self):
        self.set_exp('0')

    # 0 = get current memory or 1 = plus memory or 2 = minus memory or 3 = clear memory
    def on_all_m_click(self, do=0):
        exp = self.get_exp()
        if do == 3:
            self.memory = 0.0
        elif exp not in Calculator.errors:
            if do == 0:
                r = str(self.memory)
                if r.endswith('.0'):
                    r = r.replace('.0', '')
                if exp == '0':
                    self.set_exp(r)
                else:
                    self.set_exp(exp + r)
            elif do in (1, 2):
                res = self.get_result(exp)
                if res:
                    if res in Calculator.errors:
                        self.last_invalid_exp = exp
                        self.set_exp(res)
                    try:
                        exp_float = float(res)
                        if do == 1:
                            self.memory += exp_float
                        elif do == 2:
                            self.memory -= exp_float
                    except:
                        self.last_invalid_exp = exp
                        self.set_exp(Calculator.errors[4])

    def on_ce_click(self):
        exp = self.get_exp()
        if exp in Calculator.errors and self.last_invalid_exp:
            self.set_exp(self.last_invalid_exp)

    def on_equal_click(self):
        exp = self.get_exp()
        res = self.get_result(exp)
        if res:
            if res in Calculator.errors:
                self.last_invalid_exp = exp
            self.set_exp(res)

    def get_result(self, exp, double_star_allow=False):
        if exp not in Calculator.errors:
            if exp == '()' or (not double_star_allow and '**' in exp):
                return Calculator.errors[1]
            else:
                try:
                    ans = eval(exp)
                    if str(ans).endswith('.0'):
                        ans = str(ans).replace('.0', '')
                    return str(ans)
                except ZeroDivisionError:
                    return Calculator.errors[0]
                except SyntaxError:
                    return Calculator.errors[1]
                except:
                    return Calculator.errors[2]
        return None

    def set_exp(self, text):
        text = str(text).replace('*', '\u00d7').replace('/', '\u00f7')
        self.exp_label.setPlainText(text)
        self.exp_label.moveCursor(QTextCursor.End)

    def get_exp(self):
        return str(self.exp_label.toPlainText()).replace('\u00d7', '*').replace('\u00f7', '/').replace('\n', '')


if __name__ == '__main__':
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(appctxt.app.exec_())
