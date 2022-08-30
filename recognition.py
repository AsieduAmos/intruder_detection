import cv2
import numpy as np 
import sqlite3
import os

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("SELECT * FROM Details")
print(c.fetchall())

fname = "recognizer/trainingData.yml"
if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)

face_cascade = cv2.CascadeClassifier('C:/Users/Qweku/Desktop/NEW_CODE/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 3)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
		ids,conf = recognizer.predict(gray[y:y+h,x:x+w])

		c.execute("SELECT name FROM Details WHERE  id_no = (?)", (ids,))
		result1 = c.fetchone()
		result1 = "+".join(result1)

		c.execute("SELECT relationship FROM Details WHERE  id_no = (?)", (ids,))
		result2 = c.fetchone()
		result2 = "+".join(result2)
		# name = result[0][0]
		# print(name,result)
		print(ids,conf)
		if conf < 50:
			cv2.putText(img, f"Name: {result1}", (x,y-90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150,255,0),2)
			cv2.putText(img, f"relationship: {result2}", (x,y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150,255,0),2)
			cv2.putText(img, f"Distance: {conf}", (x,y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150,255,0),2)
			# print(name,result)
			print(ids,conf)
            
		else:
			cv2.putText(img,'UNKWON PERSON DETECTED',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),2)
	cv2.imshow('Face Recognizer',img)
	
	if cv2.waitKey(10) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()