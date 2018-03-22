'''
Created on 14 Mar 2018

@author: schilsm
'''

from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtGui as gui

import pandas as pd, numpy as np, copy as cp
import math
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from PIL import Image, ImageFilter

from PyQt5.Qt import QMainWindow

class Main(QMainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        file_path = widgets.QFileDialog.getOpenFileName(self, 
        "Open Data File", "", "Image data files (*.bmp);;All files (*.*)")[0]
        if file_path:
            x = Image.open(file_path) # load an image from the hard drive
            ax = np.array(x)
            print(ax.shape)
            p0 = np.array([0,0,0])
            for px in ax[:,:]:
                if px == p0:
                    print("Yes")
                #print(px)
#             img = mpimg.imread(file_path)
#             img_plot = plt.imshow(img)
        
#         original.show() # display both images
#         blurred.show()    


if __name__ == '__main__':
    import sys
    app = widgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())