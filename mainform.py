# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Fri Dec  5 18:09:14 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 681)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/fb-icon16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_search = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_search)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.frame_search)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_2.addWidget(self.dateTimeEdit_2, 0, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 2, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 0, 3, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 0, 4, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 0, 5, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 1, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 1, 3, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 5, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 2, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 2, 3, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_search)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 2, 4, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 2, 5, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_search = QtWidgets.QPushButton(self.frame_search)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-edit-find-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QtCore.QSize(24, 24))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 6)
        self.gridLayout_9.addWidget(self.frame_search, 0, 0, 1, 1)
        self.frame_edit = QtWidgets.QFrame(self.frame)
        self.frame_edit.setObjectName("frame_edit")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_edit)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_edit)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.edit_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_name.setObjectName("edit_name")
        self.gridLayout_3.addWidget(self.edit_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.edit_date_from = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.edit_date_from.setCalendarPopup(True)
        self.edit_date_from.setObjectName("edit_date_from")
        self.gridLayout_3.addWidget(self.edit_date_from, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.edit_date_to = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.edit_date_to.setCalendarPopup(True)
        self.edit_date_to.setObjectName("edit_date_to")
        self.gridLayout_3.addWidget(self.edit_date_to, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.cb_festival = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_festival.setObjectName("cb_festival")
        self.gridLayout_3.addWidget(self.cb_festival, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)
        self.edit_state = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_state.setObjectName("edit_state")
        self.gridLayout_3.addWidget(self.edit_state, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)
        self.edit_city = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_city.setObjectName("edit_city")
        self.gridLayout_3.addWidget(self.edit_city, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 6, 0, 1, 1)
        self.edit_hall = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_hall.setObjectName("edit_hall")
        self.gridLayout_3.addWidget(self.edit_hall, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.edit_type = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_type.setObjectName("edit_type")
        self.gridLayout_3.addWidget(self.edit_type, 7, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_edit)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setMinimumSize(QtCore.QSize(0, 22))
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.edit_note = QtWidgets.QTextEdit(self.groupBox_3)
        self.edit_note.setObjectName("edit_note")
        self.gridLayout_6.addWidget(self.edit_note, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_edit)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.btn_dirigents_add = QtWidgets.QToolButton(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-list-add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dirigents_add.setIcon(icon2)
        self.btn_dirigents_add.setAutoRaise(True)
        self.btn_dirigents_add.setObjectName("btn_dirigents_add")
        self.gridLayout_8.addWidget(self.btn_dirigents_add, 0, 1, 1, 1)
        self.btn_dirigents_remove = QtWidgets.QToolButton(self.groupBox_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-list-remove-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dirigents_remove.setIcon(icon3)
        self.btn_dirigents_remove.setAutoRaise(True)
        self.btn_dirigents_remove.setObjectName("btn_dirigents_remove")
        self.gridLayout_8.addWidget(self.btn_dirigents_remove, 0, 2, 1, 1)
        self.lw_edit_dirigents = QtWidgets.QListWidget(self.groupBox_4)
        self.lw_edit_dirigents.setObjectName("lw_edit_dirigents")
        self.gridLayout_8.addWidget(self.lw_edit_dirigents, 1, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_edit)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.btn_choirs_add = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_choirs_add.setIcon(icon2)
        self.btn_choirs_add.setAutoRaise(True)
        self.btn_choirs_add.setObjectName("btn_choirs_add")
        self.gridLayout_5.addWidget(self.btn_choirs_add, 0, 1, 1, 1)
        self.btn_choirs_remove = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_choirs_remove.setIcon(icon3)
        self.btn_choirs_remove.setAutoRaise(True)
        self.btn_choirs_remove.setObjectName("btn_choirs_remove")
        self.gridLayout_5.addWidget(self.btn_choirs_remove, 0, 2, 1, 1)
        self.lw_edit_choirs = QtWidgets.QListWidget(self.groupBox_5)
        self.lw_edit_choirs.setObjectName("lw_edit_choirs")
        self.gridLayout_5.addWidget(self.lw_edit_choirs, 1, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_5, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_edit_confirm = QtWidgets.QPushButton(self.frame_edit)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-dialog-ok-apply-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_confirm.setIcon(icon4)
        self.btn_edit_confirm.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit_confirm.setObjectName("btn_edit_confirm")
        self.horizontalLayout.addWidget(self.btn_edit_confirm)
        self.btn_edit_save = QtWidgets.QPushButton(self.frame_edit)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-document-save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_save.setIcon(icon5)
        self.btn_edit_save.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit_save.setObjectName("btn_edit_save")
        self.horizontalLayout.addWidget(self.btn_edit_save)
        self.btn_edit_cancel = QtWidgets.QPushButton(self.frame_edit)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-dialog-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_cancel.setIcon(icon6)
        self.btn_edit_cancel.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit_cancel.setObjectName("btn_edit_cancel")
        self.horizontalLayout.addWidget(self.btn_edit_cancel)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.frame_edit)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.btn_works_add = QtWidgets.QToolButton(self.groupBox)
        self.btn_works_add.setIcon(icon2)
        self.btn_works_add.setAutoRaise(True)
        self.btn_works_add.setObjectName("btn_works_add")
        self.gridLayout.addWidget(self.btn_works_add, 0, 1, 1, 1)
        self.btn_works_add_soloist = QtWidgets.QToolButton(self.groupBox)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-list-add-user-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_works_add_soloist.setIcon(icon7)
        self.btn_works_add_soloist.setAutoRaise(True)
        self.btn_works_add_soloist.setObjectName("btn_works_add_soloist")
        self.gridLayout.addWidget(self.btn_works_add_soloist, 0, 2, 1, 1)
        self.btn_works_remove = QtWidgets.QToolButton(self.groupBox)
        self.btn_works_remove.setIcon(icon3)
        self.btn_works_remove.setAutoRaise(True)
        self.btn_works_remove.setObjectName("btn_works_remove")
        self.gridLayout.addWidget(self.btn_works_remove, 0, 3, 1, 1)
        self.tw_edit_works = QtWidgets.QTreeWidget(self.groupBox)
        self.tw_edit_works.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_edit_works.setAnimated(True)
        self.tw_edit_works.setObjectName("tw_edit_works")
        self.tw_edit_works.headerItem().setText(0, "1")
        self.tw_edit_works.header().setVisible(False)
        self.gridLayout.addWidget(self.tw_edit_works, 1, 0, 1, 4)
        self.gridLayout_7.addWidget(self.groupBox, 0, 1, 1, 2)
        self.gridLayout_9.addWidget(self.frame_edit, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout_12.addWidget(self.tableView, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchiv = QtWidgets.QMenu(self.menubar)
        self.menuArchiv.setObjectName("menuArchiv")
        self.menuZaznam = QtWidgets.QMenu(self.menubar)
        self.menuZaznam.setObjectName("menuZaznam")
        self.menuPomocnik = QtWidgets.QMenu(self.menubar)
        self.menuPomocnik.setObjectName("menuPomocnik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionPridat_zaznam = QtWidgets.QAction(MainWindow)
        self.actionPridat_zaznam.setObjectName("actionPridat_zaznam")
        self.actionUpravit_zaznam = QtWidgets.QAction(MainWindow)
        self.actionUpravit_zaznam.setObjectName("actionUpravit_zaznam")
        self.actionOdstranit_zaznam = QtWidgets.QAction(MainWindow)
        self.actionOdstranit_zaznam.setObjectName("actionOdstranit_zaznam")
        self.actionUkoncit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-application-exit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUkoncit.setIcon(icon8)
        self.actionUkoncit.setObjectName("actionUkoncit")
        self.actionPridat = QtWidgets.QAction(MainWindow)
        self.actionPridat.setIcon(icon2)
        self.actionPridat.setObjectName("actionPridat")
        self.actionUpravit = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/Actions-document-edit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpravit.setIcon(icon9)
        self.actionUpravit.setObjectName("actionUpravit")
        self.actionOdstranit = QtWidgets.QAction(MainWindow)
        self.actionOdstranit.setIcon(icon3)
        self.actionOdstranit.setObjectName("actionOdstranit")
        self.actionO_programe = QtWidgets.QAction(MainWindow)
        self.actionO_programe.setObjectName("actionO_programe")
        self.actionSprava_festivalov = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/Places-folder-sound-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSprava_festivalov.setIcon(icon10)
        self.actionSprava_festivalov.setObjectName("actionSprava_festivalov")
        self.menuArchiv.addAction(self.actionSprava_festivalov)
        self.menuArchiv.addSeparator()
        self.menuArchiv.addAction(self.actionUkoncit)
        self.menuZaznam.addAction(self.actionPridat)
        self.menuZaznam.addAction(self.actionUpravit)
        self.menuZaznam.addAction(self.actionOdstranit)
        self.menuPomocnik.addAction(self.actionO_programe)
        self.menubar.addAction(self.menuArchiv.menuAction())
        self.menubar.addAction(self.menuZaznam.menuAction())
        self.menubar.addAction(self.menuPomocnik.menuAction())
        self.toolBar.addAction(self.actionSprava_festivalov)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUkoncit)
        self.toolBar_2.addAction(self.actionPridat)
        self.toolBar_2.addAction(self.actionUpravit)
        self.toolBar_2.addAction(self.actionOdstranit)

        self.retranslateUi(MainWindow)
        self.actionUkoncit.triggered['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edit_name, self.edit_date_from)
        MainWindow.setTabOrder(self.edit_date_from, self.edit_date_to)
        MainWindow.setTabOrder(self.edit_date_to, self.cb_festival)
        MainWindow.setTabOrder(self.cb_festival, self.edit_state)
        MainWindow.setTabOrder(self.edit_state, self.edit_city)
        MainWindow.setTabOrder(self.edit_city, self.edit_hall)
        MainWindow.setTabOrder(self.edit_hall, self.edit_type)
        MainWindow.setTabOrder(self.edit_type, self.tw_edit_works)
        MainWindow.setTabOrder(self.tw_edit_works, self.btn_works_add)
        MainWindow.setTabOrder(self.btn_works_add, self.btn_works_remove)
        MainWindow.setTabOrder(self.btn_works_remove, self.edit_note)
        MainWindow.setTabOrder(self.edit_note, self.lw_edit_dirigents)
        MainWindow.setTabOrder(self.lw_edit_dirigents, self.btn_dirigents_add)
        MainWindow.setTabOrder(self.btn_dirigents_add, self.btn_dirigents_remove)
        MainWindow.setTabOrder(self.btn_dirigents_remove, self.lw_edit_choirs)
        MainWindow.setTabOrder(self.lw_edit_choirs, self.btn_choirs_add)
        MainWindow.setTabOrder(self.btn_choirs_add, self.btn_choirs_remove)
        MainWindow.setTabOrder(self.btn_choirs_remove, self.btn_edit_confirm)
        MainWindow.setTabOrder(self.btn_edit_confirm, self.btn_edit_save)
        MainWindow.setTabOrder(self.btn_edit_save, self.btn_edit_cancel)
        MainWindow.setTabOrder(self.btn_edit_cancel, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.checkBox_5)
        MainWindow.setTabOrder(self.checkBox_5, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.checkBox_8)
        MainWindow.setTabOrder(self.checkBox_8, self.checkBox_6)
        MainWindow.setTabOrder(self.checkBox_6, self.lineEdit_14)
        MainWindow.setTabOrder(self.lineEdit_14, self.checkBox_7)
        MainWindow.setTabOrder(self.checkBox_7, self.lineEdit_15)
        MainWindow.setTabOrder(self.lineEdit_15, self.tableView)
        MainWindow.setTabOrder(self.tableView, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.lineEdit_16)
        MainWindow.setTabOrder(self.lineEdit_16, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.checkBox_9)
        MainWindow.setTabOrder(self.checkBox_9, self.dateTimeEdit_2)
        MainWindow.setTabOrder(self.dateTimeEdit_2, self.checkBox_4)
        MainWindow.setTabOrder(self.checkBox_4, self.btn_search)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filharmonie Brno - Arcihv koncertů"))
        self.checkBox.setText(_translate("MainWindow", "Datum:"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("MainWindow", "d. M. yyyy"))
        self.checkBox_4.setText(_translate("MainWindow", "Festival:"))
        self.checkBox_7.setText(_translate("MainWindow", "Solisti:"))
        self.checkBox_2.setText(_translate("MainWindow", "Místo konání:"))
        self.checkBox_5.setText(_translate("MainWindow", "Skladatel:"))
        self.checkBox_8.setText(_translate("MainWindow", "Dirigent:"))
        self.checkBox_3.setText(_translate("MainWindow", "Typ koncertu:"))
        self.checkBox_6.setText(_translate("MainWindow", "Skladba:"))
        self.checkBox_9.setText(_translate("MainWindow", "Poznámka:"))
        self.btn_search.setText(_translate("MainWindow", "Hledat"))
        self.label_11.setText(_translate("MainWindow", "Název:"))
        self.label.setText(_translate("MainWindow", "Datum od:"))
        self.edit_date_from.setDisplayFormat(_translate("MainWindow", "d. M. yyyy"))
        self.label_12.setText(_translate("MainWindow", "Datum do:"))
        self.edit_date_to.setDisplayFormat(_translate("MainWindow", "d. M. yyyy"))
        self.label_9.setText(_translate("MainWindow", "Festival:"))
        self.label_2.setText(_translate("MainWindow", "Stát konání:"))
        self.label_3.setText(_translate("MainWindow", "Město konání:"))
        self.label_5.setText(_translate("MainWindow", "Sál:"))
        self.label_4.setText(_translate("MainWindow", "Typ koncertu:"))
        self.label_8.setText(_translate("MainWindow", "Poznámka"))
        self.label_7.setText(_translate("MainWindow", "Dirigenti"))
        self.btn_dirigents_add.setToolTip(_translate("MainWindow", "Přidat dirigenta..."))
        self.btn_dirigents_add.setText(_translate("MainWindow", "..."))
        self.btn_dirigents_remove.setToolTip(_translate("MainWindow", "Odstránit záznam"))
        self.btn_dirigents_remove.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "Sbory"))
        self.btn_choirs_add.setToolTip(_translate("MainWindow", "Přidat sbor..."))
        self.btn_choirs_add.setText(_translate("MainWindow", "..."))
        self.btn_choirs_remove.setToolTip(_translate("MainWindow", "Odstránit záznam"))
        self.btn_choirs_remove.setText(_translate("MainWindow", "..."))
        self.btn_edit_confirm.setText(_translate("MainWindow", "Přidat"))
        self.btn_edit_save.setText(_translate("MainWindow", "Upravit"))
        self.btn_edit_cancel.setText(_translate("MainWindow", "Zrušit"))
        self.label_6.setText(_translate("MainWindow", "Skladatel, skladba, solisti"))
        self.btn_works_add.setToolTip(_translate("MainWindow", "Přidat skladatela a skladbu..."))
        self.btn_works_add.setText(_translate("MainWindow", "..."))
        self.btn_works_add_soloist.setToolTip(_translate("MainWindow", "Přidat solistu..."))
        self.btn_works_add_soloist.setText(_translate("MainWindow", "..."))
        self.btn_works_remove.setToolTip(_translate("MainWindow", "Odstránit záznam"))
        self.btn_works_remove.setText(_translate("MainWindow", "..."))
        self.menuArchiv.setTitle(_translate("MainWindow", "Archiv"))
        self.menuZaznam.setTitle(_translate("MainWindow", "Záznam"))
        self.menuPomocnik.setTitle(_translate("MainWindow", "Pomocník"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionPridat_zaznam.setText(_translate("MainWindow", "Pridat zaznam"))
        self.actionUpravit_zaznam.setText(_translate("MainWindow", "Upravit zaznam"))
        self.actionOdstranit_zaznam.setText(_translate("MainWindow", "Odstranit zaznam"))
        self.actionUkoncit.setText(_translate("MainWindow", "Ukončit"))
        self.actionPridat.setText(_translate("MainWindow", "Přidat"))
        self.actionUpravit.setText(_translate("MainWindow", "Upravit"))
        self.actionOdstranit.setText(_translate("MainWindow", "Odstranit"))
        self.actionO_programe.setText(_translate("MainWindow", "O programe"))
        self.actionSprava_festivalov.setText(_translate("MainWindow", "Správa festivalů"))

import resource_rc
