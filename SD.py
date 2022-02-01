import cv2
import numpy as np
cam = cv2.VideoCapture("rtsp://atul:ttpl1234@192.168.10.231:554//Streaming/channels/102")

cam1 = cv2.VideoCapture("rtsp://atul:ttpl1234@192.168.10.232:554//Streaming/channels/102")
# cam1.set(320, 240)
cam2 = cv2.VideoCapture("rtsp://atul:ttpl1234@192.168.10.233:554//Streaming/channels/102")
# cam2.set(320, 240)
cam3 = cv2.VideoCapture("rtsp://atul:ttpl1234@192.168.10.241:554//Streaming/channels/102")
# cam3.set(320, 240)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
# width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outputvid.avi', -1, 20.0, (640,480))
# result = cv2.VideoWriter('filename.avi', 
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video1.avi', fourcc, 20.0, size)
out1 = cv2.VideoWriter('video2.avi', fourcc, 20.0, size)
out2 = cv2.VideoWriter('video3.avi', fourcc, 20.0, size)
out3 = cv2.VideoWriter('video4.avi', fourcc, 20.0, size)
while True:
    
    ret, frame = cam.read()
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    ret3, frame3 = cam3.read()
    # if ret==True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
    if (ret,ret1,ret2,ret3):
        small = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)
        cv2.imshow('Cam 0',small)
        small1 = cv2.resize(frame1, (0, 0), fx=0.50, fy=0.50)
        cv2.imshow('Cam 1',small1)
        small2 = cv2.resize(frame2, (0, 0), fx=0.50, fy=0.50)
        cv2.imshow('Cam 2',small2)
        small3 = cv2.resize(frame3, (0, 0), fx=0.50, fy=0.50)
        cv2.imshow('Cam 3',small3)
        # print("camera 0 started")
        out.write(frame)
        out1.write(frame1)
        out2.write(frame2)
        out3.write(frame3)
    # if (ret1):
    #     cv2.imshow('Cam 1',frame1)
    #     print("camera 1 started")
    # if (ret2):
    #     cv2.imshow('Cam 2',frame2)
    #     print("camera 2 started")
    # if (ret3):
    #     cv2.imshow('Cam 3',frame3)
    #     print("camera 3 started")
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # else:
    #     break

# Release everything if job is finished
out.release()
cam.release()
cam1.release()
cam2.release()
cam3.release()

cv2.destroyAllWindows()
