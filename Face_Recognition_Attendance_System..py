import face_recognition
import cv2
import numpy as np
import csv

from datetime import datetime

video_capture = cv2.VideoCapture(0)

Rehan_img = face_recognition.load_image_file("Faces/Rehan.jpg")
Rehan_encoding = face_recognition.face_encodings(Rehan_img)[0]

Wafiya_img = face_recognition.load_image_file("Faces/Wafiya.png")
Wafiya_encoding = face_recognition.face_encodings(Wafiya_img)[0]

Known_face_encoding = [Rehan_encoding,Wafiya_encoding]
Known_face_names = ["Rehan","Wafiya"]

#List of expected Student
student = Known_face_names.copy()

face_location = []
face_encoding = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv","w+", newline="")
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0),fx = 0.25, fy = 0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    name = ""
    for face_encoding in face_encodings :
        matches = face_recognition.compare_faces(Known_face_encoding,face_encoding)
        face_distance = face_recognition.face_distance(Known_face_encoding,face_encoding)
        best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
            name = Known_face_names[best_match_index]
    
    #add text if person is present
    if name in Known_face_names:
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,100)
        fontscale = 1.5
        fontColor = (255, 0,0)
        thickness = 3
        LineType = 2
        cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontscale, fontColor, thickness, LineType)

        if name in student:
            student.remove(name)
            current_time = now.strftime("%H-%M-S")
            lnwriter.writerow([name,current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()