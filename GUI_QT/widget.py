# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6 import QtGui

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_main_qwidget

class Widget(QWidget):
    def __init__(self, cantidad_imagenes, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_qwidget()
        self.ui.setupUi(self)
        # eventos
        self.ui.boton_siguiente_tag1.clicked.connect(self.boton_event_siguinte_tag1)
        self.ui.boton_siguiente_tag2.clicked.connect(self.boton_event_siguinte_tag2)
        self.ui.boton_siguiente_tag3.clicked.connect(self.boton_event_siguinte_tag3)
        self.ui.boton_siguiente_tag4.clicked.connect(self.boton_event_siguinte_tag4)
        self.ui.boton_agregar_tag4.clicked.connect(self.boton_event_agregar_tag4)
        # imagenes para los layout
        self.label_image = list()
        for index in range(0, cantidad_imagenes):
            self.label_image.append(QLabel())
            
        self.ui.antes_calibracion_layout.addWidget(self.label_image[0],
                                  1,
                                  1)
        self.ui.despues_calibracion_layout.addWidget(self.label_image[1],
                                    1,
                                    1)
        self.ui.histograma_antes_layout.addWidget(self.label_image[2],
                                    1,
                                    1)  
        self.ui.histograma_despues_layout.addWidget(self.label_image[3],
                                    1,
                                    1) 
        self.ui.foto_antes_layout.addWidget(self.label_image[4],
                                    1,
                                    1) 
        self.ui.foto_despues_layout.addWidget(self.label_image[5],
                                    1,
                                    1) 
        self.ui.divicion_grid_layout.addWidget(self.label_image[6],
                                    1,
                                    1) 
        self.ui.resultados_layout.addWidget(self.label_image[7],
                                    1,
                                    1) 
        self.ui.config_camera_layout_tag5.addWidget(self.label_image[8],
                                    1,
                                    1) 
        self.ui.config_camera_result_layout_tag5.addWidget(self.label_image[9],
                                    1,
                                    1)
    def Show_frames(self, frame, index_layout):      
        try:
            bytesPerLine = frame.shape[1] * frame.shape[2]
        except AttributeError as error_list:
            print(error_list)
        else:
            ima = QtGui.QImage(frame,
                               frame.shape[1],
                               frame.shape[0],
                               bytesPerLine,
                               QtGui.QImage.Format_RGB888)
            imagen = QtGui.QPixmap.fromImage(ima)
            imagen_scalada = imagen.scaled(469, 469, Qt.KeepAspectRatio)
            self.label_image[index_layout].setPixmap(imagen_scalada)


    def boton_event_siguinte_tag1(self):
        pass

    def boton_event_siguinte_tag2(self):
        pass

    def boton_event_siguinte_tag3(self):
        pass

    def boton_event_siguinte_tag4(self):
        pass

    def boton_event_agregar_tag4(self):
        pass

    def boton_capturar_tag5(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget(8)
    widget.show()
    sys.exit(app.exec())


