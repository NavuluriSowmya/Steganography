import cv2
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import encryption
import decryption

img = None
msg = ""
password = ""

def load_image():
    global img
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        img = cv2.imread(file_path)  # Read the image
        if img is not None:
            messagebox.showinfo("Image Loaded", "Image loaded successfully!")
        else:
            messagebox.showerror("Error", "Failed to load image!")

def encrypt_button_click():
    global msg
    global password
    msg = message_entry_encrypt.get()
    password = password_entry_encrypt.get()
    
    if not msg or not password or img is None:
        messagebox.showerror("Input Error", "Please enter message, password and load an image")
        return
    
    # Creating dictionaries for encryption
    d = {chr(i): i for i in range(255)}
    encryption.encryptor(msg, password, d, img)

def decrypt_button_click():
    pas = password_entry_decrypt.get()
    
    if not password:
        messagebox.showerror("Input Error", "please provide password")
        return

    # Creating dictionaries for decryption
    c = {i: chr(i) for i in range(255)}
    d_msg = decryption.decryptor(password, msg, img, c, pas)
    decrypted_message_var.set(f"Decrypted Message: {d_msg}")

root = tk.Tk()
root.title("Steganography")
root.geometry("400x300")

# Create a notebook (tabbed view)
notebook = ttk.Notebook(root)
notebook.pack(expand=1,fill='both')

style = ttk.Style()
style.configure("TNotebook.Tab", 
                font=("Arial", 10),  # Increase the font size
                padding=[10, 10]) 

# Encryption Tab
encrypt_tab = ttk.Frame(notebook)
notebook.add(encrypt_tab, text="Encrypt")

# Image input button
load_image_button = tk.Button(encrypt_tab, text="Load Image", command=load_image)
load_image_button.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

# Encryption Message entry
message_label_encrypt = tk.Label(encrypt_tab, text="Enter secret message:")
message_label_encrypt.grid(row=1, column=0,padx=10, pady=10)
message_entry_encrypt = tk.Entry(encrypt_tab, width=40)
message_entry_encrypt.grid(row=1, column=1,padx=10, pady=10)

# Encryption Password entry
password_label_encrypt = tk.Label(encrypt_tab, text="Enter passcode:")
password_label_encrypt.grid(row=2, column=0)
password_entry_encrypt = tk.Entry(encrypt_tab, width=40)
password_entry_encrypt.grid(row=2, column=1,padx=10, pady=10)

# Encrypt button
encrypt_button = tk.Button(encrypt_tab, text="Encrypt", command=encrypt_button_click)
encrypt_button.grid(row=3, column=0, columnspan=2,padx=10, pady=10)

# Decryption Tab
decrypt_tab = ttk.Frame(notebook)
notebook.add(decrypt_tab, text="Decrypt")

# Decryption Password entry
password_label_decrypt = tk.Label(decrypt_tab, text="Enter passcode:")
password_label_decrypt.grid(row=1, column=0,padx=10, pady=10)
password_entry_decrypt = tk.Entry(decrypt_tab, width=40)
password_entry_decrypt.grid(row=1, column=1,padx=10, pady=10)

# Decrypt button
decrypt_button = tk.Button(decrypt_tab, text="Decrypt", command=decrypt_button_click)
decrypt_button.grid(row=2, column=0, columnspan=2,padx=10, pady=10)

# Decrypted message output
decrypted_message_var = tk.StringVar()
decrypted_message_label = tk.Label(decrypt_tab, textvariable=decrypted_message_var)
decrypted_message_label.grid(row=3, column=0, columnspan=2)

# Run the Tkinter loop
root.mainloop()



