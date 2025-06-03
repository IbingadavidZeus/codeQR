import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

# Variable globale pour stocker l'image PIL
qr_image = None

def generate_qr_code():
    global qr_image  # pour que save_qr_code y ait accès
    data = entry_data.get()

    if not data:
        messagebox.showerror("Erreur", "Veuillez entrer un texte pour générer le code QR.")
        return

    # Générer le QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200))
    qr_image = img  # on garde l'image originale pour la sauvegarde

    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk

def save_qr_code():
    if qr_image is None:
        messagebox.showwarning("Aucun QR code", "Veuillez d'abord générer un QR code.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Fichiers PNG", "*.png")],
        title="Enregistrer le QR code"
    )

    if filepath:
        qr_image.save(filepath)
        messagebox.showinfo("Succès", f"QR code enregistré sous :\n{filepath}")

# Interface graphique
root = tk.Tk()
root.title("Générateur de Code QR")
root.geometry("400x550")

tk.Label(root, text="Générateur de QR Code", font=("Arial", 20)).pack(pady=10)
tk.Label(root, text="Texte à encoder :").pack(pady=5)

entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=5)

generate_button = tk.Button(root, text="Générer le QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Télécharger le QR Code", command=save_qr_code)
save_button.pack(pady=5)

img_label = tk.Label(root)
img_label.pack(pady=10)

root.mainloop()
