import cv2
import os
import numpy as np
from PIL import Image

from tqdm import tqdm


image_path='D:/deeplearning_test/cut/pore2background_CUT/train_latest/images/fake_B-86/'
save_path = 'D:/deeplearning_test/cut/pore2background_CUT/train_latest/images/fake_B_86_gray/'

if not os.path.exists(save_path):
    os.makedirs(save_path)
for filename in os.listdir(image_path):
    color_img = cv2.imread(image_path + filename)
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2GRAY)
    # gray_img is still a two-dimensional matrix representation at this point, so the array-to-image conversion has to be implemented
    gray = Image.fromarray(gray_img)
    gray.save(save_path + filename)

