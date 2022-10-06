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
                