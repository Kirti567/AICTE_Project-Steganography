import cv2
import numpy as np

# Load the image
img = cv2.imread("mypic.jpg")  # Ensure the image exists

if img is None:
    print("Error: Unable to read the image file.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg = f"{len(msg):03d}" + msg  # Store message length as first 3 characters

binary_msg = ''.join(format(ord(char), '08b') for char in msg)  # Convert to binary

data_index = 0
msg_len = len(binary_msg)

for row in img:
    for pixel in row:
        for channel in range(3):  # Modify RGB channels
            if data_index < msg_len:
                pixel[channel] = (pixel[channel] & 0xFE) | int(binary_msg[data_index])
                data_index += 1

cv2.imwrite("encryptedImage.png", img)

# Save password separately
with open("password.txt", "w") as file:
    file.write(password)

print("Encryption Complete! Secret message hidden successfully.")
