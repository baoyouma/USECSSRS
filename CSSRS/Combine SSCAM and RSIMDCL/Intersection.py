import os
from PIL import Image
import shutil

image1_path = "D:/deeplearning_test/256png1_5/73.55/55erzhihua/"
image2_path = "D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/55otsu/"
save_path = 'D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/55cssrs/'
if not os.path.exists(save_path):
    os.makedirs(save_path)


def pixel_equal(image1, image2, x, y):
    # Take two picture pixel points
    piex1 = image1.load()[x, y]
    piex2 = image2.load()[x, y]

    if piex1 + piex2 == 510:
        return True
    else:
        return False
def compare(image1, image2):
    left = 0		# Position of the start of the coordinates
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            if pixel_equal(image1, image2, i, j):
                image1.putpixel((i, j), 255)
            else:
                image1.putpixel((i, j), 0)
    img = image1
    img.save(save_path + filename1)

if __name__ == "__main__":
    for filename1 in os.listdir(image1_path):
        print(filename1)
        image1 = Image.open(image1_path + filename1)
        basename1=os.path.basename(filename1[:-4])
        for filename2 in os.listdir(image2_path):
            print(filename2)
            image2 = Image.open(image2_path + filename2)
            basename2 = os.path.basename(filename2[:-4])
            if basename1 == basename2:
                compare(image1, image2)
