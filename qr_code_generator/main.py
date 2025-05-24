import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    data = entry_data.get()

    if not data:
        messagebox.showerror("Erreur", "Veuillez entrer un texte pour générer le code QR.")
        return

    # Création du QR code avec taille minimale, mais adaptative
    qr = qrcode.QRCode(
        version=None,  # laisse qrcode déterminer la version (taille logique)
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Génération de l'image
    img = qr.make_image(fill_color="black", back_color="white")

    # Redimensionnement à taille fixe (ex. 200x200 pixels)
    # img = img.resize((200, 200), Image.ANTIALIAS)

    # Conversion pour affichage dans Tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Affichage dans le label
    img_label.config(image=img_tk)
    img_label.image = img_tk

# Interface
root = tk.Tk()
root.title("Générateur de Code QR")
root.geometry("400x500")

tk.Label(root, text="Générateur de QR Code", font=("Arial", 20)).pack(pady=10)
tk.Label(root, text="Texte à encoder :").pack(pady=5)

entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=5)

generate_button = tk.Button(root, text="Générer le QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

root.mainloop()
