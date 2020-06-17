from PyQt5.QtWidgets import QShortcut, QAction, QPushButton, QSizePolicy, QWidget, QLayout, QGridLayout, QTextEdit
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QKeySequence, QIcon, QPixmap, QFont, QTextCursor
from author import UiAboutPage
from shortcut_ui import UiShortcutPage

def set_ui(main, backspace_image_link, app_icon):
    set_menu(main, app_icon)
    main.setFixedWidth(321)
    main.setFixedHeight(451)

    main.exp_label = QTextEdit(main)
    main.exp_label.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
    main.exp_label.setGeometry(QRect(0, 20, 321, 81))
    sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.exp_label.sizePolicy().hasHeightForWidth())
    main.exp_label.setSizePolicy(sizePolicy)
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(16)
    main.exp_label.setFont(font)
    main.exp_label.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #9999ff, stop:.5 rgba(102, 204, 255, 255), stop:1 #9999ff); border: 5px ridge #737373; border-bottom: 10px ridge gray; padding: 4px;")
    # main.exp_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
    main.exp_label.setObjectName("exp_label")
    main.num_operator_grid = QWidget(main)
    main.num_operator_grid.setGeometry(QRect(0, 210, 321, 241))
    main.num_operator_grid.setObjectName("num_operator_grid")
    main.gridLayout = QGridLayout(main.num_operator_grid)
    main.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
    main.gridLayout.setContentsMargins(5, 10, 5, 5)
    main.gridLayout.setSpacing(3)
    main.gridLayout.setObjectName("gridLayout")
    main.bt_minus = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_minus.sizePolicy().hasHeightForWidth())
    main.bt_minus.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_minus.setFont(font)
    main.bt_minus.setStyleSheet("QPushButton {background: #ffd11a;} QPushButton:pressed {background: #ffcc00}")
    main.bt_minus.setObjectName("bt_minus")
    main.gridLayout.addWidget(main.bt_minus, 1, 3, 1, 1)
    main.bt_f_bracket = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_f_bracket.sizePolicy().hasHeightForWidth())
    main.bt_f_bracket.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_f_bracket.setFont(font)
    main.bt_f_bracket.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_f_bracket.setObjectName("bt_f_bracket")
    main.gridLayout.addWidget(main.bt_f_bracket, 0, 3, 1, 1)
    main.bt_plus = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_plus.sizePolicy().hasHeightForWidth())
    main.bt_plus.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_plus.setFont(font)
    main.bt_plus.setStyleSheet("QPushButton {background: #ffd11a;} QPushButton:pressed {background: #ffcc00}")
    main.bt_plus.setObjectName("bt_plus")
    main.gridLayout.addWidget(main.bt_plus, 1, 4, 1, 1)
    main.bt_4 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_4.sizePolicy().hasHeightForWidth())
    main.bt_4.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_4.setFont(font)
    main.bt_4.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_4.setObjectName("bt_4")
    main.gridLayout.addWidget(main.bt_4, 1, 0, 1, 1)
    main.bt_6 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_6.sizePolicy().hasHeightForWidth())
    main.bt_6.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_6.setFont(font)
    main.bt_6.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_6.setObjectName("bt_6")
    main.gridLayout.addWidget(main.bt_6, 1, 2, 1, 1)
    main.bt_dot = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_dot.sizePolicy().hasHeightForWidth())
    main.bt_dot.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_dot.setFont(font)
    main.bt_dot.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_dot.setObjectName("bt_dot")
    main.gridLayout.addWidget(main.bt_dot, 3, 2, 1, 1)
    main.bt_7 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_7.sizePolicy().hasHeightForWidth())
    main.bt_7.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_7.setFont(font)
    main.bt_7.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_7.setObjectName("bt_7")
    main.gridLayout.addWidget(main.bt_7, 2, 0, 1, 1)
    main.bt_5 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_5.sizePolicy().hasHeightForWidth())
    main.bt_5.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_5.setFont(font)
    main.bt_5.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_5.setObjectName("bt_5")
    main.gridLayout.addWidget(main.bt_5, 1, 1, 1, 1)
    main.bt_equal = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_equal.sizePolicy().hasHeightForWidth())
    main.bt_equal.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_equal.setFont(font)
    main.bt_equal.setStyleSheet("QPushButton {background: #ffd11a;} QPushButton:pressed {background: #ffcc00}")
    main.bt_equal.setObjectName("bt_equal")
    main.gridLayout.addWidget(main.bt_equal, 2, 4, 2, 1)
    main.bt_l_bracket = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_l_bracket.sizePolicy().hasHeightForWidth())
    main.bt_l_bracket.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_l_bracket.setFont(font)
    main.bt_l_bracket.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_l_bracket.setObjectName("bt_l_bracket")
    main.gridLayout.addWidget(main.bt_l_bracket, 0, 4, 1, 1)
    main.bt_multiply = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_multiply.sizePolicy().hasHeightForWidth())
    main.bt_multiply.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_multiply.setFont(font)
    main.bt_multiply.setStyleSheet("QPushButton {background: #ffd11a;} QPushButton:pressed {background: #ffcc00}")
    main.bt_multiply.setObjectName("bt_multiply")
    main.gridLayout.addWidget(main.bt_multiply, 2, 3, 1, 1)
    main.bt_9 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_9.sizePolicy().hasHeightForWidth())
    main.bt_9.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_9.setFont(font)
    main.bt_9.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_9.setObjectName("bt_9")
    main.gridLayout.addWidget(main.bt_9, 2, 2, 1, 1)
    main.bt_8 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_8.sizePolicy().hasHeightForWidth())
    main.bt_8.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_8.setFont(font)
    main.bt_8.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_8.setObjectName("bt_8")
    main.gridLayout.addWidget(main.bt_8, 2, 1, 1, 1)
    main.bt_divide = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_divide.sizePolicy().hasHeightForWidth())
    main.bt_divide.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_divide.setFont(font)
    main.bt_divide.setStyleSheet("QPushButton {background: #ffd11a;} QPushButton:pressed {background: #ffcc00}")
    main.bt_divide.setObjectName("bt_divide")
    main.gridLayout.addWidget(main.bt_divide, 3, 3, 1, 1)
    main.bt_3 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_3.sizePolicy().hasHeightForWidth())
    main.bt_3.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_3.setFont(font)
    main.bt_3.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_3.setObjectName("bt_3")
    main.gridLayout.addWidget(main.bt_3, 0, 2, 1, 1)
    main.bt_2 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_2.sizePolicy().hasHeightForWidth())
    main.bt_2.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_2.setFont(font)
    main.bt_2.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_2.setObjectName("bt_2")
    main.gridLayout.addWidget(main.bt_2, 0, 1, 1, 1)
    main.bt_1 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_1.sizePolicy().hasHeightForWidth())
    main.bt_1.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_1.setFont(font)
    main.bt_1.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_1.setObjectName("bt_1")
    main.gridLayout.addWidget(main.bt_1, 0, 0, 1, 1)
    main.bt_0 = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_0.sizePolicy().hasHeightForWidth())
    main.bt_0.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_0.setFont(font)
    main.bt_0.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_0.setObjectName("bt_0")
    main.gridLayout.addWidget(main.bt_0, 3, 1, 1, 1)
    main.bt_plus_or_minus = QPushButton(main.num_operator_grid)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_plus_or_minus.sizePolicy().hasHeightForWidth())
    main.bt_plus_or_minus.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_plus_or_minus.setFont(font)
    main.bt_plus_or_minus.setStyleSheet("QPushButton{background: #e6ffff;}")
    main.bt_plus_or_minus.setObjectName("bt_plus_or_minus")
    main.gridLayout.addWidget(main.bt_plus_or_minus, 3, 0, 1, 1)
    main.gridLayoutWidget_2 = QWidget(main)
    main.gridLayoutWidget_2.setGeometry(QRect(0, 100, 321, 111))
    main.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
    main.gridLayout_2 = QGridLayout(main.gridLayoutWidget_2)
    main.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
    main.gridLayout_2.setContentsMargins(5, 5, 5, 0)
    main.gridLayout_2.setHorizontalSpacing(2)
    main.gridLayout_2.setVerticalSpacing(3)
    main.gridLayout_2.setObjectName("gridLayout_2")
    main.bt_ce = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_ce.sizePolicy().hasHeightForWidth())
    main.bt_ce.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_ce.setFont(font)
    main.bt_ce.setStyleSheet("QPushButton {background: red}")
    main.bt_ce.setObjectName("bt_ce")
    main.gridLayout_2.addWidget(main.bt_ce, 0, 1, 1, 1)
    main.bt_mc = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_mc.sizePolicy().hasHeightForWidth())
    main.bt_mc.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_mc.setFont(font)
    main.bt_mc.setStyleSheet("QPushButton {background: red}")
    main.bt_mc.setObjectName("bt_mc")
    main.gridLayout_2.addWidget(main.bt_mc, 0, 2, 1, 1)
    main.bt_ac = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_ac.sizePolicy().hasHeightForWidth())
    main.bt_ac.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_ac.setFont(font)
    main.bt_ac.setStyleSheet("QPushButton {background: red}")
    main.bt_ac.setObjectName("bt_ac")
    main.gridLayout_2.addWidget(main.bt_ac, 0, 0, 1, 1)
    main.bt_mm = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_mm.sizePolicy().hasHeightForWidth())
    main.bt_mm.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_mm.setFont(font)
    main.bt_mm.setStyleSheet("QPushButton {background: red}")
    main.bt_mm.setObjectName("bt_mm")
    main.gridLayout_2.addWidget(main.bt_mm, 0, 4, 1, 1)
    main.bt_mp = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_mp.sizePolicy().hasHeightForWidth())
    main.bt_mp.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_mp.setFont(font)
    main.bt_mp.setStyleSheet("QPushButton {background: red}")
    main.bt_mp.setObjectName("bt_mp")
    main.gridLayout_2.addWidget(main.bt_mp, 0, 3, 1, 1)
    main.bt_m = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_m.sizePolicy().hasHeightForWidth())
    main.bt_m.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_m.setFont(font)
    main.bt_m.setStyleSheet("QPushButton {background: red}")
    main.bt_m.setObjectName("bt_m")
    main.gridLayout_2.addWidget(main.bt_m, 0, 5, 1, 1)
    main.bt_c = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_c.sizePolicy().hasHeightForWidth())
    main.bt_c.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(12)
    main.bt_c.setFont(font)
    main.bt_c.setStyleSheet("QPushButton {background: red}")
    main.bt_c.setObjectName("bt_c")
    main.gridLayout_2.addWidget(main.bt_c, 1, 0, 1, 1)
    main.bt_root_by_2 = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_root_by_2.sizePolicy().hasHeightForWidth())
    main.bt_root_by_2.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_root_by_2.setFont(font)
    main.bt_root_by_2.setStyleSheet("QPushButton {background: blue}")
    main.bt_root_by_2.setObjectName("bt_root_by_2")
    main.gridLayout_2.addWidget(main.bt_root_by_2, 1, 1, 1, 1)
    main.bt_root_by_3 = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_root_by_3.sizePolicy().hasHeightForWidth())
    main.bt_root_by_3.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_root_by_3.setFont(font)
    main.bt_root_by_3.setStyleSheet("QPushButton {background: blue}")
    main.bt_root_by_3.setObjectName("bt_root_by_3")
    main.gridLayout_2.addWidget(main.bt_root_by_3, 1, 2, 1, 1)
    main.bt_square = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_square.sizePolicy().hasHeightForWidth())
    main.bt_square.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_square.setFont(font)
    main.bt_square.setStyleSheet("QPushButton {background: blue}")
    main.bt_square.setObjectName("bt_square")
    main.gridLayout_2.addWidget(main.bt_square, 1, 3, 1, 1)
    main.bt_cube = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_cube.sizePolicy().hasHeightForWidth())
    main.bt_cube.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_cube.setFont(font)
    main.bt_cube.setStyleSheet("QPushButton {background: blue}")
    main.bt_cube.setObjectName("bt_cube")
    main.gridLayout_2.addWidget(main.bt_cube, 1, 4, 1, 1)
    main.bt_back = QPushButton(main.gridLayoutWidget_2)
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main.bt_back.sizePolicy().hasHeightForWidth())
    main.bt_back.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(14)
    main.bt_back.setFont(font)
    main.bt_back.setStyleSheet("QPushButton {background: purple}")
    main.bt_back.setObjectName("bt_back")
    main.gridLayout_2.addWidget(main.bt_back, 1, 5, 1, 1)

    set_text_on_ui(main, backspace_image_link)
    set_on_click_event(main)


