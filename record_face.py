import cv2
import numpy as np 
import sqlite3
import os

conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c = conn.cursor()


face_cascade = cv2.CascadeClassifier('C:/Users/Qweku/Desktop/NEW_CODE/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


Fullname = input("Enter your name: ")
Id_number = input("Index: ")
Relationship = input("Relationship: ")
c.execute('INSERT INTO Details(id_no,name,Relationship) VALUES (?,?,?)', (Id_number,Fullname,Relationship))


uid = c.lastrowid
print(uid)

counter = 0

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	for (x,y,w,h) in faces:
		counter += 1
		cv2.imwrite(f"dataset/{Fullname}."+str(Id_number)+"."+str(counter)+".jpg",gray[y:y+h,x:x+w])
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
		cv2.waitKey(100)
	cv2.imshow('img',img)
	if cv2.waitKey(10)== ord('q'):
		break

	if counter == 100:
		break
cap.release()




conn.commit()

conn.close()
cv2.destroyAllWindows()