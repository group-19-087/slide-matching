import cv2
import numpy
import numpy as np
import os
import ffmpeg
import subprocess

# Extracting a dataframe for every second
command = "ffmpeg -i TrimmedVideo.mp4 -vf fps=1 frames/frame%04d.jpg -hide_banner"
subprocess.call(command, shell=True)

path, dirs, files = next(os.walk("./frames"))
file_count = len(files)
print(file_count)
i = "0001"

while int(i)<file_count :
    img1 = cv2.imread('thumb0135.jpg',0)
    # print('frames/frame'+ i +'.jpg')
    # getting the difference of the images
    img2 = cv2.imread('frames/frame' + i + '.jpg', 0)
    res = cv2.absdiff(img1, img2)
    res = res.astype(np.uint8)
    percentage = (numpy.count_nonzero(res) * 100) / res.size
    print(percentage)

    if percentage < 1:
        print('match found : frames/frame' + i + '.jpg')
        break
    else:
        print(i)
        i = str(int(i)+1)
        while len(i) < 4:
            i = '0' + i
        print(i)


# img1 = cv2.imread('thumb0135.jpg', 0)
# img2 = cv2.imread('frames/frame0143.jpg', 0)

#--- take the absolute difference of the images ---
# res = cv2.absdiff(img1, img2)

#--- convert the result to integer type ---
# res = res.astype(np.uint8)

#--- find percentage difference based on number of pixels that are not zero ---
# percentage = (numpy.count_nonzero(res) * 100)/ res.size
#
# print(percentage)

