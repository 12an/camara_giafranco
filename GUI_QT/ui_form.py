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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

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
        self.boton_siguiente_tag1 = QPushButton(self.tabs_calibracion)
        self.boton_siguiente_tag1.setObjectName(u"boton_siguiente_tag1")
        self.boton_siguiente_tag1.setGeometry(QRect(-10, 533, 811, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.boton_siguiente_tag1.setFont(font)
        self.gridLayoutWidget = QWidget(self.tabs_calibracion)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 391, 531))
        self.antes_calibracion_layout = QGridLayout(self.gridLayoutWidget)
        self.antes_calibracion_layout.setObjectName(u"antes_calibracion_layout")
        self.antes_calibracion_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.antes_calibracion_layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_2 = QWidget(self.tabs_calibracion)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(410, 0, 391, 531))
        self.despues_calibracion_layout = QGridLayout(self.gridLayoutWidget_2)
        self.despues_calibracion_layout.setObjectName(u"despues_calibracion_layout")
        self.despues_calibracion_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.despues_calibracion_layout.setContentsMargins(0, 0, 0, 0)
        self.taps_.addTab(self.tabs_calibracion, "")
        self.tab_histogramas = QWidget()
        self.tab_histogramas.setObjectName(u"tab_histogramas")
        self.boton_siguiente_tag2 = QPushButton(self.tab_histogramas)
        self.boton_siguiente_tag2.setObjectName(u"boton_siguiente_tag2")
        self.boton_siguiente_tag2.setGeometry(QRect(-10, 530, 811, 41))
        self.boton_siguiente_tag2.setFont(font)
        self.gridLayoutWidget_3 = QWidget(self.tab_histogramas)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 391, 261))
        self.histograma_antes_layout = QGridLayout(self.gridLayoutWidget_3)
        self.histograma_antes_layout.setObjectName(u"histograma_antes_layout")
        self.histograma_antes_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.histograma_antes_layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_4 = QWidget(self.tab_histogramas)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(400, 0, 401, 261))
        self.histograma_despues_layout = QGridLayout(self.gridLayoutWidget_4)
        self.histograma_despues_layout.setObjectName(u"histograma_despues_layout")
        self.histograma_despues_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.histograma_despues_layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_5 = QWidget(self.tab_histogramas)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 270, 391, 261))
        self.foto_antes_layout = QGridLayout(self.gridLayoutWidget_5)
        self.foto_antes_layout.setObjectName(u"foto_antes_layout")
        self.foto_antes_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.foto_antes_layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_6 = QWidget(self.tab_histogramas)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(400, 270, 401, 261))
        self.foto_despues_layout = QGridLayout(self.gridLayoutWidget_6)
        self.foto_despues_layout.setObjectName(u"foto_despues_layout")
        self.foto_despues_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.foto_despues_layout.setContentsMargins(0, 0, 0, 0)
        self.taps_.addTab(self.tab_histogramas, "")
        self.tab_divicion = QWidget()
        self.tab_divicion.setObjectName(u"tab_divicion")
        self.boton_siguiente_tag3 = QPushButton(self.tab_divicion)
        self.boton_siguiente_tag3.setObjectName(u"boton_siguiente_tag3")
        self.boton_siguiente_tag3.setGeometry(QRect(-10, 530, 811, 41))
        self.boton_siguiente_tag3.setFont(font)
        self.gridLayoutWidget_7 = QWidget(self.tab_divicion)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 0, 801, 531))
        self.divicion_grid_layout = QGridLayout(self.gridLayoutWidget_7)
        self.divicion_grid_layout.setObjectName(u"divicion_grid_layout")
        self.divicion_grid_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.divicion_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.taps_.addTab(self.tab_divicion, "")
        self.tab_resultados = QWidget()
        self.tab_resultados.setObjectName(u"tab_resultados")
        self.boton_siguiente_tag4 = QPushButton(self.tab_resultados)
        self.boton_siguiente_tag4.setObjectName(u"boton_siguiente_tag4")
        self.boton_siguiente_tag4.setGeometry(QRect(0, 530, 401, 41))
        self.boton_siguiente_tag4.setFont(font)
        self.boton_agregar_tag4 = QPushButton(self.tab_resultados)
        self.boton_agregar_tag4.setObjectName(u"boton_agregar_tag4")
        self.boton_agregar_tag4.setGeometry(QRect(400, 530, 401, 41))
        self.boton_agregar_tag4.setFont(font)
        self.gridLayoutWidget_8 = QWidget(self.tab_resultados)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(-1, -1, 801, 531))
        self.resultados_layout = QGridLayout(self.gridLayoutWidget_8)
        self.resultados_layout.setObjectName(u"resultados_layout")
        self.resultados_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.resultados_layout.setContentsMargins(0, 0, 0, 0)
        self.taps_.addTab(self.tab_resultados, "")
        self.configurar_camera = QWidget()
        self.configurar_camera.setObjectName(u"configurar_camera")
        self.gridLayoutWidget_9 = QWidget(self.configurar_camera)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 0, 381, 521))
        self.config_camera_layout_tag5 = QGridLayout(self.gridLayoutWidget_9)
        self.config_camera_layout_tag5.setObjectName(u"config_camera_layout_tag5")
        self.config_camera_layout_tag5.setSizeConstraint(QLayout.SetFixedSize)
        self.config_camera_layout_tag5.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_10 = QWidget(self.configurar_camera)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(400, 0, 401, 521))
        self.config_camera_result_layout_tag5 = QGridLayout(self.gridLayoutWidget_10)
        self.config_camera_result_layout_tag5.setObjectName(u"config_camera_result_layout_tag5")
        self.config_camera_result_layout_tag5.setSizeConstraint(QLayout.SetFixedSize)
        self.config_camera_result_layout_tag5.setContentsMargins(0, 0, 0, 0)
        self.boton_siguiente_tag3_2 = QPushButton(self.configurar_camera)
        self.boton_siguiente_tag3_2.setObjectName(u"boton_siguiente_tag3_2")
        self.boton_siguiente_tag3_2.setGeometry(QRect(-10, 530, 811, 41))
        self.boton_siguiente_tag3_2.setFont(font)
        self.taps_.addTab(self.configurar_camera, "")

        self.retranslateUi(main_qwidget)

        self.taps_.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_qwidget)
    # setupUi

    def retranslateUi(self, main_qwidget):
        main_qwidget.setWindowTitle(QCoreApplication.translate("main_qwidget", u"Calidad Prado", None))
        self.boton_siguiente_tag1.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tabs_calibracion), QCoreApplication.translate("main_qwidget", u"Calibracion", None))
        self.boton_siguiente_tag2.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_histogramas), QCoreApplication.translate("main_qwidget", u"Histogramas", None))
        self.boton_siguiente_tag3.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_divicion), QCoreApplication.translate("main_qwidget", u"Divicion", None))
        self.boton_siguiente_tag4.setText(QCoreApplication.translate("main_qwidget", u"Siguiente", None))
        self.boton_agregar_tag4.setText(QCoreApplication.translate("main_qwidget", u"Agregar", None))
        self.taps_.setTabText(self.taps_.indexOf(self.tab_resultados), QCoreApplication.translate("main_qwidget", u"Resultados", None))
        self.boton_siguiente_tag3_2.setText(QCoreApplication.translate("main_qwidget", u"Capturar", None))
        self.taps_.setTabText(self.taps_.indexOf(self.configurar_camera), QCoreApplication.translate("main_qwidget", u"Configurar Camara", None))
    # retranslateUi

