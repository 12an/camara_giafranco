# This Python file uses the following encoding: utf-8
import os
from cv2 import imwrite, imread
import glob


class DatosControl:
    def __init__(self, path):
        self.path_directory = path
        self.imagenes = list()
        self.alturas = list()
        print("inicializando DatosControl ")

    def save_(func):
        def inner(*arg,**args):
            imwrite(func(*arg,**args))
            
        
    def open_foto(self, path = False):
        # charging images
        for name in glob.iglob('./' + self.carpeta + '/*.png'):
            self.imagenes.append(imread(self.path_directory + 
                                        "/" + 
                                        self.carpeta +
                                        name))
            self.alturas.append(name[name.find("_") + 1: len(name)])
    def get_registed_camera_instricic(self, path = False):
        pass
    def save_registed_camera_instricic(self, ):
        pass
    #guarda foto con path nombre, altura y carpeta en especifico
    @save_
    def save_fotos(self, foto, altura, name, carpeta, path = False):
        return os.path.join(self.path_directory, self.carpeta, name + "_" + str(altura) + ".png"), foto
                