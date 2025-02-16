import cv2
import os
import numpy as np

def encode_message(img, msg, password):
    msg = password + "|" + msg + "#####"  
    binary_msg = ''.join(format(ord(i), '08b') for i in msg)
    
    if len(binary_msg) > img.size:
        raise ValueError("Message is too long for the image.")
    
    data_index = 0
    for row in img:
        for pixel in row:
            for i in range(3): 
                if data_index < len(binary_msg):
                    pixel[i] = (pixel[i] & ~1) | int(binary_msg[data_index])
                    data_index += 1
                else:
                    break
    
    cv2.imwrite("encryptedImage.png", img)
    print("Message encoded successfully.")
    os.system("start encryptedImage.png")

if __name__ == "__main__":
    img = cv2.imread("mypic.png")
    if img is None:
        raise FileNotFoundError("Image not found. Please provide the correct path.")
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encode_message(img, msg, password)
