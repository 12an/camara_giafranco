# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_main_qwidget(object):
    def setupUi(self, main_qwidget):
        if not main_qwidget.objectName():
            main_qwidget.setObjectName(u"main_qwidget")
        main_qwidget.resize(800, 600)
        self.taps_ = QTabWidget(main_qwidget)
        self.taps_.setObjectName(u"taps_")
        self.taps_.setGeometry(QRect(0, 0, 801, 601))
        self.taps_.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabs_calibracion = QWidget()
        self.tabs_calibracion.setObjectName(u"tabs_calibracion")
        self.pushButton_2 = QPushButton(self.tabs_calibracion)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-10, 533, 811, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.taps_.addTab(self.tabs_calibracion, "")
        self.tab_histogramas = QWidget()
        self.tab_histogramas.setObjectName(u"tab_histogramas")
        self.pushButton_tab_histogramas = QPushButton(self.tab_histogramas)
        self.pushButton_tab_histogramas.setObjectName(u"pushButton_tab_histogramas")
        self.pushButton_tab_histogramas.setGeometry(QRect(-10, 530, 811, 41))
        self.pushButton_tab_histogramas.setFont(font)
        self.taps_.addTab(self.tab_histogramas, "")
        self.tab_divicion = QWidget()
        self.tab_divicion.setObjectName(u"tab_divicion")
        self.pushButton_tab_siguiente = QPushButton(self.tab_divicion)
        self.pushButton_tab_siguiente.setObjectName(u"pushButton_tab_siguiente")
        self.pushButton_tab_siguiente.setGeometry(QRect(-10, 530, 811, 41))
        self.pushButton_tab_siguiente.setFont(font)
        self.taps_.addTab(self.tab_divicion, "")
        self.tab_resultados = QWidget()
        self.tab_resultados.setObjectName(u"tab_resultados")
        self.pushButton_tab_resultados_siguiente = QPushButton(self.tab_resultados)
        self.pushButton_tab_resultados_siguiente.setObjectName(u"pushButton_tab_resultados_siguiente")
        self.pushButton_tab_resultados_siguiente.setGeometry(QRect(0, 530, 401, 41))
        self.pushButton_tab_resultados_siguiente.setFont(font)
        self.pushButton_resultados_sagregar = QPushButton(self.tab_resultados)
        self.pushButton_resultados_sagregar.setObjectName(u"pushButton_resultados_sagregar")
        self.pushButton_resultados_sagregar.setGeometry(QRect(400, 530, 401, 41))
        self.pushButton_resultados_sagregar.setFont(font)
        self.taps_.addTab(self.tab_resultados, "")

        self.retranslateUi(main_qwidget)

        self.taps_.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_qwidget)
    # setupUi

    def retranslateUi(self, main_qwidget):
        main_qwidget.setWindowTitle(QCoreApplication.translate("main_qwidget", u"Calidad Prado", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tabs_calibracion), QCoreApplication.translate("main_qwidget", u"Calibracion", None))
        self.pushButton_tab_histogramas.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_histogramas), QCoreApplication.translate("main_qwidget", u"Histogramas", None))
        self.pushButton_tab_siguiente.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_divicion), QCoreApplication.translate("main_qwidget", u"Divicion", None))
        self.pushButton_tab_resultados_siguiente.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.pushButton_resultados_sagregar.setText(QCoreApplication.translate("main_qwidget", u"Agregar", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_resultados), QCoreApplication.translate("main_qwidget", u"Resultados", None))
    # retranslateUi

