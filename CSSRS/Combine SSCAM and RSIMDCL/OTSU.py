import cv2
import os
import numpy as np
from PIL import Image

from tqdm import tqdm


image_path='D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/55chafen/'
save_path = 'D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/55otsu/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

for filename in os.listdir(image_path):
    print(filename)
    image = cv2.imread(image_path + filename)
    def rgb2gray(image):
        h = image.shape[0]
        w = image.shape[1]
        grayimage = np.zeros((h, w), np.uint8)
        for i in tqdm(range(h)):
            for j in range(w):
                grayimage[i, j] = 0.144 * image[i, j, 0] + 0.587 * image[i, j, 1] + 0.299 * image[i, j, 2]
        return grayimage
    ### OTSU
    def otsu(image):
        ### Height and width
        h = image.shape[0]
        w = image.shape[1]
        ### Request total pixels
        m = h*w
        otsuimg = np.zeros((h, w), np.uint8)
        ##Initial Threshold
        initial_threshold = 0
        ### Final Threshold
        final_threshold   = 0
        # Initialisation of statistical parameters for the number of grey levels
        histogram = np.zeros(256, np.int32)
        # Initialise the statistical parameters for the distribution of each grey level in the image
        probability = np.zeros(256, np.float32)
        ### Statistics of the number of grey levels
        for i in tqdm(range(h)):
            for j in range(w):
                s = image[i,j]
                histogram[s] = histogram[s] +1
        ### Statistical parameters for the distribution of each grey level in the image
        for i in tqdm(range(256)):
            probability[i] = histogram[i]/m
        for i in tqdm(range(255)):
            w0 = w1 = 0  ## Number of shades of grey in foreground and background
            fgs = bgs = 0  # Define the sum of the grey levels of the foreground pixel points and the sum of the grey levels of the background pixel points
            for j in range(256):
                if j <= i:  # Current i is the segmentation threshold
                    w0 += probability[j]  # Accumulation of foreground pixel points as a proportion of the whole image
                    fgs += j * probability[j]
                else:
                    w1 += probability[j]  # Accumulation of background pixel points as a proportion of the whole image
                    bgs += j * probability[j]
            u0 = fgs / w0  # Average grey level of foreground pixel points
            u1 = bgs / w1  # Average grey level of background pixel points
            G  = w0*w1*(u0-u1)**2
            if G >= initial_threshold:
                initial_threshold = G
                final_threshold = i
        print(final_threshold)
        for i in range(h):
            for j in range(w):
                if image[i, j] > final_threshold:
                    otsuimg[i, j] = 255
                else:
                    otsuimg[i, j] = 0
        return otsuimg


    grayimage = rgb2gray(image)
    otsuimage = otsu(grayimage)
    cv2.imwrite(save_path + filename, otsuimage)

cv2.waitKey()