import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qr_code():
    data = entry_data.get()

    if not data:
        messagebox.showerror("Error", "Please enter some data to generate QR code.")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Resize the image to fit the GUI better
    # img = img.resize((200, 200), Image.ANTIALIAS)

    # Convert to ImageTk for Tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Update label with new image
    img_label.config(image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection


# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")

title = tk.Label(root, text="QR Code Generator", font=("Arial", 24))
title.pack(pady=20)

tk.Label(root, text="Enter data to encode:").pack(pady=10)

entry_data = tk.Entry(root, width=50)
entry_data.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)    
generate_button.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

root.mainloop()
