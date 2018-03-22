
from PIL import Image, ImageFilter  # imports the library

original = Image.open("C:\\users\\schilsm\\Desktop\\test.bmp") # load an image from the hard drive
blurred = original.filter(ImageFilter.BLUR) # blur the image

original.show() # display both images
blurred.show()
