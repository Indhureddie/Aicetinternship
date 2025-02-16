import cv2
import os
import numpy as np

def encode_message(img, msg, password):
    msg += "#####"  # Delimiter to indicate end of message
    binary_msg = ''.join(format(ord(i), '08b') for i in msg)
    
    if len(binary_msg) > img.size:
        raise ValueError("Message is too long for the image.")
    
    data_index = 0
    for row in img:
        for pixel in row:
            for i in range(3):  # Iterate through R, G, B
                if data_index < len(binary_msg):
                    pixel[i] = (pixel[i] & ~1) | int(binary_msg[data_index])  # LSB encoding
                    data_index += 1
                else:
                    break
    
    cv2.imwrite("encryptedImage.png", img)
    print("Message encoded successfully.")
    os.system("start encryptedImage.png")  # Open the image (Windows only)

def decode_message(img, password):
    binary_msg = ""
    for row in img:
        for pixel in row:
            for i in range(3):  # Extract from R, G, B
                binary_msg += str(pixel[i] & 1)
    
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_msg = ''.join(chr(int(char, 2)) for char in chars)
    
    # Extract the message before the delimiter #####
    message = decoded_msg.split("#####")[0]
    print("Decrypted message:", message)

if __name__ == "__main__":
    img = cv2.imread("mypic.png")
    if img is None:
        raise FileNotFoundError("Image not found. Please provide the correct path.")
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encode_message(img, msg, password)
    
    pas = input("Enter passcode for decryption: ")
    if pas == password:
        img = cv2.imread("encryptedImage.png")
        decode_message(img, password)
    else:
        print("Incorrect password. Access denied.")
