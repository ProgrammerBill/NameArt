#!/usr/bin/python
import cv2
import numpy as np

def get_width(img):
    return img.shape[1]

def get_height(img):
    return img.shape[0]

def sketch_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(gray)
    gblur_img = cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
    color_dodged = cv2.divide(gray, 255-gblur_img, scale=256)
    return 255 - cv2.divide(255-color_dodged, 255-gblur_img, scale=256)

def show_image(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)

if __name__ == '__main__':
    img = cv2.imread("Max.jpg")
    sketched = sketch_img(img)
   
    B, G, R = cv2.split(img)
    ret,thresh1=cv2.threshold(R, 50, 255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    dilated = cv2.dilate(thresh1,kernel)
    
    show_image("Image", img)
    show_image("Sketch", sketched)
    show_image("thresh1", thresh1)
    show_image("dilated", dilated)
    
    cv2.waitKey (0)
    cv2.destroyAllWindows()
