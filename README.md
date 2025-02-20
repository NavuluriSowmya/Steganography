# Steganography
Python-based GUI application allows you to hide and extract secret messages within image files using steganography techniques. It enables encryption of messages by embedding them in an image and decryption for recovering the original message using a password.

## Features

- **Load Image**: Choose an image file (JPEG, PNG, BMP) to use for embedding a secret message.
- **Encrypt Message**: Enter a secret message and a password to embed the message securely into the image.
- **Decrypt Message**: Extract the secret message from the image using the same password used during encryption.
- **Password Protection**: Both encryption and decryption rely on a user-defined password to ensure secure hiding and revealing of the message.

## Requirements

Before running this application, make sure you have Python 3.x installed and the following libraries:

- `cv2` (OpenCV)
- `tkinter` (Python GUI library)
- `PIL` (Pillow for image handling)
- Custom modules: `encryption.py` and `decryption.py` (for implementing steganography logic)

You can install required libraries using the following commands:

```
pip install opencv-python
pip install Pillow
```

## Usage Instructions

### Encrypting a Message
1. Click **Load Image** to select an image file from your computer.
2. Enter the secret message you want to hide in the **Enter secret message** field.
3. Provide a **passcode** (password) for encryption in the **Enter passcode** field.
4. Click **Encrypt** to embed the message within the image.

### Decrypting a Message
1. Load the encrypted image.
2. Enter the same passcode used during encryption in the **Enter passcode** field.
3. Click **Decrypt** to retrieve and display the secret message.

## Running the Application

1. Clone or download this repository to your local machine.
2. Open the terminal or command prompt in the folder containing the Python script.
3. Run the application.
   
The application will launch a window with two tabs: **Encrypt** and **Decrypt**.

## License

This project is licensed under the MIT License. Feel free to fork, modify, and distribute as needed.

## Acknowledgments

- OpenCV for image processing
- Pillow for image handling
- Tkinter for creating the GUI

