# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from DataModel import DatosControl
from widget import Widget, MplCanvas
from camera import CameraIntrisicsValue
import cv2

class ControlModel(DatosControl, Widget):

    def __init__(self, *arg, **args):
        print("inicializando Controlador ")
        self.index_tag1 = 0
        self.index_tag2 = 0
        self.index_tag3 = 0
        self.index_tag4 = 0
        self.index_tag5 = 0

        self.current_dir = os.path.abspath(os.path.dirname( __file__ ))
        self.sensor_size = [3.55,5.88]
        self.resolucion = [1920, 1080]
        # cargando app
        Widget.__init__(self,
                        *[],
                        **{"cantidad_imagenes":10})
        self.parametros_calibracion = {"numero_cameras" : 1,
                                  "sensor_size" : self.sensor_size,
                                  "camera_id" : 0,
                                  "CHECKERBOARD" : (7,10)
                                  }
        self.camera_instrisics_ = CameraIntrisicsValue(*[],
                                                       **self.parametros_calibracion
                                                       )

        #datos
        DatosControl.__init__(self,*[],
                                      **{"path" : self.current_dir,
                                         "carpeta_fotos_analisis" : "fotos_analisis",
                                         "carpeta_fotos_chesspattern" : "fotos_chess_pattern",
                                         "carpeta_gui" : "GUI_QT",
                                         "carpeta_data" : "data",
                                         "instriscic_pkl" : r"\registed_data_instricic.pkl"
                                         }
                             )
        # configurando inicio
        self.open_foto_analisis(False)
        self.open_foto_chesspattern(False)

    def boton_event_siguinte_tag1(self):
        if(self.index_tag1<self.total_fotos_analisis):
            foto, foto_calibracion = next(self.imagenes_analisis[self.index_tag1])
            self.Show_frames(foto, 0)
            self.Show_frames(foto_calibracion, 1)
            self.index_tag1 += 1

    def boton_event_siguinte_tag2(self):
        if(self.index_tag2<self.total_fotos_analisis):
            foto, foto_norm, histograma_plot, histograma_norma_bilat_plot  = next(self.imagenes_analisis[self.index_tag2])
            self.Show_frames(foto, 4)
            self.Show_frames(foto_norm, 5)
            self.show_plot(histograma_plot, 0)
            self.show_plot(histograma_norma_bilat_plot, 1)
            self.index_tag2 += 1

    def boton_event_siguinte_tag3(self):
        if(self.index_tag3<self.total_fotos_analisis):
            foto = next(self.imagenes_analisis[self.index_tag3])
            self.Show_frames(foto, 6)
            self.index_tag3 += 1

    def boton_event_siguinte_tag4(self):
        if(self.index_tag4<self.total_fotos_analisis):
            foto = next(self.imagenes_analisis[self.index_tag4])
            self.Show_frames(foto, 7)
            self.index_tag4 += 1

    def boton_event_agregar_tag4(self):
        pass

    def boton_event_siguiente_tag5(self):
        print("aaaa")
        if(self.index_tag5<self.total_fotos_chesspattern ):
            print("aaafa")
            foto = self.imagenes_chesspattern[self.index_tag5].foto
            #cv2.imshow("ddd",foto)
            draw_foto = self.camera_instrisics_.extracting_corners(foto)
            #cv2.imshow("dsa",draw_foto)
            self.Show_frames(foto, 8)
            self.Show_frames(draw_foto, 9)
            self.index_tag5 += 1

    def boton_event_calcular_tag5(self):
        if(self.index_tag5>0):
            self.camera_instriscic = self.camera_instrisics_.get_intrisic_parameters()
	
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejecucion = ControlModel()
    ejecucion.show()
    sys.exit(app.exec_())
