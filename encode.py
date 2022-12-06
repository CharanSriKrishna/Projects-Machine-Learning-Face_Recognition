import face_recognition
import cv2
import os
from datetime import datetime
from datetime import date
from csv import writer
path='images'
myList = os.listdir(path)
images = []

def addimages(classNames):
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                now = datetime.now()
                now2=date.today()
                dtString = now.strftime('%H:%M')
                th=now.strftime('%H')
                tm=now.strftime('%M')
                datestring=now2.strftime("%d/%m")
                m=1
                if (int(th)<8):
                    m=1
                elif(int(th)==8) and (int(tm)<=50):
                    m=1
                else:
                    m=-1   
                f.writelines(f'{name},{dtString},{datestring},{m}\n')
