import face_recognition
import cv2
import base64
import numpy as np
import mySql_fetch as sql

def get_encode(img):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    img = face_recognition.face_encodings(img)[0]
    img = img.tobytes()
    return img

def con_binary(filename):
    file = open('H:\Face_Recognition\images\\20CS016.jpg','rb').read()
    file = base64.b64encode(file)
    return file

def add_person():
   address=input("Location:")
   encode = cv2.imread(address)
   encode = get_encode(encode)
   img = con_binary(address)
   name = input("Name")
   RollNo = input("RollNo")
   sql.cursor.execute("insert into face_details values (%s , %s, %s ,%s )",(RollNo , name , img , encode))
   sql.con.commit()

add_person()
