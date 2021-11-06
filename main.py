import skimage.feature
from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import measure
from skimage.measure import regionprops




if __name__ == '__main__':
    # loading the original and grayscale pictures
    car_image = imread('car.jpg')
    gray_car_image = imread('car.jpg', as_gray=True)
    # gray_car_image *=255

    # plotting them along the binary picture
    fig, ax = plt.subplots(1, 3)

    ax[0].imshow(car_image)
    ax[1].imshow(gray_car_image, cmap='gray')

    # creating and plotting the binary
    threshold = threshold_otsu(gray_car_image)
    binary_image = gray_car_image > threshold



    ax[2].imshow(binary_image, cmap='gray')

    ax[0].imshow(binary_image, cmap='gray')

    # plt.show()

    # split to connected areas
    image_label = measure.label(binary_image)

    # going over all regions in the gray image and marking those big enough to possibly be the license plate
    for region in regionprops(image_label):

        # checking if the region is big enough to possibly be the license plate
        if region.area >= 50:
            # if so, drawing a red rectangle over it
            min_row, min_col, max_row, max_col = region.bbox
            rect_border = patches.Rectangle((min_row, min_col), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False)
            ax[2].add_patch(rect_border)


    plt.show()
    #normalizing the grey image



    #plotting


