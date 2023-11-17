import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()  # 啟用訓練人臉模型方法
recognizer.read(
    r"OpenCV-Face-Recognition-master\FacialRecognition\trainer\trainer.yml"
)  # 讀取人臉模型檔
cascade_path = "OpenCV-Face-Recognition-master\FaceDetection\Cascades\haarcascade_frontalface_default.xml"  # 載入人臉追蹤模型
face_cascade = cv2.CascadeClassifier(cascade_path)  # 啟用人臉追蹤

cap = cv2.VideoCapture(0)  # 開啟攝影機
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Initialize variables to store the name and confidence
name = ""
confidence = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (540, 300))  # 縮小尺寸，加快辨識效率
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成黑白
    faces = face_cascade.detectMultiScale(gray)  # 追蹤人臉 ( 目的在於標記出外框 )

    # 建立姓名和 id 的對照表
    name_mapping = {
        "1": "Kenny",
        "2": "Kai",
        "3": "Ryan",
        "4": "Jiageng",
        "5": "cc",
        "6": "Weisheng",
        "7": "cengjing",
    }

    # 依序判斷每張臉屬於哪個 id
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 標記人臉外框
        idnum, confidence = recognizer.predict(
            gray[y : y + h, x : x + w]
        )  # 取出 id 號碼以及信心指數 confidence
        if str(idnum) in name_mapping:
            name = name_mapping[str(idnum)]  # 如果信心指數小於 60，取得對應的名字
            confidence = confidence
        else:
            name = ""
            confidence = 0

        # Display the name and confidence
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

    cv2.imshow("Face Recognition", img)  # 顯示影像

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有視窗
