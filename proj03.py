import cv2
face_obj = cv2.CascadeClassifier("E:/01/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_obj = cv2.VideoCapture(0)
while True:
    ret , video_obj1 = video_obj.read()
    color_obj = cv2.cvtColor(video_obj1,cv2.COLOR_BGR2GRAY)
    faces = face_obj.detectMultiScale(
        color_obj,
        scaleFactor=1.1,
        minNeighbors= 5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE,
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_obj1,(x,y),(x+w,y+h),(0,225,0),2)
    cv2.imshow("Video_ON",video_obj1)
    if cv2.waitKey(10) == ord("q"):
        break

video_obj.release()
