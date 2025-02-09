import cv2
import face_recognition
import numpy as np
import xlsxwriter
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

print("-------------WELCOME TO THE FACE RECOGNITION SYSTEM-------------\n\nPlease Wait...\nWhile the system is working...\nThank you for your patience! Our face recognition system is starting up, and we appreciate your understanding\nas we work to provide you with a seamless experience.\nPlease hold on for just a moment!")

# Initialize known face encodings and names
known_face_encodings = []
known_face_names = []

# Load and encode each image separately
def encode_images():
    global known_face_encodings, known_face_names
    
    try:
        person1_image = face_recognition.load_image_file(r"C:\\Users\\bhart\\OneDrive\\Pictures\\Camo Studio Snapshot 2024-12-12 - 20-39-17.jpg")
        person1_encoding = face_recognition.face_encodings(person1_image)
        if person1_encoding:
            known_face_encodings.append(person1_encoding[0])
            known_face_names.append("Bharti Manjhi")

        person2_image = face_recognition.load_image_file(r"C:\\Users\\bhart\\OneDrive\\Pictures\\WhatsApp Image 2024-12-12 at 20.35.14_72a3f6a8.jpg")
        person2_encoding = face_recognition.face_encodings(person2_image)
        if person2_encoding:
            known_face_encodings.append(person2_encoding[0])
            known_face_names.append("Bharti Premani")

        
        person3_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Picture1.png")
        person3_encoding = face_recognition.face_encodings(person3_image)
        if person3_encoding:
            known_face_encodings.append(person3_encoding[0])
            known_face_names.append("Simran Jain")

        person4_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\WhatsApp Image 2024-12-13 at 11.16.32_cb3c0ab9.jpg")
        person4_encoding = face_recognition.face_encodings(person4_image)
        if person4_encoding:
            known_face_encodings.append(person4_encoding[0])
            known_face_names.append("Yuvraj Tiwari")
        
        person5_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\WhatsApp Image 2024-12-13 at 11.06.47_6c27e8a2.jpg")
        person5_encoding = face_recognition.face_encodings(person5_image)
        if person5_encoding:
            known_face_encodings.append(person5_encoding[0])
            known_face_names.append("Vikas Kushwah")

        person6_image = face_recognition.load_image_file(r"C:\Users\bhart\Downloads\WhatsApp Image 2025-01-18 at 11.26.09_49be30e2.jpg")
        person6_encoding = face_recognition.face_encodings(person6_image)
        if person6_encoding:
            known_face_encodings.append(person6_encoding[0])
            known_face_names.append("Priyanka Bandil")

        person7_image = face_recognition.load_image_file(r"C:\Users\bhart\Downloads\WhatsApp Image 2025-01-18 at 10.26.38_678b1aaa.jpg")
        person7_encoding = face_recognition.face_encodings(person7_image)
        if person7_encoding:
            known_face_encodings.append(person7_encoding[0])
            known_face_names.append("Lisha Chaurasia")

        person8_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Camo Studio Snapshot 2024-11-29 - 14-18-51.jpg")
        person8_encoding = face_recognition.face_encodings(person8_image)
        if person8_encoding:
            known_face_encodings.append(person8_encoding[0])
            known_face_names.append("Anmol Rana")

        person9_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Camo Studio Snapshot 2024-11-29 - 14-18-43.jpg")
        person9_encoding = face_recognition.face_encodings(person9_image)
        if person9_encoding:
            known_face_encodings.append(person9_encoding[0])
            known_face_names.append("Aryan Singh Sikarwar")

        person10_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Screenshot 2024-10-13 165248.png")
        person10_encoding = face_recognition.face_encodings(person10_image)
        if person10_encoding:
            known_face_encodings.append(person10_encoding[0])
            known_face_names.append("Rekha Manjhi")

        person11_image = face_recognition.load_image_file(r"C:\Users\bhart\OneDrive\Pictures\Camo Studio Snapshot 2024-11-29 - 14-18-22.jpg")
        person11_encoding = face_recognition.face_encodings(person11_image)
        if person11_encoding:
            known_face_encodings.append(person11_encoding[0])
            known_face_names.append("Aneesh Tomar")



        # Add more people in the same way...

    except Exception as e:
        messagebox.showerror("Error", f"Error while encoding images: {e}")

# Variables for attendance
video_capture = None
running = False
students = []
output_file = ""

# Function to start attendance
def start_attendance():
    global video_capture, running, students, output_file
    if running:
        messagebox.showinfo("Info", "Attendance is already running.")
        return

    if not known_face_encodings:
        messagebox.showerror("Error", "No face encodings found. Please ensure images are loaded correctly.")
        return

    running = True
    students = known_face_names.copy()
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    output_file = f"{current_date}.xlsx"
    video_capture = cv2.VideoCapture(0)

    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()
    worksheet.write("A1", "Name", workbook.add_format({'bold': True}))
    worksheet.write("B1", "Time", workbook.add_format({'bold': True}))
    row = 1

    while running:
        ret, frame = video_capture.read()
        if not ret:
            messagebox.showerror("Error", "Failed to access the camera.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compute face distances and get best match
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            name = "Unknown"

            if face_distances[best_match_index] < 0.5:  # Adjust the threshold
                name = known_face_names[best_match_index]

                # Check if the detected face is already recorded
                if name in students:
                    students.remove(name)  # Remove from the list once recorded
                    current_time = datetime.now().strftime("%H:%M:%S")
                    worksheet.write(row, 0, name)
                    worksheet.write(row, 1, current_time)
                    row += 1

            else:
                name = "Unknown"  # Keep it unknown if no valid match

            # Draw rectangle around face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("a"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    workbook.close()
    messagebox.showinfo("Success", f"Attendance saved to {output_file}")


# Stop Attendance Function
def stop_attendance():
    global running
    if not running:
        messagebox.showinfo("Info", "Attendance is not running.")
        return

    running = False
    messagebox.showinfo("Stopped", "Attendance has been stopped.")

# Tkinter GUI
root = tk.Tk()
root.title("Attendance System")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# Add GUI Elements
tk.Label(root, text="Face Recognition Attendance System Using IOT", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333").pack(pady=20)

start_button = tk.Button(root, text="Start Attendance", font=("Arial", 12), bg="#4caf50", fg="white", command=start_attendance)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Attendance", font=("Arial", 12), bg="#f44336", fg="white", command=stop_attendance)
stop_button.pack(pady=10)

tk.Label(root, text="SHOW YOUR FACE\n\nPress 'a' in video window screen to stop manually\n\nPlease wait while the camera is opening...\n\nThank you for your patience! Our face recognition system is starting up, and we appreciate your understanding as we work to provide you with a seamless experience.\nPlease hold on for just a moment!", font=("Arial", 15), bg="#f0f8ff", fg="#555").pack(pady=20)

# Load Images and Encodings on Startup
encode_images()

# Run the GUI
root.mainloop()
