import cv2 as cv


class LenaIP:

    def __init__(self):
        self.matrix = cv.imread('img/Lena.png')

    def read_lena(self):
        dimensions = self.matrix.shape
        value = self.matrix[0][0]
        print(dimensions, value)
        return dimensions

    def convert_lena_to_grayscale(self):
        grayscale = cv.cvtColor(self.matrix, cv.COLOR_BGR2GRAY)
        dimension = grayscale.shape
        oct_val = grayscale[0][0]
        print(dimension, oct_val)
        return [dimension, oct_val]
