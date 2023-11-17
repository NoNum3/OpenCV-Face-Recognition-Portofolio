import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()  # Create LBPH face recognizer
recognizer.read(
    r"OpenCV-Face-Recognition-master\FacialRecognition\trainer\trainer.yml"
)  # Load the trained model
cascade_path = "OpenCV-Face-Recognition-master\FaceDetection\Cascades\haarcascade_frontalface_default.xml"  # 載入人臉追蹤模型
face_cascade = cv2.CascadeClassifier(cascade_path)  # Create a face tracking classifier

cap = cv2.VideoCapture(0)  # Open the camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Create a comparison table of names and IDs
name = ""
confidence = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (540, 300))  # Resize the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray)  # Detect faces

    # Create a comparison table of names and IDs
    name_mapping = {
        "1": "Kenny",
        "2": "Kai",
        "4": "Jiageng",
        "5": "cc",
        "6": "Weisheng",
        "7": "cengjing",
    }

    # Draw a rectangle around the face
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a rectangle
        idnum, confidence = recognizer.predict(
            gray[y : y + h, x : x + w]
        )  # Get the ID number and confidence index of the face
        if str(idnum) in name_mapping:
            name = name_mapping[str(idnum)]  # Get the name of the face
            confidence = confidence
        else:
            name = ""
            confidence = 0

        #  Display the name and confidence index of the face
        cv2.putText(
            img,
            name,
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            img,
            f"Confidence: {confidence}",
            (x, y - 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    cv2.imshow("Face Recognition", img)  # Display the image

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all windows
