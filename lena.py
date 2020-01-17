import cv2 as cv


def read_lena():
    matrix = cv.imread('img/Lena.png')
    dimensions = matrix.shape
    value = matrix[0][0]
    print(dimensions, value)
    return dimensions
