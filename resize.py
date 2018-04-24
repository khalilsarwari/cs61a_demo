import os
import cv2

for file in os.listdir('train'):
	path = os.path.join('train', file)
	image = cv2.imread(path)
	resized = cv2.resize(image, (250, 250))
	cv2.imwrite(path,resized)
