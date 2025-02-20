import cv2
import os
from tkinter import messagebox
def encryptor(msg,password,d,img):
 m = 0
 n = 0
 z = 0

 for i in range(len(msg)):
     img[n, m, z] = d[msg[i]]
     n = n + 1
     m = m + 1
     z = (z + 1) % 3

 cv2.imwrite("encryptedImage.jpg", img)
 os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows
 messagebox.showinfo("Encrypted", "Image has been encrypted and saved as encryptedImage.jpg")
