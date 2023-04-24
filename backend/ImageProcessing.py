"Bu class görüntü işleme fonksiyonlarını içerir"
import cv2 as cv

class ImageProcessing:
    def __init__(self, img, path=None):
        self.img = img
        self.path = path

    def convert_to_gray(self):
        "Griye çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

    def convert_to_hsv(self):
        "HSVye çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)

    def convert_from_bgr_to_rgb(self):
        "BGRdan RGBye çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)

    def convert_from_rgb_to_bgr(self):
        "RGBden BGRa çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_RGB2BGR)

    def convert_to_luv(self):
        "LUVa çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2LUV)

    def convert_to_hls(self):
        "HLSye çevirme"
        self.img = cv.imread(self.path)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2HLS)