# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCPEdit.ui'
#
# Created: Sun Nov 14 21:57:12 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 807)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_streams = QtGui.QWidget()
        self.tab_streams.setObjectName("tab_streams")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_streams)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtGui.QSplitter(self.tab_streams)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setLineWidth(3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tablestreams = QtGui.QTableView(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        self.tablestreams.setFont(font)
        self.tablestreams.setMidLineWidth(3)
        self.tablestreams.setAutoScroll(True)
        self.tablestreams.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablestreams.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablestreams.setGridStyle(QtCore.Qt.SolidLine)
        self.tablestreams.setSortingEnabled(True)
        self.tablestreams.setObjectName("tablestreams")
        self.tablestreams.horizontalHeader().setStretchLastSection(True)
        self.tablestreams.verticalHeader().setVisible(False)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btnicept = QtGui.QPushButton(self.layoutWidget)
        self.btnicept.setCheckable(True)
        self.btnicept.setObjectName("btnicept")
        self.horizontalLayout.addWidget(self.btnicept)
        self.btnauto = QtGui.QPushButton(self.layoutWidget)
        self.btnauto.setCheckable(True)
        self.btnauto.setObjectName("btnauto")
        self.horizontalLayout.addWidget(self.btnauto)
        self.btnsend = QtGui.QPushButton(self.layoutWidget)
        self.btnsend.setObjectName("btnsend")
        self.horizontalLayout.addWidget(self.btnsend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabtext = QtGui.QWidget()
        self.tabtext.setObjectName("tabtext")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabtext)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnsavetext = QtGui.QPushButton(self.tabtext)
        self.btnsavetext.setObjectName("btnsavetext")
        self.verticalLayout_2.addWidget(self.btnsavetext)
        self.textstream = QtGui.QPlainTextEdit(self.tabtext)
        self.textstream.setObjectName("textstream")
        self.verticalLayout_2.addWidget(self.textstream)
        self.tabWidget.addTab(self.tabtext, "")
        self.tabhex = QtGui.QWidget()
        self.tabhex.setObjectName("tabhex")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabhex)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnsavehex = QtGui.QPushButton(self.tabhex)
        self.btnsavehex.setObjectName("btnsavehex")
        self.verticalLayout_3.addWidget(self.btnsavehex)
        self.tablehex = QtGui.QTableWidget(self.tabhex)
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(10)
        self.tablehex.setFont(font)
        self.tablehex.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tablehex.setTextElideMode(QtCore.Qt.ElideNone)
        self.tablehex.setRowCount(10)
        self.tablehex.setObjectName("tablehex")
        self.tablehex.setColumnCount(16)
        self.tablehex.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tablehex.setItem(1, 2, item)
        self.tablehex.horizontalHeader().setDefaultSectionSize(22)
        self.tablehex.horizontalHeader().setMinimumSectionSize(22)
        self.tablehex.horizontalHeader().setStretchLastSection(True)
        self.tablehex.verticalHeader().setDefaultSectionSize(18)
        self.tablehex.verticalHeader().setMinimumSectionSize(12)
        self.verticalLayout_3.addWidget(self.tablehex)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabhex, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.tabWidget_2.addTab(self.tab_streams, "")
        self.tab_rules = QtGui.QWidget()
        self.tab_rules.setObjectName("tab_rules")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab_rules)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.splitter_2 = QtGui.QSplitter(self.tab_rules)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_5 = QtGui.QWidget(self.layoutWidget1)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setMargin(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtGui.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.buttondelrule = QtGui.QPushButton(self.widget_5)
        self.buttondelrule.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttondelrule.setObjectName("buttondelrule")
        self.horizontalLayout_5.addWidget(self.buttondelrule)
        self.buttonaddrule = QtGui.QPushButton(self.widget_5)
        self.buttonaddrule.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonaddrule.setObjectName("buttonaddrule")
        self.horizontalLayout_5.addWidget(self.buttonaddrule)
        self.buttondown = QtGui.QPushButton(self.widget_5)
        self.buttondown.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttondown.setObjectName("buttondown")
        self.horizontalLayout_5.addWidget(self.buttondown)
        self.buttonup = QtGui.QPushButton(self.widget_5)
        self.buttonup.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonup.setObjectName("buttonup")
        self.horizontalLayout_5.addWidget(self.buttonup)
        self.verticalLayout_6.addWidget(self.widget_5)
        self.listrules = QtGui.QListView(self.layoutWidget1)
        self.listrules.setDragEnabled(True)
        self.listrules.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listrules.setMovement(QtGui.QListView.Free)
        self.listrules.setViewMode(QtGui.QListView.ListMode)
        self.listrules.setObjectName("listrules")
        self.verticalLayout_6.addWidget(self.listrules)
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setToolTip("")
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.group = QtGui.QGroupBox(self.widget)
        self.group.setObjectName("group")
        self.formLayout = QtGui.QFormLayout(self.group)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.group)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.linename = QtGui.QLineEdit(self.group)
        self.linename.setInputMask("")
        self.linename.setObjectName("linename")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linename)
        self.label_3 = QtGui.QLabel(self.group)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.widget_4 = QtGui.QWidget(self.group)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radio_dir_s2c = QtGui.QRadioButton(self.widget_4)
        self.radio_dir_s2c.setObjectName("radio_dir_s2c")
        self.horizontalLayout_4.addWidget(self.radio_dir_s2c)
        self.radio_dir_c2s = QtGui.QRadioButton(self.widget_4)
        self.radio_dir_c2s.setObjectName("radio_dir_c2s")
        self.horizontalLayout_4.addWidget(self.radio_dir_c2s)
        self.radio_dir_both = QtGui.QRadioButton(self.widget_4)
        self.radio_dir_both.setChecked(True)
        self.radio_dir_both.setObjectName("radio_dir_both")
        self.horizontalLayout_4.addWidget(self.radio_dir_both)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.widget_4)
        self.label_4 = QtGui.QLabel(self.group)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineaddr = QtGui.QLineEdit(self.group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineaddr.sizePolicy().hasHeightForWidth())
        self.lineaddr.setSizePolicy(sizePolicy)
        self.lineaddr.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineaddr.setObjectName("lineaddr")
        self.horizontalLayout_10.addWidget(self.lineaddr)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label_5 = QtGui.QLabel(self.group)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.lineport = QtGui.QLineEdit(self.group)
        self.lineport.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineport.setBaseSize(QtCore.QSize(150, 0))
        self.lineport.setMaxLength(6)
        self.lineport.setCursorPosition(0)
        self.lineport.setObjectName("lineport")
        self.horizontalLayout_10.addWidget(self.lineport)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.label_8 = QtGui.QLabel(self.group)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.widget_6 = QtGui.QWidget(self.group)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radio_type_nothing = QtGui.QRadioButton(self.widget_6)
        self.radio_type_nothing.setChecked(True)
        self.radio_type_nothing.setObjectName("radio_type_nothing")
        self.horizontalLayout_6.addWidget(self.radio_type_nothing)
        self.radio_type_debug = QtGui.QRadioButton(self.widget_6)
        self.radio_type_debug.setObjectName("radio_type_debug")
        self.horizontalLayout_6.addWidget(self.radio_type_debug)
        self.radio_type_muck = QtGui.QRadioButton(self.widget_6)
        self.radio_type_muck.setObjectName("radio_type_muck")
        self.horizontalLayout_6.addWidget(self.radio_type_muck)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.widget_6)
        self.label_9 = QtGui.QLabel(self.group)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.linepayload = QtGui.QLineEdit(self.group)
        self.linepayload.setObjectName("linepayload")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.linepayload)
        self.label_6 = QtGui.QLabel(self.group)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.textruleobj = QtGui.QPlainTextEdit(self.group)
        self.textruleobj.setObjectName("textruleobj")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.textruleobj)
        self.label_10 = QtGui.QLabel(self.group)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_10)
        self.widget_7 = QtGui.QWidget(self.group)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radio_passthru_yes = QtGui.QRadioButton(self.widget_7)
        self.radio_passthru_yes.setObjectName("radio_passthru_yes")
        self.horizontalLayout_7.addWidget(self.radio_passthru_yes)
        self.radio_passthru_no = QtGui.QRadioButton(self.widget_7)
        self.radio_passthru_no.setChecked(True)
        self.radio_passthru_no.setObjectName("radio_passthru_no")
        self.horizontalLayout_7.addWidget(self.radio_passthru_no)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.widget_7)
        self.verticalLayout_7.addWidget(self.group)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.buttonpreviewrule = QtGui.QPushButton(self.widget)
        self.buttonpreviewrule.setObjectName("buttonpreviewrule")
        self.horizontalLayout_8.addWidget(self.buttonpreviewrule)
        self.saverule = QtGui.QPushButton(self.widget)
        self.saverule.setObjectName("saverule")
        self.horizontalLayout_8.addWidget(self.saverule)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.labelrulepreview = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.labelrulepreview.setFont(font)
        self.labelrulepreview.setObjectName("labelrulepreview")
        self.verticalLayout_7.addWidget(self.labelrulepreview)
        self.textrulepreview = QtGui.QPlainTextEdit(self.widget)
        self.textrulepreview.setObjectName("textrulepreview")
        self.verticalLayout_7.addWidget(self.textrulepreview)
        self.horizontalLayout_11.addWidget(self.splitter_2)
        self.tabWidget_2.addTab(self.tab_rules, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.listWidget_objects = QtGui.QListWidget(self.splitter_4)
        self.listWidget_objects.setObjectName("listWidget_objects")
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.treeWidget_objectinspector = QtGui.QTreeWidget(self.splitter_3)
        self.treeWidget_objectinspector.setColumnCount(2)
        self.treeWidget_objectinspector.setObjectName("treeWidget_objectinspector")
        self.treeWidget_objectinspector.headerItem().setText(0, "1")
        self.treeWidget_objectinspector.headerItem().setText(1, "2")
        self.plainTextEdit_objectInspector = QtGui.QPlainTextEdit(self.splitter_3)
        self.plainTextEdit_objectInspector.setObjectName("plainTextEdit_objectInspector")
        self.verticalLayout_4.addWidget(self.splitter_4)
        self.tabWidget_2.addTab(self.tab, "")
        self.horizontalLayout_9.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 23))
        self.menubar.setObjectName("menubar")
        self.menuMallory = QtGui.QMenu(self.menubar)
        self.menuMallory.setObjectName("menuMallory")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFlow_Config = QtGui.QAction(MainWindow)
        self.actionFlow_Config.setObjectName("actionFlow_Config")
        self.menubar.addAction(self.menuMallory.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TCP Debugger", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setToolTip(QtGui.QApplication.translate("MainWindow", "An IP address to match. Blank for wildcard match.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Actions:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnicept.setToolTip(QtGui.QApplication.translate("MainWindow", "Tell Mallory the Debugger wants to intercept traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.btnicept.setText(QtGui.QApplication.translate("MainWindow", "Intercept", None, QtGui.QApplication.UnicodeUTF8))
        self.btnauto.setToolTip(QtGui.QApplication.translate("MainWindow", "Automagically send all packets", None, QtGui.QApplication.UnicodeUTF8))
        self.btnauto.setText(QtGui.QApplication.translate("MainWindow", "Auto Send", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsend.setToolTip(QtGui.QApplication.translate("MainWindow", "Send the selected packet", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsend.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "Save changes made during text editing", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsavetext.setText(QtGui.QApplication.translate("MainWindow", "Save Text Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabtext), QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsavehex.setToolTip(QtGui.QApplication.translate("MainWindow", "Save changes made during hex editing", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsavehex.setText(QtGui.QApplication.translate("MainWindow", "Save Hex Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(10).setText(QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(11).setText(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(12).setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(13).setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(14).setText(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.horizontalHeaderItem(15).setText(QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tablehex.isSortingEnabled()
        self.tablehex.setSortingEnabled(False)
        self.tablehex.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "AA", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.item(0, 1).setText(QtGui.QApplication.translate("MainWindow", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.item(1, 2).setText(QtGui.QApplication.translate("MainWindow", "0C", None, QtGui.QApplication.UnicodeUTF8))
        self.tablehex.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabhex), QtGui.QApplication.translate("MainWindow", "Hex", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_streams), QtGui.QApplication.translate("MainWindow", "Streams", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("MainWindow", "Listing of current rules", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Rule List", None, QtGui.QApplication.UnicodeUTF8))
        self.buttondelrule.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonaddrule.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.buttondown.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the selected rule down one level in precedence", None, QtGui.QApplication.UnicodeUTF8))
        self.buttondown.setText(QtGui.QApplication.translate("MainWindow", "\\/", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonup.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the selected rule up one level in precedence", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonup.setText(QtGui.QApplication.translate("MainWindow", "/\\", None, QtGui.QApplication.UnicodeUTF8))
        self.group.setTitle(QtGui.QApplication.translate("MainWindow", "Rule Specification", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("MainWindow", "This is the name of the rule. Anything that is a valid python name is valid here. Stick with numbers, letters and lower case letters to make the python style deities happy.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.linename.setText(QtGui.QApplication.translate("MainWindow", "default", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("MainWindow", "The direction the rule should match on. Server 2 Client (S2C) rules will only match. Any may be selected to match both directions.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_dir_s2c.setText(QtGui.QApplication.translate("MainWindow", "S2C", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_dir_c2s.setText(QtGui.QApplication.translate("MainWindow", "C2S", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_dir_both.setText(QtGui.QApplication.translate("MainWindow", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.lineaddr.setToolTip(QtGui.QApplication.translate("MainWindow", "The IP address that should be matched.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineaddr.setInputMask(QtGui.QApplication.translate("MainWindow", "000.000.000.000;_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.lineport.setToolTip(QtGui.QApplication.translate("MainWindow", "The port to match. 0 for wildcard match.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_type_nothing.setText(QtGui.QApplication.translate("MainWindow", "Nothing", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_type_debug.setText(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_type_muck.setText(QtGui.QApplication.translate("MainWindow", "Muck", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(QtGui.QApplication.translate("MainWindow", "Specify a string in the payload field. Any time that string is encountered in the payload/stream it will cause the rule to match the packet.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rule can be <span style=\" font-weight:600;\">Nothing</span>, <span style=\" font-weight:600;\">Debug</span> or <span style=\" font-weight:600;\">Muck</span>. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muck rules are special and require a comma separated array of mucks. A muck is a sed like regular expression. Muck rules only apply of type <span style=\" font-weight:600;\">Muck</span> is selected.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muck rules must be separated by a newline character. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here are a few examples of valid Muck rules:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#780000;\">\"gzip,deflate/ /1\"</span>,<span style=\" color:#780000;\">\"deflate/ /1\"</span>,<span style=\" color:#780000;\">\"gzip/ /1\"</span>. This rule replaced the strings gzip, deflate, deflate and gzip with a space. Another example would be to replace all upper case characters with the letter \'a\', <span style=\" color:#780000;\">\"[A-Z]/a/g\"</span>, Muck rules are created by the following syntax: [python regex]/replacement/[number of occurences] where g can be used in number of occurences for infinity (and beyond).</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Muck", None, QtGui.QApplication.UnicodeUTF8))
        self.textruleobj.setPlainText(QtGui.QApplication.translate("MainWindow", "\"search/replace/g\"\n"
"\"search/replace/3\"\n"
"\"search/replace/g\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Passthru", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_passthru_yes.setText(QtGui.QApplication.translate("MainWindow", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_passthru_no.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonpreviewrule.setText(QtGui.QApplication.translate("MainWindow", "Preview Rule", None, QtGui.QApplication.UnicodeUTF8))
        self.saverule.setText(QtGui.QApplication.translate("MainWindow", "Save Rule", None, QtGui.QApplication.UnicodeUTF8))
        self.labelrulepreview.setToolTip(QtGui.QApplication.translate("MainWindow", "This preview can also be pasted directly into the ruleconfig.py static rule configuation. Remember to pay attention to the ordering of the rules in ruleconfig.py.", None, QtGui.QApplication.UnicodeUTF8))
        self.labelrulepreview.setText(QtGui.QApplication.translate("MainWindow", "Rule Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_rules), QtGui.QApplication.translate("MainWindow", "Rules", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMallory.setTitle(QtGui.QApplication.translate("MainWindow", "Mallory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFlow_Config.setText(QtGui.QApplication.translate("MainWindow", "Flow Config", None, QtGui.QApplication.UnicodeUTF8))

