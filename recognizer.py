import cv2
import numpy as np
import face_recognition
import encode
import markattend

classNames = []
inclass=[]
#print(myList)
encodeListKnown=encode.addimages(classNames)

print('Encoding Complete')

cap = cv2.VideoCapture(0)
f=True
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            if name not in inclass:
                print(name," entered class")
                encode.markAttendance(name)
                inclass.append(name)
                f=True
            elif(f):
                print(name," already in class")
                f=False
            

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1)==ord(" "):
        markattend.check()
        markattend.soting()
        break
cap.release()
cv2.destroyAllWindows()
