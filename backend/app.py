# from flask import Flask, render_template, request, jsonify, Response
# # from camera import VideoCamera

# app = Flask(__name__)


# # def gen(camera):
# #     while True:
# #         data= camera.get_frame()
# #         frame=data[0]
# #         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# # @app.route('/video_feed')
# # def video_feed():
# #     return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__=="__main__":
#     app.run(debug=True)

# import cv2

# # capture frames from a camera with device index=0
# cap = cv2.VideoCapture(0)

# # loop runs if capturing has been initialized 
# while(1): 

# 	# reads frame from a camera 
# 	ret, frame = cap.read() 

# 	# Display the frame
# 	cv2.imshow('Camera',frame) 
	
# 	# Wait for 25ms
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break
		
# # release the camera from video capture
# cap.release() 

# # De-allocate any associated memory usage 
# cv2.destroyAllWindows() 
# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)