

def video_cap_sub():
    cam = cv2.VideoCapture('/run/media/neha/workshop/OpenCV Tutorial/Major Project/Baneshwor Traffic-MaZ12OeZ25I.mp4')
    #cam = cv2.VideoCapture('/run/media/neha/workshop/OpenCV Tutorial/Major Project/Live Video of Heavy Traffic Jam at Ring Road, Delhi In India-1ZA3oaTEfEo.f133.mp4')
    
    '''frame_count=int(cam.get(cv2.CAP_PROP_FRAME_COUNT))   
    fps = int(cam.get(cv2.CAP_PROP_FPS))  
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #img = cv2.imread('/run/media/neha/workshop/OpenCV Tutorial/Major Project/1.jpg')
    '''
    
    
    bg_sub = cv2.bgsegm.createBackgroundSubtractorMOG()

    while True:
        ret, frame = cam.read()
        mask = bg_sub.apply(frame)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)              
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cam.release()
    cv2.destroyAllWindows()

    



    


if __name__ == '__main__':
    import cv2
    import numpy as np

    vdo = video_cap_sub()
  