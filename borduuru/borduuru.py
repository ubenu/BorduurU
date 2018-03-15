'''
Created on 14 Mar 2018

@author: schilsm
'''

from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtGui as gui

import pandas as pd, numpy as np, copy as cp
import math

from PIL import Image, ImageFilter

from PyQt5.Qt import QMainWindow

class Main(QMainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        x = Image.open("C:\\users\\schilsm\\Desktop\\test.bmp") # load an image from the hard drive
        ax = np.array(x)
        print(ax.shape)
        print(ax[:,:,0])
        print(np.unique(ax))
        
#         original.show() # display both images
#         blurred.show()    


if __name__ == '__main__':
    import sys
    app = widgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())