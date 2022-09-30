# This Python file uses the following encoding: utf-8
import os
import sys
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from DatosControl import DatosControl
from widget import Widget
from SerComunicacion import SteperDevice
from Camera import FrameCamera

class ControlModel(SteperDevice,
                  DatosControl, Widget):

    def __init__(self, *arg, **args):
        print("inicializando Controlador ")
        self.current_dir = os.getcwd()
        self.sensor_size = [3.55,5.88]
        self.resolucion = [1920, 1080]
        self.parametros_camera = {"numero_cameras" : 1,
                                  "sensor_size" : self.sensor_size,
                                  "resolucion":self.resolucion}
        self.camera = FrameCamera(*[],
                                  **self.parametros_camera)
        # configurando resolucion
        self.camera.set_resolution(False)
        DatosControl.__init__(self, "fotos", self.current_dir)
        # creando timer recurrente.
        # actualizar fotos camera
        self.timer_actualizar_fotos = QTimer()
        self.timer_actualizar_fotos.timeout.connect(self.update_imagen_camera)
        self.timer_actualizar_fotos.start(90)  
        # guardar fotos
        self.timer_guardar_fotos = QTimer()
        self.timer_guardar_fotos.timeout.connect(self.thread_guardar_fotos)
        self.timer_guardar_fotos.start(1/4)
        # cargando app
        Widget.__init__(self,
                        *[],
                        **{"cantidad_imagenes":10, "parent" : None})

    def update_imagen_camera(self):
        self.frames = self.camera.frame()
        self.Show_frames(self.frames, 8)

    def thread_guardar_fotos(self):
        if (self.boton_capturar_tag5):
            self.save_fotos(self.frames, self.agulo)
            self.boton_capturar_tag5 = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejecucion = ControlModel()
    ejecucion.show()
    sys.exit(app.exec_())