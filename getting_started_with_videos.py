import cv2

# for capturing video
cap = cv2.VideoCapture(0)
# for saving video
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# or fourcc = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter(output file,fourcc,no_of_fame_pereconds)
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    '''
    cap.read() return true is the frame is available in - ret
    and frame variable will capture the frame
    '''
    ret, frame = cap.read()
    if ret == True:

        '''
        cap.get(cv2.CAP_PROP_FRAM)
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        get() function is use to get the property of the video
        '''
        out.write(frame) # writing this frame into the file

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

'''
link for fourcc code
http://www.fourcc.org/codecs.php
link of getting videos property
https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

'''
















# video capture properties
# https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d