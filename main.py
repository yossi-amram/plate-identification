import skimage.feature
from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt


def read_img_grey(path):
    car_image = imread(path, as_gray=True)
    return car_image



if __name__ == '__main__':
    car_image = read_img_grey('car.jpg')
    print(car_image)

    #normalizing the grey image for



    #plotting


