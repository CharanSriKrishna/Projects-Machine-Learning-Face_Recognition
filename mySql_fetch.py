import mysql.connector
import numpy as np


con = mysql.connector.connect(
    user='root',
    host='localhost',
    password='csk1234*csK',
    database='faces',
    )
cursor = con.cursor(dictionary=True)


def get_en_db( names ):
   encode_images =[]
   cursor.execute("select * from face_details")
   res = cursor.fetchall()
   for i in res:
      en_img =  np.frombuffer(i['encode'])
      encode_images.append(en_img)
      names.append(i['rollno'])

   return encode_images

def mark_attend(name , date , time , attendance):
   prompt = f"""
            insert into student_attendance (rollno ,Date , Time , attendance) values ( '{ name }' ,'{date}', '{ time }' , '{ attendance }');
   """
   cursor.execute(prompt)
   con.commit()

def today(date):
   prompt = f"""
       SELECT * FROM student_attendance WHERE Date='{date}'
   """
   cursor.execute(prompt)
   return cursor.fetchall()
