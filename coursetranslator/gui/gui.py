# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(1045,550)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.bSelectMedia = QtWidgets.QPushButton(self.centralwidget)
        self.bSelectMedia.setGeometry(QtCore.QRect(10, 10, 141, 34))
        self.bSelectMedia.setObjectName("bSelectMedia")
        self.bConvert = QtWidgets.QPushButton(self.centralwidget)
        self.bConvert.setEnabled(False)
        self.bConvert.setGeometry(QtCore.QRect(200, 370, 341, 34))
        self.bConvert.setObjectName("bConvert")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 460, 1021, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.labelCurrentOperation = QtWidgets.QLabel(self.centralwidget)
        self.labelCurrentOperation.setGeometry(QtCore.QRect(170, 400, 871, 41))
        self.labelCurrentOperation.setText("")
        self.labelCurrentOperation.setObjectName("labelCurrentOperation")
        self.bOpenOutputFolder = QtWidgets.QPushButton(self.centralwidget)
        self.bOpenOutputFolder.setGeometry(QtCore.QRect(550, 370, 241, 34))
        self.bOpenOutputFolder.setObjectName("bOpenOutputFolder")
        self.bSelectOutputFolder = QtWidgets.QPushButton(self.centralwidget)
        self.bSelectOutputFolder.setGeometry(QtCore.QRect(10, 180, 141, 34))
        self.bSelectOutputFolder.setObjectName("bSelectOutputFolder")
        self.qleOutputFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.qleOutputFolder.setGeometry(QtCore.QRect(160, 180, 861, 32))
        self.qleOutputFolder.setText("")
        self.qleOutputFolder.setReadOnly(True)
        self.qleOutputFolder.setObjectName("qleOutputFolder")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 10, 871, 161))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.qlwListFilesSelected = QtWidgets.QListWidget(self.groupBox)
        self.qlwListFilesSelected.setGeometry(QtCore.QRect(10, 30, 851, 121))
        self.qlwListFilesSelected.setObjectName("qlwListFilesSelected")
        self.bRemoveFile = QtWidgets.QPushButton(self.centralwidget)
        self.bRemoveFile.setGeometry(QtCore.QRect(10, 50, 141, 34))
        self.bRemoveFile.setObjectName("bRemoveFile")
        self.labelProgressFileIndex = QtWidgets.QLabel(self.centralwidget)
        self.labelProgressFileIndex.setGeometry(QtCore.QRect(30, 350, 131, 41))
        self.labelProgressFileIndex.setText("")
        self.labelProgressFileIndex.setObjectName("labelProgressFileIndex")
        self.bCancel = QtWidgets.QPushButton(self.centralwidget)
        self.bCancel.setGeometry(QtCore.QRect(530, 420, 108, 36))
        self.bCancel.setObjectName("bCancel")
        self.chbxOpenOutputFilesAuto = QtWidgets.QCheckBox(self.centralwidget)
        self.chbxOpenOutputFilesAuto.setGeometry(QtCore.QRect(10, 220, 291, 32))
        self.chbxOpenOutputFilesAuto.setChecked(True)
        self.chbxOpenOutputFilesAuto.setObjectName("chbxOpenOutputFilesAuto")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 250, 591, 34))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelSelectLang = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelSelectLang.setObjectName("labelSelectLang")
        self.horizontalLayout_5.addWidget(self.labelSelectLang)
        self.cbSelectLang = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cbSelectLang.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbSelectLang.setObjectName("cbSelectLang")
        self.horizontalLayout_5.addWidget(self.cbSelectLang)
        
        
        self.labelSelectLangTranslate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelSelectLangTranslate.setObjectName("labelSelectLangTranslate")
        self.horizontalLayout_5.addWidget(self.labelSelectLangTranslate)
        self.cbSelectLangTranslate = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cbSelectLangTranslate.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbSelectLangTranslate.setObjectName("cbSelectLangTranslate")
        self.horizontalLayout_5.addWidget(self.cbSelectLangTranslate)
        
       
        
        self.qleApiKey = QtWidgets.QLineEdit(self.centralwidget)
        self.qleApiKey.setEnabled(True)
        self.qleApiKey.setGeometry(QtCore.QRect(480, 300, 341, 34))
        self.qleApiKey.setObjectName("qleApiKey")
        
        self.labelApiKey = QtWidgets.QLabel(self.centralwidget)
        self.labelApiKey.setGeometry(QtCore.QRect(300, 290, 341, 34))
        self.labelApiKey.setText("")
        self.labelApiKey.setObjectName("labelApiKey")
        
        
        
        
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 34))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.actionLicense = QtWidgets.QAction(window)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout_pyTranscriber = QtWidgets.QAction(window)
        self.actionAbout_pyTranscriber.setObjectName("actionAbout_pyTranscriber")
        self.menuAbout.addAction(self.actionLicense)
        self.menuAbout.addAction(self.actionAbout_pyTranscriber)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Course Translator - v1.0 - 10/02/2021"))
        self.bSelectMedia.setText(_translate("window", "Selecciona Archivos"))
        self.bConvert.setText(_translate("window", "Generar Subtitulos"))
        self.bOpenOutputFolder.setText(_translate("window", "Abrir Carpeta Destino"))
        self.bSelectOutputFolder.setText(_translate("window", "Carpeta Destino"))
        self.groupBox.setTitle(_translate("window", "Listado de Archivos"))
        self.bRemoveFile.setText(_translate("window", "Eliminar Archivo(s)"))
        self.bCancel.setText(_translate("window", "Cancelar"))
        self.chbxOpenOutputFilesAuto.setText(_translate("window", "Al terminar abrir Carpeta Destino"))
        self.labelSelectLang.setText(_translate("window", "Idioma Audio:"))
        self.labelSelectLangTranslate.setText(_translate("window", "Idioma Traducción:"))
        self.labelApiKey.setText(_translate("window", "Google Api Key (Obligatoria)"))
        
        self.menuAbout.setTitle(_translate("window", "Información"))
        self.actionLicense.setText(_translate("window", "&Licencia"))
        self.actionAbout_pyTranscriber.setText(_translate("window", "Sobre CourseTranslator"))
