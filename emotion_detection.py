from deepface import DeepFace
import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError('Cannot open webcam')

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    if frame is None:
        raise ValueError('Unable to get a frame!')
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    # cv2.imshow('frame', frame)
    result = DeepFace.analyze(frame, actions=['emotion'], detector_backend=backends[1], enforce_detection=False)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,
                result['dominant_emotion'],
                (50, 50),
                font, 3,
                (0, 0, 255),
                2,
                cv2.LINE_4
                )
    cv2.imshow('Original Video', frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()