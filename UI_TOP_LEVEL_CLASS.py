# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0JVlhGh.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SeaServiceMaster(object):
    def setupUi(self, SeaServiceMaster):
        if not SeaServiceMaster.objectName():
            SeaServiceMaster.setObjectName(u"SeaServiceMaster")
        SeaServiceMaster.setEnabled(True)
        SeaServiceMaster.resize(889, 683)
        self.centralwidget = QWidget(SeaServiceMaster)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setEnabled(True)
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 421, 71))
        self.AutoDataGenerate = QGridLayout(self.gridLayoutWidget_2)
        self.AutoDataGenerate.setObjectName(u"AutoDataGenerate")
        self.AutoDataGenerate.setContentsMargins(0, 0, 0, 0)
        self.lcd_leave = QLCDNumber(self.gridLayoutWidget_2)
        self.lcd_leave.setObjectName(u"lcd_leave")
        self.lcd_leave.setEnabled(True)
        self.lcd_leave.setFocusPolicy(Qt.WheelFocus)
        self.lcd_leave.setLineWidth(2)
        self.lcd_leave.setMidLineWidth(1)
        self.lcd_leave.setDigitCount(3)

        self.AutoDataGenerate.addWidget(self.lcd_leave, 2, 4, 1, 1)

        self.lcd_inport = QLCDNumber(self.gridLayoutWidget_2)
        self.lcd_inport.setObjectName(u"lcd_inport")
        self.lcd_inport.setEnabled(True)
        self.lcd_inport.setLineWidth(2)
        self.lcd_inport.setDigitCount(3)

        self.AutoDataGenerate.addWidget(self.lcd_inport, 2, 3, 1, 1)

        self.lcd_training = QLCDNumber(self.gridLayoutWidget_2)
        self.lcd_training.setObjectName(u"lcd_training")
        self.lcd_training.setEnabled(True)
        self.lcd_training.setLineWidth(2)
        self.lcd_training.setDigitCount(3)

        self.AutoDataGenerate.addWidget(self.lcd_training, 2, 1, 1, 1)

        self.lcd_leave_label = QLabel(self.gridLayoutWidget_2)
        self.lcd_leave_label.setObjectName(u"lcd_leave_label")
        self.lcd_leave_label.setEnabled(True)

        self.AutoDataGenerate.addWidget(self.lcd_leave_label, 0, 4, 1, 1)

        self.lcd_seadays = QLCDNumber(self.gridLayoutWidget_2)
        self.lcd_seadays.setObjectName(u"lcd_seadays")
        self.lcd_seadays.setEnabled(True)
        self.lcd_seadays.setFrameShape(QFrame.Box)
        self.lcd_seadays.setLineWidth(2)
        self.lcd_seadays.setDigitCount(3)

        self.AutoDataGenerate.addWidget(self.lcd_seadays, 2, 2, 1, 1)

        self.lcd_absent = QLCDNumber(self.gridLayoutWidget_2)
        self.lcd_absent.setObjectName(u"lcd_absent")
        self.lcd_absent.setEnabled(True)
        self.lcd_absent.setAutoFillBackground(True)
        self.lcd_absent.setLineWidth(2)
        self.lcd_absent.setSmallDecimalPoint(True)
        self.lcd_absent.setDigitCount(3)
        self.lcd_absent.setMode(QLCDNumber.Dec)
        self.lcd_absent.setProperty("value", 0.000000000000000)
        self.lcd_absent.setProperty("intValue", 0)

        self.AutoDataGenerate.addWidget(self.lcd_absent, 2, 0, 1, 1)

        self.training_labellcd = QLabel(self.gridLayoutWidget_2)
        self.training_labellcd.setObjectName(u"training_labellcd")
        self.training_labellcd.setEnabled(True)

        self.AutoDataGenerate.addWidget(self.training_labellcd, 0, 1, 1, 1)

        self.Seadays_lcd_label = QLabel(self.gridLayoutWidget_2)
        self.Seadays_lcd_label.setObjectName(u"Seadays_lcd_label")
        self.Seadays_lcd_label.setEnabled(True)

        self.AutoDataGenerate.addWidget(self.Seadays_lcd_label, 0, 2, 1, 1)

        self.inport_lcdlable = QLabel(self.gridLayoutWidget_2)
        self.inport_lcdlable.setObjectName(u"inport_lcdlable")
        self.inport_lcdlable.setEnabled(True)

        self.AutoDataGenerate.addWidget(self.inport_lcdlable, 0, 3, 1, 1)

        self.absent_labellcd = QLabel(self.gridLayoutWidget_2)
        self.absent_labellcd.setObjectName(u"absent_labellcd")
        self.absent_labellcd.setEnabled(True)

        self.AutoDataGenerate.addWidget(self.absent_labellcd, 0, 0, 1, 1)

        self.userinstruction_lobel = QLabel(self.centralwidget)
        self.userinstruction_lobel.setObjectName(u"userinstruction_lobel")
        self.userinstruction_lobel.setEnabled(True)
        self.userinstruction_lobel.setGeometry(QRect(420, 0, 421, 71))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.userinstruction_lobel.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.userinstruction_lobel.setFont(font)
        self.userinstruction_lobel.setLayoutDirection(Qt.LeftToRight)
        self.userinstruction_lobel.setAutoFillBackground(True)
        self.userinstruction_lobel.setFrameShadow(QFrame.Raised)
        self.userinstruction_lobel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.userinstruction_lobel.setWordWrap(True)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setGeometry(QRect(10, 380, 471, 231))
        #Letter table
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(10, 80, 851, 241))
        
        self.INFOBOX = QLabel(self.centralwidget)
        self.INFOBOX.setObjectName(u"INFOBOX")
        self.INFOBOX.setEnabled(True)
        self.INFOBOX.setGeometry(QRect(430, 40, 281, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setKerning(True)
        self.INFOBOX.setFont(font1)
        self.INFOBOX.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(510, 330, 371, 331))
        self.tabWidget.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.GeneratePDF = QWidget()
        self.GeneratePDF.setObjectName(u"GeneratePDF")
        self.GeneratePDF.setToolTipDuration(-9)
        self.frame = QFrame(self.GeneratePDF)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(10, 30, 351, 271))
        self.frame.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.frame.setToolTipDuration(-2)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setEnabled(True)
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 331, 262))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ref_num = QLabel(self.gridLayoutWidget)
        self.ref_num.setObjectName(u"ref_num")
        self.ref_num.setEnabled(True)

        self.gridLayout.addWidget(self.ref_num, 6, 0, 1, 1)

        self.create_letter = QPushButton(self.gridLayoutWidget)
        self.create_letter.setObjectName(u"create_letter")
        self.create_letter.setEnabled(False)

        self.gridLayout.addWidget(self.create_letter, 2, 1, 1, 1)

        self.load_file = QPushButton(self.gridLayoutWidget)
        self.load_file.setObjectName(u"load_file")
        self.load_file.setEnabled(False)

        self.gridLayout.addWidget(self.load_file, 2, 0, 1, 1)

        self.pos_title = QLineEdit(self.gridLayoutWidget)
        self.pos_title.setObjectName(u"pos_title")
        self.pos_title.setEnabled(True)

        self.gridLayout.addWidget(self.pos_title, 8, 1, 1, 1)

        self.co_name = QLabel(self.gridLayoutWidget)
        self.co_name.setObjectName(u"co_name")
        self.co_name.setEnabled(True)

        self.gridLayout.addWidget(self.co_name, 4, 0, 1, 1)

        self.refnum = QLineEdit(self.gridLayoutWidget)
        self.refnum.setObjectName(u"refnum")
        self.refnum.setEnabled(True)

        self.gridLayout.addWidget(self.refnum, 6, 1, 1, 1)

        self.co_namerank = QLineEdit(self.gridLayoutWidget)
        self.co_namerank.setObjectName(u"co_namerank")
        self.co_namerank.setEnabled(True)

        self.gridLayout.addWidget(self.co_namerank, 4, 1, 1, 1)

        self.fullname = QLineEdit(self.gridLayoutWidget)
        self.fullname.setObjectName(u"fullname")
        self.fullname.setEnabled(True)

        self.gridLayout.addWidget(self.fullname, 7, 1, 1, 1)

        self.title_position = QLabel(self.gridLayoutWidget)
        self.title_position.setObjectName(u"title_position")
        self.title_position.setEnabled(True)

        self.gridLayout.addWidget(self.title_position, 8, 0, 1, 1)

        self.full_name = QLabel(self.gridLayoutWidget)
        self.full_name.setObjectName(u"full_name")
        self.full_name.setEnabled(True)

        self.gridLayout.addWidget(self.full_name, 7, 0, 1, 1)

        self.Lastname = QLineEdit(self.gridLayoutWidget)
        self.Lastname.setObjectName(u"Lastname")
        self.Lastname.setEnabled(True)

        self.gridLayout.addWidget(self.Lastname, 3, 1, 1, 1)

        self.last_name = QLabel(self.gridLayoutWidget)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setEnabled(True)

        self.gridLayout.addWidget(self.last_name, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.office_type = QComboBox(self.gridLayoutWidget)
        self.office_type.addItem("")
        self.office_type.addItem("")
        self.office_type.addItem("")
        self.office_type.addItem("")
        self.office_type.addItem("")
        self.office_type.setObjectName(u"office_type")
        self.office_type.setEnabled(True)

        self.verticalLayout.addWidget(self.office_type)

        self.InportTimeLetter = QRadioButton(self.gridLayoutWidget)
        self.InportTimeLetter.setObjectName(u"InportTimeLetter")
        self.InportTimeLetter.setEnabled(True)

        self.verticalLayout.addWidget(self.InportTimeLetter)


        self.gridLayout.addLayout(self.verticalLayout, 9, 0, 1, 2)

        self.fullname.raise_()
        self.full_name.raise_()
        self.refnum.raise_()
        self.title_position.raise_()
        self.pos_title.raise_()
        self.co_name.raise_()
        self.ref_num.raise_()
        self.last_name.raise_()
        self.co_namerank.raise_()
        self.create_letter.raise_()
        self.load_file.raise_()
        self.Lastname.raise_()
        self.groupBox = QGroupBox(self.GeneratePDF)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(10, 10, 361, 281))
        self.tabWidget.addTab(self.GeneratePDF, "")
        self.groupBox.raise_()
        self.frame.raise_()
        self.TableOptiions = QWidget()
        self.TableOptiions.setObjectName(u"TableOptiions")
        self.Table_tab_frame = QFrame(self.TableOptiions)
        self.Table_tab_frame.setObjectName(u"Table_tab_frame")
        self.Table_tab_frame.setGeometry(QRect(0, 0, 351, 281))
        self.Table_tab_frame.setFrameShape(QFrame.Box)
        self.Table_tab_frame.setFrameShadow(QFrame.Raised)
        self.Table_tab_frame.setLineWidth(4)
        self.Table_options_groupbox = QGroupBox(self.Table_tab_frame)
        self.Table_options_groupbox.setObjectName(u"Table_options_groupbox")
        self.Table_options_groupbox.setEnabled(True)
        self.Table_options_groupbox.setGeometry(QRect(10, 10, 331, 251))
        self.gridLayoutWidget_3 = QWidget(self.Table_options_groupbox)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 311, 241))
        self.table_optins_grid = QGridLayout(self.gridLayoutWidget_3)
        self.table_optins_grid.setObjectName(u"table_optins_grid")
        self.table_optins_grid.setVerticalSpacing(0)
        self.table_optins_grid.setContentsMargins(0, 0, 0, 0)
        self.ShipName = QLineEdit(self.gridLayoutWidget_3)
        self.ShipName.setObjectName(u"ShipName")

        self.table_optins_grid.addWidget(self.ShipName, 0, 2, 1, 1)

        self.rating = QLineEdit(self.gridLayoutWidget_3)
        self.rating.setObjectName(u"rating")

        self.table_optins_grid.addWidget(self.rating, 2, 5, 1, 1)

        self.ops_label_ship = QLabel(self.gridLayoutWidget_3)
        self.ops_label_ship.setObjectName(u"ops_label_ship")

        self.table_optins_grid.addWidget(self.ops_label_ship, 0, 1, 1, 1)

        self.ops_label_HP = QLabel(self.gridLayoutWidget_3)
        self.ops_label_HP.setObjectName(u"ops_label_HP")

        self.table_optins_grid.addWidget(self.ops_label_HP, 1, 4, 1, 1)

        self.grt_lineedit = QLineEdit(self.gridLayoutWidget_3)
        self.grt_lineedit.setObjectName(u"grt_lineedit")

        self.table_optins_grid.addWidget(self.grt_lineedit, 1, 2, 1, 1)

        self.grt = QLabel(self.gridLayoutWidget_3)
        self.grt.setObjectName(u"grt")

        self.table_optins_grid.addWidget(self.grt, 1, 1, 1, 1)

        self.prop = QLineEdit(self.gridLayoutWidget_3)
        self.prop.setObjectName(u"prop")

        self.table_optins_grid.addWidget(self.prop, 2, 2, 1, 1)

        self.ops_label_snumber = QLabel(self.gridLayoutWidget_3)
        self.ops_label_snumber.setObjectName(u"ops_label_snumber")

        self.table_optins_grid.addWidget(self.ops_label_snumber, 0, 4, 1, 1)

        self.ops_label_Rating = QLabel(self.gridLayoutWidget_3)
        self.ops_label_Rating.setObjectName(u"ops_label_Rating")

        self.table_optins_grid.addWidget(self.ops_label_Rating, 2, 4, 1, 1)

        self.ops_label_hours = QLabel(self.gridLayoutWidget_3)
        self.ops_label_hours.setObjectName(u"ops_label_hours")

        self.table_optins_grid.addWidget(self.ops_label_hours, 3, 4, 1, 1)

        self.hours_day = QLineEdit(self.gridLayoutWidget_3)
        self.hours_day.setObjectName(u"hours_day")

        self.table_optins_grid.addWidget(self.hours_day, 3, 5, 1, 1)

        self.Horsepower = QLineEdit(self.gridLayoutWidget_3)
        self.Horsepower.setObjectName(u"Horsepower")

        self.table_optins_grid.addWidget(self.Horsepower, 1, 5, 1, 1)

        self.ops_label_porp = QLabel(self.gridLayoutWidget_3)
        self.ops_label_porp.setObjectName(u"ops_label_porp")

        self.table_optins_grid.addWidget(self.ops_label_porp, 2, 1, 1, 1)

        self.Ship_Number = QLineEdit(self.gridLayoutWidget_3)
        self.Ship_Number.setObjectName(u"Ship_Number")

        self.table_optins_grid.addWidget(self.Ship_Number, 0, 5, 1, 1)

        self.nature = QLineEdit(self.gridLayoutWidget_3)
        self.nature.setObjectName(u"nature")

        self.table_optins_grid.addWidget(self.nature, 3, 2, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.table_optins_grid.addWidget(self.label_18, 3, 1, 1, 1)

        self.Typedays = QLineEdit(self.gridLayoutWidget_3)
        self.Typedays.setObjectName(u"Typedays")

        self.table_optins_grid.addWidget(self.Typedays, 4, 2, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.table_optins_grid.addWidget(self.label_20, 4, 1, 1, 1)

        self.ops_label_HP.raise_()
        self.ops_label_snumber.raise_()
        self.ops_label_Rating.raise_()
        self.ops_label_hours.raise_()
        self.ops_label_porp.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.ShipName.raise_()
        self.ops_label_ship.raise_()
        self.grt.raise_()
        self.grt_lineedit.raise_()
        self.Ship_Number.raise_()
        self.Horsepower.raise_()
        self.rating.raise_()
        self.prop.raise_()
        self.nature.raise_()
        self.hours_day.raise_()
        self.Typedays.raise_()
        self.tabWidget.addTab(self.TableOptiions, "")
        self.make_table_button = QPushButton(self.centralwidget)
        self.make_table_button.setObjectName(u"make_table_button")
        self.make_table_button.setEnabled(False)
        self.make_table_button.setGeometry(QRect(120, 620, 231, 41))
        SeaServiceMaster.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SeaServiceMaster)
        self.statusbar.setObjectName(u"statusbar")
        SeaServiceMaster.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.Lastname, self.co_namerank)
        QWidget.setTabOrder(self.co_namerank, self.refnum)
        QWidget.setTabOrder(self.refnum, self.fullname)
        QWidget.setTabOrder(self.fullname, self.pos_title)
        QWidget.setTabOrder(self.pos_title, self.office_type)
        QWidget.setTabOrder(self.office_type, self.InportTimeLetter)
        QWidget.setTabOrder(self.InportTimeLetter, self.ShipName)
        QWidget.setTabOrder(self.ShipName, self.grt_lineedit)
        QWidget.setTabOrder(self.grt_lineedit, self.prop)
        QWidget.setTabOrder(self.prop, self.nature)
        QWidget.setTabOrder(self.nature, self.Typedays)
        QWidget.setTabOrder(self.Typedays, self.Ship_Number)
        QWidget.setTabOrder(self.Ship_Number, self.Horsepower)
        QWidget.setTabOrder(self.Horsepower, self.rating)
        QWidget.setTabOrder(self.rating, self.hours_day)
        QWidget.setTabOrder(self.hours_day, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.tableView)
        QWidget.setTabOrder(self.tableView, self.load_file)
        QWidget.setTabOrder(self.load_file, self.create_letter)

        self.retranslateUi(SeaServiceMaster)
        self.Lastname.editingFinished.connect(self.load_file.show)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SeaServiceMaster)
    # setupUi

    def retranslateUi(self, SeaServiceMaster):
        SeaServiceMaster.setWindowTitle(QCoreApplication.translate("SeaServiceMaster", u"MainWindow", None))
        self.lcd_leave_label.setText(QCoreApplication.translate("SeaServiceMaster", u"Leave", None))
        self.training_labellcd.setText(QCoreApplication.translate("SeaServiceMaster", u"Training", None))
        self.Seadays_lcd_label.setText(QCoreApplication.translate("SeaServiceMaster", u"Sea Days", None))
        self.inport_lcdlable.setText(QCoreApplication.translate("SeaServiceMaster", u"In Port", None))
        self.absent_labellcd.setText(QCoreApplication.translate("SeaServiceMaster", u"Absent", None))
        self.userinstruction_lobel.setText(QCoreApplication.translate("SeaServiceMaster", u"Start by filling the fields on the right then Load the file. Once everything looks right, select 'create letter' ", None))
        self.INFOBOX.setText(QCoreApplication.translate("SeaServiceMaster", u"Info: make selections", None))
