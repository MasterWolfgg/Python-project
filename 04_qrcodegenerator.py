import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    # Get the name and phone number from the input fields
    name = name_entry.get()
    phone = phone_entry.get()

    # Combine the data into a single string
    data = f"Name: {name}\nPhone: {phone}"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and display the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

# Create a tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Create input fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

window.mainloop()