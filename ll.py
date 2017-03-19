'''import cv2 as c

img = c.imread('ii/apple.png')
gris_img = c.cvtColor(img, c.COLOR_BGR2GRAY)
c.imshow('jj',img)
c.imshow( 'jj gris', gris_img)
c.waitKey(0)
c.destroyAllWindows()'''

'''import cv2  ##---- script para visualizar webcam

def show_webcam():
	cam = cv2.VideoCapture(1)
	while True:
		n,img = cam.read()
		
		cv2.imshow('my webcam', img)
		if cv2.waitKey(1) == 27: 
			break


	cv2.destroyAllWindows()

def main():

	show_webcam()

if __name__ == '__main__':
	main()'''

import time  ##--**-- OPENCV tomar fotografia ---**
import cv2

camara = cv2.VideoCapture(1)
time.sleep(0.05)  #--se detiene el flujo de datos de videocapture---
return_value, imagen = camara.read()
cv2.imwrite("opencv.png", imagen)
del(camara) 
img = cv2.imread('opencv.png')
cv2.imshow('dd', img)
cv2.waitKey(0)
##########################-----------------------------------------------------------
