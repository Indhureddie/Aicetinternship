import cv2

def decode_message(img, password):
    binary_msg = ""
    for row in img:
        for pixel in row:
            for i in range(3):
                binary_msg += str(pixel[i] & 1)
    
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_msg = ''.join(chr(int(char, 2)) for char in chars)
    
    extracted_data = decoded_msg.split("#####")[0]
    stored_password, message = extracted_data.split("|", 1)
    
    if stored_password == password:
        print("Decrypted message:", message)
    else:
        print("Incorrect password. Access denied.")

if __name__ == "__main__":
    img = cv2.imread("encryptedImage.png")
    if img is None:
        raise FileNotFoundError("Image not found. Please provide the correct path.")
    
    password = input("Enter passcode for decryption: ")
    decode_message(img, password)
