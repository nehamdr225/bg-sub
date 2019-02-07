def video_cap_sub():
    cam = cv2.VideoCapture('/run/media/neha/workshop/OpenCV Tutorial/Major Project/Road traffic video for object recognition.mp4')
    frame_count=int(cam.get(cv2.CAP_PROP_FRAME_COUNT))   
    fps = int(cam.get(cv2.CAP_PROP_FPS))  
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #img = cv2.imread('/run/media/neha/workshop/OpenCV Tutorial/Major Project/1.jpg')
    bg_sub = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cam.read()
        mask = bg_sub.apply(frame)
        cv2.imshow('frame', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cam.release()
    cv2.destroyAllWindows()

    



    


if __name__ == '__main__':
    import cv2
    import numpy as np

    vdo = video_cap_sub()
  