def full_screen_toggle(self):
    if self.in_full_screen:
        self.exp_label.setGeometry(QRect(0, 20, 321, 81))
        self.num_operator_grid.setVisible(True)
        self.gridLayoutWidget_2.setVisible(True)
        self.in_full_screen = False
    else:
        self.exp_label.setGeometry(QRect(0, 20, 321, 431))
        self.num_operator_grid.setVisible(False)
        self.gridLayoutWidget_2.setVisible(False)
        self.in_full_screen = True


def set_menu(self, app_icon):
    menu_bar = self.menuBar()
    menu_view = menu_bar.addMenu('Calculator')
    menu_tool = menu_bar.addMenu('Tool')
    menu_about = menu_bar.addMenu('About')
    self.setMenuBar(menu_bar)

    action_full = QAction('FullScreen Toggle', self)
    action_full.setShortcut('Ctrl+F')
    action_full.triggered.connect(lambda: full_screen_toggle(self))

    action_sh = QAction('Shortcuts', self)
    action_sh.setShortcut('Ctrl+S')
    action_sh.triggered.connect(lambda: show_shortcuts(self))

    action_exit = QAction('Exit', self)
    action_exit.setShortcut('Ctrl+Q')
    action_exit.setStatusTip('Exit Calculator')
    action_exit.triggered.connect(lambda: exit(0))

    action_copy = QAction('Copy', self)
    action_copy.setShortcut('Ctrl+C')
    action_copy.triggered.connect(self.copy)

    action_paste = QAction('Paste', self)
    action_paste.setShortcut('Ctrl+V')
    action_paste.triggered.connect(self.paste)

    action_author = QAction('About this app', self)
    action_author.triggered.connect(lambda: see_about(self, app_icon))

    menu_view.addAction(action_full)
    menu_view.addAction(action_sh)
    menu_view.addSeparator()
    menu_view.addAction(action_exit)
    menu_tool.addAction(action_copy)
    menu_tool.addAction(action_paste)
    menu_about.addAction(action_author)

