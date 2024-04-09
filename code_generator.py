import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr_code():
    # Retrieve user input
    file_name = file_name_entry.get().strip()
    if not file_name.endswith('.png'):
        file_name += '.png'
    url = url_entry.get().strip()

    # Validate input
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    if not file_name:
        messagebox.showerror("Error", "Please enter a file name")
        return

    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Display QR Code
    try:
        # Save the QR code to a temporary file for display purposes
        temp_file_path = file_name
        img.save(temp_file_path)
        show_qr_code(temp_file_path)
        messagebox.showinfo("Success", "QR code generated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_qr_code(file_path):
    img = Image.open(file_path)
    # Use Image.Resampling.LANCZOS for Pillow versions >= 8.0.0
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    qr_code_label.configure(image=img)
    qr_code_label.image = img  # Keep a reference to avoid garbage collection

# Set up the GUI
root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg='light blue')

# Center the window on the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Fonts and sizes
label_font = ('Arial', 28, 'bold')  # Adjust font size as needed
entry_font = ('Arial', 28, 'bold')  # Adjust font size as needed

# Use frames to center widgets
center_frame = tk.Frame(root, bg='light blue')
center_frame.pack(expand=True)

# Create and pack the widgets in the frame, adjust bg and font as needed
tk.Label(center_frame, text="File Name (e.g., vcet.png):", font=label_font, bg='light blue').pack()
file_name_entry = tk.Entry(center_frame, font=entry_font)
file_name_entry.pack(pady=5)

tk.Label(center_frame, text="URL:", font=label_font, bg='light blue').pack()
url_entry = tk.Entry(center_frame, font=entry_font)
url_entry.pack(pady=5)

generate_button = tk.Button(center_frame, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Label to display QR Code, adjust background
qr_code_label = tk.Label(center_frame, bg='light blue')
qr_code_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
