import os
from PIL import Image
import shutil
import cv2

image1_path = "D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/realL/"
image2_path = "D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/fakeL/"
save_path = 'D:/deeplearning_test/256png1_5/55rsimresult/test_latest/images/55chafen/'
if not os.path.exists(save_path):

    os.makedirs(save_path)

files1 = os.listdir(image1_path)
for file1 in files1:
    image1 = cv2.imread(os.path.join(image1_path, file1))
    basename1 = os.path.basename(file1[:-4])
    files2 = os.listdir(image2_path)
    for file2 in files2:
        image2 = cv2.imread(os.path.join(image2_path, file2))
        basename2 = os.path.basename(file2[:-4])
        if basename1 == basename2:
            diff = cv2.absdiff(image1,image2)
            cv2.imwrite(save_path + str(file1), diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

