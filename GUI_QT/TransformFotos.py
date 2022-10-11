# This Python file uses the following encoding: utf-8
import cv2
import numpy as np

class LuminosidadFotos:
    def __init__(self, foto):
        self.foto = foto
        self.get_foto_YUV()
        self.histograma_Luminosidad()
        self.histograma_luminosidad_acumulado()
        self.normalizacion_Luminosidad()
        self.get_RGB_from_YUV()
              
    def get_foto_YUV(self):
        self.img_yuv = cv2.cvtColor(self.foto, cv2.COLOR_BGR2YUV)

    def histograma_Luminosidad(self):
        self.histo_bruto = np.zeros(256, int)
        self.histo_y = np.zeros(256, int)
        for i in range(0, self.foto.shape[0]):
            for j in range(0, self.foto.shape[1]):
                self.histo_y[self.img_yuv[:,:,0][i,j]] = self.histo_y[self.img_yuv[:,:,0][i,j]] + 1
                self.histo_bruto[self.foto[i,j]] = self.histo_bruto[self.foto[i,j]] + 1
  
    def histograma_luminosidad_acumulado(self):
        self.histo_y_ac = np.zeros(256, int)
        #preparando vector
        self.histo_y_ac[0] = self.histo_y[0]
        for i in range(1, 256):
            self.histo_y_ac[i] = self.histo_y[i] + self.histo_y_ac[i - 1]

    def normalizacion_Luminosidad(self):
        numero_pixeles = self.img_yuv[:,:,0].size
        histograma_normalizado = self.histo_y_ac / numero_pixeles * 220
        for i in range(0, self.foto.shape[0]):
            for j in range(0, self.foto.shape[1]):
                self.img_yuv[:,:,0][i,j] = histograma_normalizado[self.img_yuv[:,:,0][i,j]]

	
    def get_RGB_from_YUV(self):
        # convert the YUV image back to RGB format
        self.foto_normalizada = cv2.cvtColor(self.img_yuv, cv2.COLOR_YUV2BGR)

class FiltroFotos:
    def __init__(self, foto_normalizada):
        self.foto_normalizada = foto_normalizada
        self.bilateral_filtro()
        self.histograma_bilateral()

    def bilateral_filtro(self):
        self.foto_norm_bilate = cv2.bilateralFilter(self.foto_normalizada,30,80,80)

    def histograma_bilateral(self):
        self.histo_norma_bilater = np.zeros(256, int)
        for i in range(0, self.foto_normalizada.shape[0]):
            for j in range(0, self.foto_normalizada.shape[1]):
                self.histo_norma_bilater[self.foto_normalizada[i,j]] = self.histo_norma_bilater[self.foto_normalizada[i,j]] + 1

class CalibrateFoto():
    def __init__(self, foto,
                 mtx,
                 dist,
                 R,
                 T,
                 width,
                 height,
                 altura):
                 #origen_coordenada,
                 #posicion_coordenada,
                 #rotacion_dron):
        self.mtx = mtx
        self.dist = dist
        self.R = R
        self.T = T
        self.rio_foto = list()
        self.foto_tratada = foto
        self.width = width
        self.height = height
        self.z = altura
        self.calibrate()
        #self.translation_vector = 
        #self.rotacion = rotacion_dron
        #self.foto_3d_from_2d = 
        #self.foto_word_coordinates = 
    def calibrate(self):
        self.newcameramtx, self.roi = cv2.getOptimalNewCameraMatrix(self.mtx,
                                                          self.dist,
                                                          (self.width , self.height ),
                                                          1,
                                                          (self.width , self.height ))
        mapx, mapy = cv2.initUndistortRectifyMap(self.mtx, self.dist, None, self.newcameramtx, (self.width , self.height ), 5)
        dst1 = cv2.remap(self.foto_tratada, mapx, mapy, cv2.INTER_LINEAR)
        self.foto_calibrada = cv2.cvtColor(dst1, cv2.COLOR_RGB2BGR)
        # crop the image
        x, y, w, h = self.roi
        self.foto_calibrada_recortada = self.foto_calibrada[y:y+h, x:x+w]
        
    def get_foto_3d_from_2d(self):
        # z es constante a la altura de la imagen
        for i in range(0, self.width):
            for j in range(0, self.height):
                vector_pixel_2d_posicion = np.matrix([[i], [j], [self.z]])
                self.foto_3d_from_2d = self.newcameramtx.I * vector_pixel_2d_posicion
        pass
    def get_word_coordinate_foto(self):
        pass