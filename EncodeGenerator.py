import cv2
import face_recognition
import pickle
import os

#importing the student images
folderPath= 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # print(path)
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

print(studentIds)

def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encoding(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
print("Encoding Completed")