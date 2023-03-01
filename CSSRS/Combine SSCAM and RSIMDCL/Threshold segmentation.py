import os
from PIL import Image
import shutil


file_path = 'D:/deeplearning_test/256png1_5/73.55/73sscam/'
save_path = 'D:/deeplearning_test/256png1_5/73.55/73erzhihua/'
if not os.path.exists(save_path):
    os.makedirs(save_path)
###Binarization
for filename in os.listdir(file_path):
    print(filename)
    img = Image.open(file_path + filename)
    img1 = img.convert('L')
    threshold = 32

    table = []
    for i in range(256):
        if i < threshold :
            table.append(0)  #Control of white areas in new images
        else:
            table.append(1)

    photo = img1.point(table, '1')
    photo.save(save_path + filename)
