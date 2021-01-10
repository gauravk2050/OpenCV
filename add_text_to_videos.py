
import cv2
import datetime
#VideoCapture(File_Name or camera number)
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 3000)  # 3 is for width 
#cap.set(4, 3000) # 4 is for height
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):        #isOpened() gives False if the file name is wrong or the index given is worng
    """
    ret: return True if the frame is available 
    frame: will capture the frame
    """
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
       datet = str(datetime.datetime.now())
       #putText(image,text,origen,fontFace,color,thickness=None,lineType=None,bottomLeftOrigin=None)
       frame = cv2.putText(frame, text, (10, 50), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       frame = cv2.putText(frame, datet, (10, 100), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)

      """
      For Changing the colour of the capturing video use cv2.cvtColor(frame,colot_name)
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',gray)
      """

       cv2.imshow('frame', frame)
      """
      0xFF is the mask for 64 bit machine for the keyborad input
      0xFF == ord('q) : Checking for the press key is q or not 
      """
       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()













#  video capture properties
# https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
