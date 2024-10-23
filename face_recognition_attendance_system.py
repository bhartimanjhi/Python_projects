import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime

known_face_encodings = []
known_face_names= []

# Use raw strings (r"") to handle file paths or use forward slashes ("/")
known_person1_image = face_recognition.load_image_file(r"C:\Users\bhart\AppData\Local\Temp\real python\WhatsApp Image 2023-12-26 at 22.09.40_cdbe525d (2).jpg")
known_person2_image = face_recognition.load_image_file(r"C:\Users\bhart\AppData\Local\Temp\real python\WhatsApp Image 2024-10-12 at 22.37.34_15d4a82e.jpg")
known_person3_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Screenshot 2024-10-13 165248.png")

# Process face encodings
known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]  # Fix here
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("papa")
known_face_names.append("bharu")
known_face_names.append("Rekha")

students= known_face_names.copy()


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+', newline="")
lnwriter = csv.writer(f)


# Load pre-trained face detection model
face_cap = cv2.CascadeClassifier(r"C:\Users\bhart\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

# Open the default camera
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

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()