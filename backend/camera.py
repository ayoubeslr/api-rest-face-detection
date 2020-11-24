# import cv2

# cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, 0)
#     detections = cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
#     if(len(detections) > 0):
#         (x,y,w,h) = detections[0]
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

#     # for (x,y,w,h) in detections:
#     # 	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
# import the necessary packages
import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()

    def get_frame(self):
        #extracting frames
            ret, frame = self.video.read()
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
            interpolation=cv2.INTER_AREA)                    
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            face_rects=face_cascade.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            break
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()