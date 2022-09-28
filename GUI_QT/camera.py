# This Python file uses the following encoding: utf-8

import cv2
import numpy as np
import glob


class Camera:

    def __init__(self, camera_id, *arg, **args):
        print("inicializando Camera ")
        self.camera_id = camera_id
        self.captura = cv2.VideoCapture(self.camera_id)


class CameraResolution(Camera):
    def __init__(self, resolucion, *arg, **args):
        Camera.__init__(self, *arg, **args)
        self.resolucion_frames = resolucion
    def get_resolution(self):
        try:
            self.width = int(self.captura.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = int(self.captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print("{0} X {1} es".format(self.width, self.height) +
                  "la resolucio actual camera #{0}".format(self.camera_id))
        except cv2.error as error:
            print("Error con la camera " + str(error))

    def set_resolution(self, default):
        for frame_cameras in self.captura:
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
            ret, frame1 = self.captura.read(self.camera_ID)
            return cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)

class CameraIntrisicsValue():
    def __init__(self, sensor_size, CHECKERBOARD,
                 camera_id, *arg, **args):
        self.sensor_size = sensor_size
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
        # charging images
        self.images = glob.glob('./calibracion/camera_' +
                                str(camera_id) +
                                '/*.jpg')
        frame,*_ = *self.images
        self.shape = cv2.cvtColor(cv2.imread(frame),
                                  cv2.COLOR_BGR2GRAY
                                  ).shape[::-1]

    def extracting_corners(self, show):
        for fname in self.images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
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
                img = cv2.drawChessboardCorners(img, 
                                                self.CHECKERBOARD, 
                                                corners2, 
                                                ret)
            if show:
                cv2.imshow('img',img)
                cv2.waitKey(0)

    def get_intrisic_parameters(self):
        """
        Performing camera calibration by 
        passing the value of known 3D points (objpoints)
        and corresponding pixel coordinates of the 
        detected corners (imgpoints)
        """
        *self.intrisics = cv2.calibrateCamera(self.objpoints, 
                                              self.imgpoints, 
                                              self.shape,
                                              None,
                                              None)