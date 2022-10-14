# This Python file uses the following encoding: utf-8
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6 import QtGui

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_main_qwidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

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
        self.ui.boton_siguiente_tag5.clicked.connect(self.boton_event_siguiente_tag5)
        self.ui.boton_calcular_tag5.clicked.connect(self.boton_event_calcular_tag5)
        # imagenes para los layout
        self.label_image = list()
        for index in range(0, cantidad_imagenes):
            self.label_image.append(QLabel())
        
        self.plot_layout = list()
        self.plot_layout.append(self.ui.histograma_antes_layout)
        self.plot_layout.append(self.ui.histograma_despues_layout)
        self.ui.antes_calibracion_layout.addWidget(self.label_image[0],
                                  1,
                                  1)
        self.ui.despues_calibracion_layout.addWidget(self.label_image[1],
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
    def Show_frames(self, frame, index_layout, scalar = True, bit_image=False):      
        try:
            bytesPerLine = frame.shape[1] * frame.shape[2]
        except AttributeError as error_list:
            print(error_list)
        else:
            if not(bit_image):
                ima = QtGui.QImage(frame,
                                   frame.shape[1],
                                   frame.shape[0],
                                   bytesPerLine,
                                   QtGui.QImage.Format_RGB888)
            else:
                ima = QtGui.QImage(frame,
                                   frame.shape[1],
                                   frame.shape[0],
                                   bytesPerLine,
                                   QtGui.QImage.Format_RGB32)
            imagen = QtGui.QPixmap.fromImage(ima)
            if scalar:
                imagen = imagen.scaled(469, 469, Qt.KeepAspectRatio)

            self.label_image[index_layout].setPixmap(imagen)

    def Show_frames_(self, frame, index_layout, scalar = True, bit_image=False):      
        try:
            bytesPerLine = frame.shape[1] * frame.shape[2]
        except AttributeError as error_list:
            print(error_list)
        else:

            imagen = QtGui.QPixmap.fromImage(frame)


            self.label_image[index_layout].setPixmap(imagen)
            
    def show_plot(self, canvas_plot, index_layout):
        self.plot_layout[index_layout].addWidget(canvas_plot,
                                                 1,
                                                 1)

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

    def boton_event_siguiente_tag5(self):
        pass

    def boton_event_calcular_tag5(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget(8)
    widget.show()
    sys.exit(app.exec())


