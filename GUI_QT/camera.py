# This Python file uses the following encoding: utf-8

import cv2
import numpy as np


class Camera:

    def __init__(self, camera_id, sensor_size, *arg, **args):
        print("inicializando Camera ")
        self.camera_id = camera_id
        self.captura = cv2.VideoCapture(self.camera_id)
        self.sensor_size = sensor_size


class CameraIntrisicsValue(Camera):
    def __init__(self,
                 CHECKERBOARD,
                 *arg, **args):
        self.CHECKERBOARD = CHECKERBOARD
        self.criteria = (cv2.TERM_CRITERIA_EPS + 
                         cv2.TERM_CRITERIA_MAX_ITER,
                         30,
                         0.001)
        # Creating vector to store vectors of 3D points for each checkerboard image
        self.objpoints = list()
        # Creating vector to store vectors of 2D points for each checkerboard image
        self.imgpoints = list()
        # Defining the world coordinates for 3D points
        self.objp = np.zeros((1,
                              CHECKERBOARD[0] * CHECKERBOARD[1],
                              3), np.float32)
        self.objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 
                                     0:CHECKERBOARD[1]].T.reshape(-1, 2)
        self.prev_img_shape = None
        self.intrisics = list()


    def extracting_corners(self, foto):
        gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
        # Find the chess board corners
        # If desired number of corners are found in the image then ret = true
        ret, corners = cv2.findChessboardCorners(gray,
                                                 self.CHECKERBOARD,
                                                 cv2.CALIB_CB_ADAPTIVE_THRESH + 
                                                 cv2.CALIB_CB_FAST_CHECK + 
                                                 cv2.CALIB_CB_NORMALIZE_IMAGE)
        """
        If desired number of corner are detected,
        we refine the pixel coordinates and display 
        them on the images of checker board
        """
        print(ret)
        if ret == True:
            self.objpoints.append(self.objp)
            # refining pixel coordinates for given 2d points.
            corners2 = cv2.cornerSubPix(gray,
                                        corners, 
                                        (11,11),
                                        (-1,-1), 
                                        self.criteria)
            self.imgpoints.append(corners2)
            # Draw and display the corners
            return cv2.drawChessboardCorners(foto, 
                                            self.CHECKERBOARD, 
                                            corners2, 
                                            ret)

    def get_intrisic_parameters(self):
        """
        Performing camera calibration by 
        passing the value of known 3D points (objpoints)
        and corresponding pixel coordinates of the 
        detected corners (imgpoints)
        """
        self.intrisics = cv2.calibrateCamera(self.objpoints,
                                              self.imgpoints,
                                              self.shape,
                                              None,
                                              None)
class CameraResolution(Camera):
    def __init__(self, resolucion, *arg, **args):
        Camera.__init__(self, *arg, **args)
        self.resolucion_frames = resolucion
        #resolucion defecto
        self.width = 1080
        self.height = 720
    def get_resolution(self):
        try:
            self.width = int(self.captura.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = int(self.captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print("{0} X {1} es".format(self.width, self.height) +
                  "la resolucio actual camera #{0}".format(self.camera_id))
        except cv2.error as error:
            print("Error con la camera " + str(error))

    def set_resolution(self, default):
        if default:
            self.width, self.height = self.resolucion_frames
            self.set_()
        else:
            self.set_()

    def set_(self):
        self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 
                         self.width
                         )
        self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 
                         self.height
                         )

class FrameCamera(CameraResolution):

    def __init__(self, *arg, **args):
        print("inicializando FrameCamera ")
        CameraResolution.__init__(self, *arg, **args)

    def frame(self):
            ret, frame1 = self.captura.read(self.camera_id)
            return cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
