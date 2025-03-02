import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

if img is None:
    print("Error: Unable to read the encrypted image file.")
    exit()

# Read the stored password
with open("password.txt", "r") as file:
    original_password = file.read().strip()

# Ask for password
pas = input("Enter passcode for Decryption: ")

if pas == original_password:
    binary_msg = ""
    
    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_msg += str(pixel[channel] & 1)  # Extract LSB

    # Convert binary to text
    char_list = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    decoded_chars = [chr(int(char, 2)) for char in char_list]

    msg_length = int("".join(decoded_chars[:3]))  # Get message length
    message = "".join(decoded_chars[3:3+msg_length])  # Extract exact message

    print("\nDecryption Successful! Secret message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
