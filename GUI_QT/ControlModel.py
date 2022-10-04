# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from DataModel import DatosControl
from widget import Widget
from camera import FrameCamera, CameraIntrisicsValue


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
        self.parametros_camera = {"numero_cameras" : 1,
                                  "sensor_size" : self.sensor_size,
                                  "resolucion" : self.resolucion,
                                  "camera_id" : 0
                                  }
        self.parametros_calibracion = {"numero_cameras" : 1,
                                  "sensor_size" : self.sensor_size,
                                  "camera_id" : 0,
                                  "CHECKERBOARD" : (7,10)
                                  }
        self.camera = FrameCamera(*[],
                                  **self.parametros_camera)
        self.camera_instrisics_ = CameraIntrisicsValue(*[],
                                                       **self.parametros_calibracion
                                                       )

        #datos
        DatosControl.__init__(self,*[],
                                      **{"path" : self.current_dir,
                                         "carpeta_fotos_analisis" : "fotos_analisis",
                                         "carpeta_fotos_chesspattern" : "fotos_chess_pattern",
                                         "carpeta_gui" : "GUI_QT"
                                         }
                             )
        # configurando inicio
        self.camera.set_resolution(False)
        self.open_foto_analisis(False)
        # actualizar fotos camera
        self.timer_actualizar_fotos = QTimer()
        self.timer_actualizar_fotos.timeout.connect(self.update_imagen_camera)
        self.timer_actualizar_fotos.start(90)  

    def update_imagen_camera(self):
        self.frame = self.camera.frame()
        self.Show_frames(self.frame, 8)

    def boton_event_siguinte_tag1(self):
        foto, foto_calibracion = next(self.imagenes_analisis[self.index_tag1])
        self.Show_frames(foto, 0)
        self.Show_frames(foto_calibracion, 1)
        self.index_tag1 += 1

    def boton_event_siguinte_tag2(self):
        foto, foto_norm, foto_histo, foto_norm_histo  = next(self.imagenes_analisis[self.index_tag2])
        self.Show_frames(foto, 2)
        self.Show_frames(foto_norm, 3)
        self.Show_frames(foto_histo, 4)
        self.Show_frames(foto_histo, 5)
        self.index_tag2 += 1

    def boton_event_siguinte_tag3(self):
        foto = next(self.imagenes_analisis[self.index_tag3])
        self.Show_frames(foto, 6)
        self.index_tag3 += 1

    def boton_event_siguinte_tag4(self):
        foto = next(self.imagenes_analisis[self.index_tag4])
        self.Show_frames(foto, 7)
        self.index_tag4 += 1

    def boton_event_agregar_tag4(self):
        pass

    def boton_capturar_tag5(self):
        self.live_chesspattern_foto(self.frame, self.index_tag5)
        self.index_tag5 += 1
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejecucion = ControlModel()
    ejecucion.show()
    sys.exit(app.exec_())