#if QT_CONFIG(tooltip)
        self.GeneratePDF.setToolTip(QCoreApplication.translate("SeaServiceMaster", u"When you fill out all the  info ", None))
#endif // QT_CONFIG(tooltip)
        self.ref_num.setText(QCoreApplication.translate("SeaServiceMaster", u"Reference #", None))
        self.create_letter.setText(QCoreApplication.translate("SeaServiceMaster", u"Create Letter", None))
        self.load_file.setText(QCoreApplication.translate("SeaServiceMaster", u"Load File", None))
        self.co_name.setText(QCoreApplication.translate("SeaServiceMaster", u"CO Name/Rank", None))
        self.refnum.setText(QCoreApplication.translate("SeaServiceMaster", u"Reference #", None))
        self.co_namerank.setText(QCoreApplication.translate("SeaServiceMaster", u"CO's Name And Rank", None))
        self.title_position.setText(QCoreApplication.translate("SeaServiceMaster", u"Position/Title", None))
        self.full_name.setText(QCoreApplication.translate("SeaServiceMaster", u"Full Name", None))
        self.Lastname.setText(QCoreApplication.translate("SeaServiceMaster", u"Last Name of Person", None))
        self.last_name.setText(QCoreApplication.translate("SeaServiceMaster", u"Last Name", None))
        self.office_type.setItemText(0, QCoreApplication.translate("SeaServiceMaster", u"Officer Type", None))
        self.office_type.setItemText(1, QCoreApplication.translate("SeaServiceMaster", u"Deck Type", None))
        self.office_type.setItemText(2, QCoreApplication.translate("SeaServiceMaster", u"Oiler", None))
        self.office_type.setItemText(3, QCoreApplication.translate("SeaServiceMaster", u"Engineering", None))
        self.office_type.setItemText(4, QCoreApplication.translate("SeaServiceMaster", u"Survey", None))

        self.InportTimeLetter.setText(QCoreApplication.translate("SeaServiceMaster", u"Inport Time Letter", None))
        self.groupBox.setTitle(QCoreApplication.translate("SeaServiceMaster", u"Select The Type of Letter to Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneratePDF), QCoreApplication.translate("SeaServiceMaster", u"FILE ", None))
        self.Table_options_groupbox.setTitle(QCoreApplication.translate("SeaServiceMaster", u"Options for the table to display", None))
        self.ShipName.setText(QCoreApplication.translate("SeaServiceMaster", u"Oscar Dyson", None))
        self.rating.setText(QCoreApplication.translate("SeaServiceMaster", u"Ordinary Seaman", None))
        self.ops_label_ship.setText(QCoreApplication.translate("SeaServiceMaster", u"Ship", None))
        self.ops_label_HP.setText(QCoreApplication.translate("SeaServiceMaster", u"HP", None))
        self.grt_lineedit.setText(QCoreApplication.translate("SeaServiceMaster", u"2200", None))
        self.grt.setText(QCoreApplication.translate("SeaServiceMaster", u"GRT", None))
        self.prop.setText(QCoreApplication.translate("SeaServiceMaster", u"Motor", None))
        self.ops_label_snumber.setText(QCoreApplication.translate("SeaServiceMaster", u"Number", None))
        self.ops_label_Rating.setText(QCoreApplication.translate("SeaServiceMaster", u"Rating", None))
        self.ops_label_hours.setText(QCoreApplication.translate("SeaServiceMaster", u"Hours", None))
        self.hours_day.setText(QCoreApplication.translate("SeaServiceMaster", u"12", None))
        self.Horsepower.setText(QCoreApplication.translate("SeaServiceMaster", u"3094", None))
        self.ops_label_porp.setText(QCoreApplication.translate("SeaServiceMaster", u"Propulsion", None))
        self.Ship_Number.setText(QCoreApplication.translate("SeaServiceMaster", u"9270335", None))
        self.nature.setText(QCoreApplication.translate("SeaServiceMaster", u"Coastwise", None))
        self.label_18.setText(QCoreApplication.translate("SeaServiceMaster", u"Nature", None))
        self.Typedays.setText(QCoreApplication.translate("SeaServiceMaster", u"Underway", None))
        self.label_20.setText(QCoreApplication.translate("SeaServiceMaster", u"Type Days", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TableOptiions), QCoreApplication.translate("SeaServiceMaster", u"TABLE", None))
        self.make_table_button.setText(QCoreApplication.translate("SeaServiceMaster", u"Create Table", None))
    # retranslateUi