def set_text_on_ui(main, backspace_image_link):
    main.exp_label.setText("0")
    main.exp_label.moveCursor(QTextCursor.End)
    main.bt_ac.setText("AC")
    main.bt_c.setText("C")
    main.bt_ce.setText("CE")
    main.bt_mc.setText("MC")
    main.bt_mp.setText("M+")
    main.bt_mm.setText("M-")
    main.bt_m.setText("M")
    main.bt_root_by_2.setText("\u221A")
    main.bt_root_by_3.setText("\u221B")
    main.bt_square.setText("x\u00B2")
    main.bt_cube.setText("x\u00B3")
    backspace_icon = QIcon()
    backspace_icon.addPixmap(QPixmap(backspace_image_link), QIcon.Normal, QIcon.Off)
    main.bt_back.setIcon(backspace_icon)
    main.bt_back.setIconSize(QSize(45, 45))
    main.bt_1.setText("1")
    main.bt_2.setText("2")
    main.bt_3.setText("3")
    main.bt_4.setText("4")
    main.bt_5.setText("5")
    main.bt_6.setText("6")
    main.bt_7.setText("7")
    main.bt_8.setText("8")
    main.bt_9.setText("9")
    main.bt_0.setText("0")
    main.bt_plus_or_minus.setText("\u00B1")
    main.bt_dot.setText(".")
    main.bt_plus.setText("+")
    main.bt_minus.setText("-")
    main.bt_multiply.setText("\u00d7")
    main.bt_divide.setText("\u00f7")
    main.bt_equal.setText("=")
    main.bt_f_bracket.setText("(")
    main.bt_l_bracket.setText(")")


