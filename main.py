from lena import LenaIP

if __name__ == '__main__':
    lena = LenaIP()
    print("Read Lena.png :")
    lena.read_lena()
    print("Convert Lena.png to grayscale :")
    lena.convert_lena_to_grayscale()
