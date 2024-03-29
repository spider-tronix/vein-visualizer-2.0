import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import time

def multi_clahe(img, num):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(num):
	    img = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4+i*2,4+i*2)).apply(img)
    return img

def process(frame):
		#frame_start = time.time()
		img = cv2.resize(frame,(256,256))
		img = np.fliplr(img)

		img_r = img.reshape((256*256, 1))
		res = np.zeros((256**2, 1), dtype=np.uint8)
		
		for i in tmatrix:
			res[i[0]] = img_r[i[1]-1]
		res = res.reshape((256, 256, 1))
		return(res)
#tmatrix = np.load('tmat-new.npy') 


def kmatrix(img, k1, k2, k3):
	#dst = [[k1,  k2,  1.31038377e-03 -3.11018871e-05  k3]]	
	# undistort

	dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
	return(dst)


cap = cv2.VideoCapture('video.mp4')
ret, frame = cap.read()

mtx = np.array([[534.07088367, 0.0, 341.53407538], [ 0.0, 534.11914599, 232.94565269], [ 0.0, 0.0, 1.0]])
dist = np.array([[-2.92971637e-01,  1.07706963e-01,  1.31038377e-03, -3.11018871e-05,  4.34798099e-02]])
h, w = frame.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

t = []
while(ret):
	try:
		ret, frame = cap.read()
		start = time.time()
		frame = cv2.resize(frame, (256, 256)) 
		frame1 = multi_clahe(frame, 3)
		

		'''res = process(frame1)
		cv2.imshow('res', np.hstack((res,res)))	 '''

		res = kmatrix(frame1, 0, 0, 0)
		cv2.imshow('res',cv2.undistort(frame1, mtx, dist, None, newcameramtx))
		if (cv2.waitKey(1) & 0xFF == ord('q')):
			break
		end = time.time()
		t.append(1/(end-start))
	except(cv2.error):
		pass
print(np.average(t))
cap.release()
cv2.destroyAllWindows()
