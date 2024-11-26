import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime

known_face_encodings = []
known_face_names= []

known_person1_image = face_recognition.load_image_file(r"C:\Users\bhart\AppData\Local\Temp\real python\WhatsApp Image 2024-11-15 at 21.31.13_5743f08e.jpg")
known_person2_image = face_recognition.load_image_file(r"C:\Users\bhart\AppData\Local\Temp\real python\WhatsApp Image 2024-11-15 at 18.00.04_70675250.jpg")
known_person3_image = face_recognition.load_image_file(r"C:\Users\bhart\AppData\Local\Temp\real python\WhatsApp Image 2024-11-15 at 21.25.04_415b26e4.jpg")


known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]


known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)


known_face_names.append("Bharti Manjhi")
known_face_names.append("Simran Jain")
known_face_names.append("Bharti Premani")




students= known_face_names.copy()


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+', newline="")
lnwriter = csv.writer(f)


face_cap = cv2.CascadeClassifier(r"C:\Users\bhart\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_locations=face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)




    for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
        name = "unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        if name in known_face_names:
           if name in students:
             students.remove(name)
             print(students)
             current_time = now.strftime("%H-%M-%S")
             lnwriter.writerow([name, current_time])



        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

        cv2.imshow("video", frame)

    

    # Exit the loop if 'a' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("a"):
        break

video_capture.release()
cv2.destroyAllWindows()