# This Python file uses the following encoding: utf-8
import os
from cv2 import imwrite, imread
import glob


class DatosControl:
    def __init__(self, carpeta, path):
        self.path_directory = path
        self.carpeta
        self.imagenes = list()
        self.alturas = list()
        print("inicializando DatosControl ")

    def save_fotos(self, foto, altura):
        imwrite(os.path.join(self.path_directory, 
                             self.carpeta,
                             self.carpeta
                             + "_" + str(altura)
                             + ".png"),
                foto
                )

    def open_foto(self):
        # charging images
        for name in glob.iglob('./' + self.carpeta + '/*.png'):
            self.imagenes.append(imread(self.path_directory + 
                                        "/" + 
                                        self.carpeta +
                                        name))
            self.alturas.append(name[name.find("_") + 1: len(name)])
            



        