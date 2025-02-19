import cv2
import os
import codecs
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

# Create dictionaries for encoding and decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def select_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img_path.set(file_path)

def encrypt_image():
    global encrypted_msg, password  # Keep track of the global variables
    img = cv2.imread(img_path.get())
    if img is None:
        messagebox.showerror("Error", "Could not load image.")
        return

    msg = msg_entry.get()
    password = pass_entry.get()  # Set password for encryption

    encrypted_msg = codecs.encode(msg, 'rot_13')  # Encrypt the message with ROT13
    msg_length = len(encrypted_msg)
    
    if msg_length > img.shape[0] * img.shape[1]:
        messagebox.showerror("Error", "Message too long to be embedded in this image.")
        return

    n, m = 0, 0
    for i in range(msg_length):
        img[n, m, 0] = d[encrypted_msg[i]]  # Embed only in one channel
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
    
    cv2.imwrite("encryptedImage.png", img)
    os.system("start encryptedImage.png")

    # Display encrypted message in ROT13 form
    messagebox.showinfo("Encrypted Message", f"Encrypted Message (ROT13): {encrypted_msg}")
    messagebox.showinfo("Success", "Image encrypted successfully. Check the output image.")

def decrypt_image():
    pas = pass_decrypt_entry.get()
    if password != pas:
        messagebox.showerror("Error", "Invalid passcode!")
        return
    
    img = cv2.imread("encryptedImage.png")
    if img is None:
        messagebox.showerror("Error", "Could not load encrypted image.")
        return
    
    decrypted_chars = []
    n, m = 0, 0
    for _ in range(len(encrypted_msg)):
        decrypted_chars.append(c[img[n, m, 0]])
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
    
    decrypted_msg = codecs.decode("".join(decrypted_chars), 'rot_13')
    messagebox.showinfo("Decrypted Message", f"Decrypted message: {decrypted_msg}")

# Create the main window
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Create StringVar for storing the image path
img_path = tk.StringVar()

# Create UI elements
tk.Label(root, text="Select an Image").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=img_path, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_image).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Enter Secret Message").grid(row=1, column=0, padx=10, pady=5)
msg_entry = tk.Entry(root, width=40)
msg_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Passcode").grid(row=2, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Encrypt Image", command=encrypt_image).grid(row=3, column=1, padx=10, pady=20)

tk.Label(root, text="Enter Passcode for Decryption").grid(row=4, column=0, padx=10, pady=5)
pass_decrypt_entry = tk.Entry(root, width=40, show="*")
pass_decrypt_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Decrypt Image", command=decrypt_image).grid(row=5, column=1, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