def set_on_click_event(self):
    self.bt_ac.clicked.connect(lambda: self.on_ac_click())
    self.bt_c.clicked.connect(lambda: self.on_c_click())
    self.bt_ce.clicked.connect(lambda: self.on_ce_click())
    self.bt_mc.clicked.connect(lambda: self.on_all_m_click(3))
    self.bt_mp.clicked.connect(lambda: self.on_all_m_click(1))
    self.bt_mm.clicked.connect(lambda: self.on_all_m_click(2))
    self.bt_m.clicked.connect(lambda: self.on_all_m_click(0))
    self.bt_root_by_2.clicked.connect(lambda: self.on_root_click(2))
    self.bt_root_by_3.clicked.connect(lambda: self.on_root_click(3))
    self.bt_square.clicked.connect(lambda: self.on_square_or_cube(2))
    self.bt_cube.clicked.connect(lambda: self.on_square_or_cube(3))
    self.bt_back.clicked.connect(lambda: self.on_back_click())
    self.bt_1.clicked.connect(lambda: self.if_clicked("1"))
    self.bt_2.clicked.connect(lambda: self.if_clicked("2"))
    self.bt_3.clicked.connect(lambda: self.if_clicked("3"))
    self.bt_4.clicked.connect(lambda: self.if_clicked("4"))
    self.bt_5.clicked.connect(lambda: self.if_clicked("5"))
    self.bt_6.clicked.connect(lambda: self.if_clicked("6"))
    self.bt_7.clicked.connect(lambda: self.if_clicked("7"))
    self.bt_8.clicked.connect(lambda: self.if_clicked("8"))
    self.bt_9.clicked.connect(lambda: self.if_clicked("9"))
    self.bt_0.clicked.connect(lambda: self.if_clicked("0"))
    self.bt_dot.clicked.connect(lambda: self.if_clicked("."))
    self.bt_plus_or_minus.clicked.connect(lambda: self.on_plus_minus_click())
    self.bt_plus.clicked.connect(lambda: self.if_clicked("+"))
    self.bt_minus.clicked.connect(lambda: self.if_clicked("-"))
    self.bt_multiply.clicked.connect(lambda: self.if_clicked("*"))
    self.bt_divide.clicked.connect(lambda: self.if_clicked("/"))
    self.bt_equal.clicked.connect(lambda: self.on_equal_click())
    self.bt_f_bracket.clicked.connect(lambda: self.if_clicked("("))
    self.bt_l_bracket.clicked.connect(lambda: self.if_clicked(")"))


