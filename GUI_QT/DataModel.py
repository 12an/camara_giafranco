# This Python file uses the following encoding: utf-8
import os
import glob
from cv2 import imwrite, imread, cvtColor, COLOR_RGB2BGR
import pickle
from  TransformFotos import LuminosidadFotos, FiltroFotos
from widget import MplCanvas

class DataAnalisis:
    def __init__(self):
        self.area_total = 0
        self.area_color = list()
class Foto:
    def __init__(self, foto, id_foto, coordenadas, altura):
        self.coordenadas = coordenadas
        self.id_foto = id_foto
        self.area_color = dict()
        self.foto = foto

class FotoTransformData(Foto, LuminosidadFotos, FiltroFotos):

    def __init__(self, *arg,**args):
        Foto.__init__(self, *arg,**args)
        LuminosidadFotos.__init__(self, self.foto)
        self.index = 0
        FiltroFotos.__init__(self, self.foto_normalizada)
        self.histograma_plot = MplCanvas(self, width=5, height=4, dpi=100)
        self.histograma_norma_bilat_plot = MplCanvas(self, width=5, height=4, dpi=100)
        self.histograma_plot.axes.plot(self.histo_bruto)
        self.histograma_norma_bilat_plot.axes.plot(self.histo_norma_bilater)        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index<4:
            if self.index==0:
                self.index += 1
                return self.foto, self.foto
            if self.index==1:
                self.index += 1
                return (self.foto,
                        self.foto_normalizada,
                        self.histograma_plot,
                        self.histograma_norma_bilat_plot)
            if self.index==2:
                self.index += 1
                return self.foto,
            if self.index==3:
                self.index += 1
                return self.foto,
        
    def reset_index(self):
        self.index = 0


class FotoChesspatternData():
    total_fotos = 0
    def __init__(self, id_foto, foto):
        self.id_foto = id_foto
        self.agregada = False
        self.foto = foto
        self.__class__.total_fotos += 1

class DatosControl():

    def __init__(self, path,
                 carpeta_fotos_analisis,
                 carpeta_fotos_chesspattern,
                 carpeta_gui,
                 instriscic_pkl,
                 carpeta_data
                  ):
        print("inicializando DatosControl ")
        self.path_directory = path
        self.imagenes_analisis = list()
        self.imagenes_chesspattern = list()       
        self.carpeta_fotos_analisis = carpeta_fotos_analisis
        self.carpeta_fotos_chesspattern = carpeta_fotos_chesspattern
        self.instriscic_pkl = instriscic_pkl
        self.carpeta_data = carpeta_data
        self.carpeta_gui = carpeta_gui
        self.total_fotos_analisis = 0
        self.total_fotos_chesspattern = 0
        self.camera_instriscic = list()
        self.read_instricic_camera()
    def save_(func):
        def inner(self, *arg,**args):
            imwrite(func(self, *arg,**args))
        return inner

    def open_(func):
        def inner(self, *arg,**args):

            # charging images
            path, tipo_imagen = func(self, *arg,**args)
            for path_name_foto in glob.iglob(path + "\*.jpg"):
                name_foto = path_name_foto[len(path) + 1 : ]
                imagen = cvtColor(imread(path_name_foto), COLOR_RGB2BGR)
                id_imagen = name_foto[0:name_foto.find("_")]
                if(tipo_imagen==1):
                    altura_imagen = int(name_foto[name_foto.find("_") + 1: name_foto.find("-")])
                    coordenada_mix = name_foto[name_foto.find("-") + 1: name_foto.find(".")]
                    coordenada_imagen = {"x":coordenada_mix[coordenada_mix.find("x") + 1 :coordenada_mix.find("y")],
                                         "y":coordenada_mix[coordenada_mix.find("x") + 1 :coordenada_mix.find("y")]}
                    self.imagenes_analisis.append(FotoTransformData(imagen,
                                                                      id_imagen,
                                                                      coordenada_imagen,
                                                                      altura_imagen
                                                                      )
                                                  )
                    self.total_fotos_analisis += 1
                if(tipo_imagen==2):
                    print("aa1daa")
                    self.imagenes_chesspattern.append(
                        FotoChesspatternData(id_imagen, imagen) 
                                                    )
                    self.total_fotos_chesspattern += 1
        return inner

    @open_
    def open_foto_analisis(self, path = False):
        print(self.path_directory)
        if isinstance(path, bool):
            path = self.path_directory
            return path.replace(self.carpeta_gui, self.carpeta_fotos_analisis), 1
        else:
            return path, 1

    @open_
    def open_foto_chesspattern(self, path = False):
        if isinstance(path, bool):
            path = self.path_directory
            return path.replace(self.carpeta_gui, self.carpeta_fotos_chesspattern), 2
        else:
            return path, 2
    
    def get_registed_camera_instricic(self, path = False):
        pass
    def save_registed_camera_instricic(self, ):
        pass

    #guarda foto con path nombre, altura y carpeta en especifico
    @save_
    def save_fotos_name(self, foto, altura, name, carpeta, path = False):
        if isinstance(path, bool):
            return os.path.join(self.path_directory, self.carpeta, name + "_" + str(altura) + ".png"), foto
        else:
            return os.path.join(path, self.carpeta, name + "_" + str(altura) + ".png"), foto

    def save_instricic_camera(self):
        with open(self.path_directory.replace(self.carpeta_gui, self.carpeta_data) + self.instriscic_pkl , "wb") as saving:
            pickle.dump(self.camera_instriscic, saving)
        
    def read_instricic_camera(self):
        with open(self.path_directory.replace(self.carpeta_gui, self.carpeta_data) + self.instriscic_pkl , "rb") as reading:
            try:
                self.camera_instriscic = pickle.load(reading)
            except EOFError as nothing_in_file:
                print("there is nothing in the file")
                print(nothing_in_file)
