""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.10.1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.circle(frame, (w/3+x, h/3+y), w/20, WHITE, (5/3)*(w/14))
		cv2.circle(frame, (2*w/3+x, h/3+y), w/20, WHITE, (5/3)*(w/14))
		cv2.circle(frame, (w/3+x, h/3+y), w/45, BLACK, (5/3)*(w/18))
		cv2.circle(frame, (2*w/3+x, h/3+y), w/45, BLACK, (5/3)*(w/18))
		## Only an arc from an ellipse ##
		cv2.ellipse(frame, (w/2+x, 2*h/3+y), (w/3, w/7), 0, 10, 170, BLACK, (4/3)*(w/30))
		## Complete ellipse ##
		# cv2.ellipse(frame, ((w/2+x, 3*h/4+y), (w/3, w/7), 0), BLACK, 5)

		# Draws a rectangle
		# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

    # Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

    ### Grayscale stuff###
	# # Our operations on the frame come here
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# # Display the resulting frame
	# cv2.imshow('frame',gray)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()