def set_key_sequence(self):
    QShortcut(QKeySequence('up'), self).activated.connect(lambda: self.exp_label.moveCursor(QTextCursor.Up))
    QShortcut(QKeySequence('down'), self).activated.connect(lambda: self.exp_label.moveCursor(QTextCursor.Down))
    QShortcut(QKeySequence('left'), self).activated.connect(lambda: self.exp_label.moveCursor(QTextCursor.Left))
    QShortcut(QKeySequence('right'), self).activated.connect(lambda: self.exp_label.moveCursor(QTextCursor.Right))
    QShortcut(QKeySequence('m'), self).activated.connect(lambda: self.on_all_m_click(0))
    QShortcut(QKeySequence('Shift+m'), self).activated.connect(lambda: self.on_all_m_click(1))
    QShortcut(QKeySequence('Ctrl+m'), self).activated.connect(lambda: self.on_all_m_click(3))
    QShortcut(QKeySequence('Alt+m'), self).activated.connect(lambda: self.on_all_m_click(2))
    QShortcut(QKeySequence('c'), self).activated.connect(lambda: self.on_c_click())
    QShortcut(QKeySequence('Shift+c'), self).activated.connect(lambda: self.on_ac_click())
    QShortcut(QKeySequence('e'), self).activated.connect(lambda: self.on_ce_click())
    QShortcut(QKeySequence('Backspace'), self).activated.connect(lambda: self.on_back_click())
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
    QShortcut(QKeySequence('Return'), self).activated.connect(lambda: self.on_equal_click())
    QShortcut(QKeySequence('Enter'), self).activated.connect(lambda: self.on_equal_click())
    QShortcut(QKeySequence('='), self).activated.connect(lambda: self.if_clicked('='))
    QShortcut(QKeySequence('ctrl+2'), self).activated.connect(lambda: self.on_square_or_cube(2))
    QShortcut(QKeySequence('ctrl+3'), self).activated.connect(lambda: self.on_square_or_cube(3))
    QShortcut(QKeySequence('ctrl+4'), self).activated.connect(lambda: self.on_square_or_cube(4))
    QShortcut(QKeySequence('ctrl+5'), self).activated.connect(lambda: self.on_square_or_cube(5))
    QShortcut(QKeySequence('ctrl+6'), self).activated.connect(lambda: self.on_square_or_cube(6))
    QShortcut(QKeySequence('ctrl+7'), self).activated.connect(lambda: self.on_square_or_cube(7))
    QShortcut(QKeySequence('ctrl+8'), self).activated.connect(lambda: self.on_square_or_cube(8))
    QShortcut(QKeySequence('ctrl+9'), self).activated.connect(lambda: self.on_square_or_cube(9))
    QShortcut(QKeySequence('alt+2'), self).activated.connect(lambda: self.on_root_click(2))
    QShortcut(QKeySequence('alt+3'), self).activated.connect(lambda: self.on_root_click(3))
    QShortcut(QKeySequence('alt+4'), self).activated.connect(lambda: self.on_root_click(4))
    QShortcut(QKeySequence('alt+5'), self).activated.connect(lambda: self.on_root_click(5))
    QShortcut(QKeySequence('alt+6'), self).activated.connect(lambda: self.on_root_click(6))
    QShortcut(QKeySequence('alt+7'), self).activated.connect(lambda: self.on_root_click(7))
    QShortcut(QKeySequence('alt+8'), self).activated.connect(lambda: self.on_root_click(8))
    QShortcut(QKeySequence('alt+9'), self).activated.connect(lambda: self.on_root_click(9))

 

def show_shortcuts(self):
    if self.shortcut_page is None:
        self.shortcut_page = QWidget()
        self.shortcut_page.setWindowTitle('Shortcuts')
        self.shortcut_page.setFixedWidth(340)
        self.shortcut_page.setFixedHeight(444)
        self.shortcut_page.setWindowModality(Qt.ApplicationModal)
        ui = UiShortcutPage()
        ui.setup_ui(self.shortcut_page)
        QShortcut(QKeySequence('Esc'), self.shortcut_page).activated.connect(lambda: self.shortcut_page.close())
    self.shortcut_page.destroy()
    self.shortcut_page.show()


def see_about(self, icon):
    if self.about_page is None:
        self.about_page = QWidget()
        self.about_page.setWindowTitle('About')
        self.about_page.setFixedWidth(350)
        self.about_page.setFixedHeight(221)
        self.about_page.setWindowModality(Qt.ApplicationModal)
        ui = UiAboutPage()
        ui.setup_ui(self.about_page)
        ui.icon.setPixmap(QPixmap(icon))
        QShortcut(QKeySequence('Esc'), self.about_page).activated.connect(lambda: self.about_page.close())
    self.about_page.destroy()
    self.about_page.show()
