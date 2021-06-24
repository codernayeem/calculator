import math
from math import pi, e, degrees as deg, radians as rad

ERRORS = ['Error', 'SyntaxError', 'MathError', 'ZeroDivisionError', 'NotANumberError', 'PasteError']

POWERS = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '.': '\u02d9', '*': '\u02df', '(': '\u207d', ')': '\u207e', '+': '\u207a', '-': '\u207b', '/': '\ua719'}
POWER_VALUES = {v: k for k, v in POWERS.items()}
POWER_LIST = [v for k, v in POWERS.items()]

# Used: Button >> if_clicked >> Monitor
MONITOR_SYMBOLS = {'*': '×', '/': '÷', 'pi': 'π', 'asin': 'ŭ', 'acos': 'Ů', 'atan': 'ů', 'sin': 'Ū', 'cos': 'ū', 'tan': 'Ŭ', 'log': 'Ű', 'ln': 'ű', 'logx': 'Ų', 'deg': 'ų', 'rad': 'Ŵ', '!': 'ŵ', 'rootx': 'Ŷ', 'root2': '√', 'root3': '∛'}

# Used: Monitor >> get_result >> get_standard
ADVANCED_KEYS = {'^': '**', '×': '*', '÷': '/', 'π': 'pi', '√': 'root(2,', '∛': 'root(3,', 'ŭ': 'asin(', 'Ů': 'acos(', 'ů': 'atan(', 'Ű': 'log(', 'Ū': 'sin(', 'ū': 'cos(', 'Ŭ': 'tan(', 'ű': 'ln(', 'Ų': 'logx(', 'ų': 'deg(', 'Ŵ': 'rad(', 'ŵ': 'fact(', 'Ŷ': 'root('}

ADVANCED_SYMBOLS = ['ŭ', 'Ů', 'ů', 'Ū', 'ū', 'Ŭ', 'Ű', 'ű', 'Ų', 'ų', 'Ŵ', 'ŵ', 'Ŷ', '√', '∛']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0', 'π', 'e']

# Can be used after 0 (Monitor Symbols)
AFTER_0 = ['^', ')', '*10', ',', '+', '-', '×', '÷', '.'] + POWER_LIST

def is_symbol(s):
    return True if s in NUMBERS + ADVANCED_SYMBOLS + ['+', '-', '×', '÷', '(', ')', '^', ','] + POWER_LIST else False

def error(exp):
    return True if exp in ERRORS else False

def make_power(bt):
    return POWERS.get(bt, bt)

def fix_bracket(exp, symbols, include_in_bracket, put_baracket_at_first=False):
    old_char, new_exp, got_symbol = None, '', False
    for a_char in exp:
        if old_char is not None:
            if got_symbol:
                if a_char in include_in_bracket:
                    new_exp += a_char
                else:
                    new_exp += ')' + a_char
                    got_symbol = False
            elif old_char in symbols:
                got_symbol = True
                if put_baracket_at_first:
                    new_exp += '('
                new_exp += a_char
            else:
                new_exp += a_char
            old_char = a_char
        else:
            old_char = a_char
            new_exp += a_char
    if got_symbol:
        new_exp += ')'
    return new_exp

def fix_multiplication(exp, before, after):
    old_char = None
    new_exp = ''
    for a_char in exp:
        if old_char is not None:
            if old_char in before and a_char in after:
                new_exp += '*' + a_char
            else:
                new_exp += a_char
            old_char = a_char
        else:
            old_char = a_char
            new_exp += a_char
    return new_exp

def check_exp_and_get_standard(exp):
    exp = fix_bracket(exp, ['\u221a', '\u221b'], NUMBERS + POWER_LIST) # fixes bracket after roots
    exp = fix_bracket(exp, '^', NUMBERS + POWER_LIST, True) # fixes bracket after cap
    exp = fix_multiplication(exp, NUMBERS + POWER_LIST +  [')'], ['(', 'e', 'π'] + ADVANCED_SYMBOLS) # fixes multiply after/before some symbols

    # convert powers to plain equation with brackets
    res = ''
    last_was_power = False
    for a_char in exp:
        if last_was_power and a_char not in POWER_LIST:
            res += ')'
        if a_char in POWER_LIST:
            res += POWER_VALUES[a_char] if last_was_power else '**(' + POWER_VALUES[a_char]
            last_was_power = True
        else:
            res += a_char
            last_was_power = False
    if last_was_power:
        res += ')'
    return res

def correct_ans(ans):
    ans = str(round(ans, 11)) # round ans to 11 decimal points to avoid large decimal
    if ans.endswith('.0'):
        ans = ans[:-2]
    if 'e' in ans:
        r = ''
        e_got = False
        for a_char in ans:
            if e_got:
                if a_char != '+':
                    r += make_power(a_char)
            elif a_char == 'e':
                e_got = True
                r += '\u00d710'
            else:
                r += a_char
        ans = r
    return ans

def get_result(exp, degree_enabled):
    if '()' in exp or '**' in exp:
        return ERRORS[1]

    exp = check_exp_and_get_standard(exp)
    if error(exp):
        return exp
    
    degree_enabled = 'True' if degree_enabled else 'False'
    for k, v in ADVANCED_KEYS.items():
        exp = exp.replace(k, f'{v}{degree_enabled},') if v in ['asin(', 'acos(', 'atan(', 'sin(', 'cos(', 'tan('] else exp.replace(k, v)
    
    try:
        ans = eval(exp)
        if str(ans).endswith('j)'):
            return ERRORS[3]
        return ', '.join([correct_ans(i) for i in ans]) if isinstance(ans, tuple) else correct_ans(ans)
    except ZeroDivisionError:
        return ERRORS[3]
    except SyntaxError:
        return ERRORS[1]
    except Exception as e:
        # print(e)
        return ERRORS[2] if str(e) == 'math domain error' else ERRORS[0]

# Maths
def fact(n):
    return math.factorial(n)
def logx(base, n):
    return math.log(n, base)
def log(n):
    return math.log10(n)
def ln(n):
    return logx(math.e, n)
def root(power, base):
    return base ** (1/power)

def check_radian(degree_enabled, n):
    return rad(n) if degree_enabled else n
def check_degree(degree_enabled, n):
    return deg(n) if degree_enabled else n

def sin(degree_enabled, n):
    return math.sin(check_radian(degree_enabled, n))
def cos(degree_enabled, n):
    return math.cos(check_radian(degree_enabled, n))
def tan(degree_enabled, n):
    return math.tan(check_radian(degree_enabled, n))
def asin(degree_enabled, n):
    return check_degree(degree_enabled, math.asin(n))
def acos(degree_enabled, n):
    return check_degree(degree_enabled, math.acos(n))
def atan(degree_enabled, n):
    return check_degree(degree_enabled, math.atan(n))
