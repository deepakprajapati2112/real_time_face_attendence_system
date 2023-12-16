import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3,620)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background3.png')


folderModePath= 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

print(len(imgModeList))

while True:
    success, img = cap.read()

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[40:40 + 633, 804:804 + 414] = imgModeList[1]

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)