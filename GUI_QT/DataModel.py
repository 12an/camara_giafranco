# This Python file uses the following encoding: utf-8
import os
from cv2 import imwrite, imread
import glob
import TransformFotos


class foto_transform_data(TransformFotos):
    def __init__(self, foto, id_foto, coordenadas, altura):
        self.coordenadas = coordenadas
        self.id_foto = id_foto
        self.foto = foto
        self.area_color = dict()

    def __iter__(self):
        if self.index<4:
            if self.index==0:
                yield self.foto, self.calibracion()
            if self.index==1:
                yield self.histogram()
            if self.index==2:
                yield self.divicion()
            if self.index==3:
                yield self.mask_final_resultado()
    def reset_index(self):
        self.index = 0

class foto_chesspattern_data():
    shape = [0, 0, 0]
    total_fotos = 0
    def __init__(self, id_foto):
        self.id_foto = id_foto
        self.agregada = True

    #verificamos ( de forma sencilla) que todas las fotas tengan el m,ismio tama'o
    def save(self, cls, foto):
        if(cls.total_fotos==0):
            cls.shape = foto.shape
        else:
            if(foto.shape != cls.shape):
                self.agregada = False
            else:
                self.agregada = True
        cls.total_fotos += 1
        self.foto = foto

class DatosControl():
    def __init__(self, path, carpeta_fotos_analisis, carpeta_fotos_chesspattern):
        print("inicializando DatosControl ")
        self.path_directory = path
        self.imagenes_analisis = list()
        self.imagenes_chesspattern = list()       
        self.carpeta_fotos_analisis = carpeta_fotos_analisis
        self.carpeta_fotos_chesspattern = carpeta_fotos_chesspattern

    def save_(func):
        def inner(*arg,**args):
            imwrite(func(*arg,**args))

    def open_(self, func):
        def inner(*arg,**args):
            # charging images
            path, tipo_imagen = func(*arg,**args)
            for name in glob.iglob(path + "/*.png"):
                imagen = imread(path, "/" + name)
                id_imagen = name[0:name.find("_")]
                if(tipo_imagen==1):
                    altura_imagen = int(name[name.find("_") + 1: name.find("-")])
                    coordenada_mix = name[name.find("-") + 1: name.find(".")]
                    coordenada_imagen = {"x":coordenada_mix[coordenada_mix.find("x") + 1 :coordenada_mix.find("y")],
                                         "y":coordenada_mix[coordenada_mix.find("x") + 1 :coordenada_mix.find("y")]}
                    self.imagenes_analisis.append(foto_transform_data(imagen,
                                                                      id_imagen,
                                                                      coordenada_imagen,
                                                                      altura_imagen
                                                                      )
                                                  )
                if(tipo_imagen==2):
                    self.imagenes_chesspattern.append(
                        foto_chesspattern_data(id_imagen).save(imagen) 
                                                    )

    @open_
    def open_foto_analisis(self, path = False):
        if isinstance(path, bool()):
            return os.path.join(self.path_directory, self.carpeta_fotos_analisis), 1
        else:
            return path, 1

    @open_
    def open_foto_chesspattern(self, path = False):
        if isinstance(path, bool()):
            return os.path.join(self.path_directory, self.carpeta_fotos_chesspattern), 2
        else:
            return path, 2

    def get_registed_camera_instricic(self, path = False):
        pass
    def save_registed_camera_instricic(self, ):
        pass

    #guarda foto con path nombre, altura y carpeta en especifico
    @save_
    def save_fotos_name(self, foto, altura, name, carpeta, path = False):
        if isinstance(path, bool()):
            return os.path.join(self.path_directory, self.carpeta, name + "_" + str(altura) + ".png"), foto
        else:
            return os.path.join(path, self.carpeta, name + "_" + str(altura) + ".png"), foto


