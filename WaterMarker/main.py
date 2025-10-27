# Water Marker
# September 2025
# Charles (Chip) Brady
# This program adds a watermark to an image.
import tkinter as tk
import tkinter.filedialog
from tkinter import *

from PIL import Image, ImageDraw, ImageFont, ImageTk

# Soure Directory where image is located
## May need to be changed depending on location of Picture Files
SOURCE_DIRECTORY = ("/Pictures")

DEFAULT_FILE_PATH = ("watermarker_default.PNG")

# Size of the label in tkinter
LABEL_SIZE = (300, 400)

# Build tkinter window
window = Tk()
window.title("Water Marker")
window.minsize(width=750, height=750)
window.config(padx=10, pady=20, background="white")

# Put default image into image label
default_watermarker_image = Image.open("watermarker_default.PNG")
default_watermarker_image = default_watermarker_image.resize(LABEL_SIZE)
default_watermarker_image = ImageTk.PhotoImage(default_watermarker_image)
image_label = tk.Label(image=default_watermarker_image)
image_label.image = default_watermarker_image
# Place default image label
image_label.place(x=100, y=0)

# Setup Default file path
file_path = ("watermarker_default.PNG")
image = default_watermarker_image

# Upload an image to watermarker and place image into label
def upload_image():
    global file_path, orig_width, orig_height
    # Open file explorer to display image
    file_path = tkinter.filedialog.askopenfilename(initialdir=SOURCE_DIRECTORY, filetypes=(("jpeg files", "*.jpg"), ("PNG files", "*.png*")))

    image = (Image.open(file_path))

    # Save original size of image
    orig_width, orig_height = image.size

    # resize image to fit into label
    label_fit_image = image.resize(LABEL_SIZE)

    # Convert to tkinter image
    label_picture = ImageTk.PhotoImage(label_fit_image)

    # Replace image label
    image_label.config(image=label_picture)
    image_label.image = label_picture


# Add watermark to image
def water_mark():
    global file_path, watermark_image
    image = (Image.open(file_path))
    # Copy the image
    copy_image = image.copy()
    copy_image = copy_image.convert("RGBA")
    # Get watermark String from input box
    string_to_watermark = watermarktext.get()
    # Create watermark text to add
    watermark_text = Image.new("RGBA", copy_image.size, color=(255,255,255,128))
    # Create a Draw object
    draw = ImageDraw.Draw(watermark_text)
    # Load a font
    font = ImageFont.truetype("times.ttf", 150)
    # Draw text to image. Text should be at half opacity
    draw.text((300,300), string_to_watermark, font=font, fill=(0,0,0,128))
    # Display image
    watermark_image = Image.alpha_composite(copy_image, watermark_text)
    watermark_image.show()

def download_image():
    image = watermark_image
    watermarked_image = image.resize((orig_width, orig_height))
    save_file_path = tkinter.filedialog.asksaveasfilename(defaultextension='png', filetypes=(("jpeg files", "*.jpg"), ("PNG files", "*.png*")))
    if save_file_path is not None:
        watermarked_image.save(fp = save_file_path)

# Check if water mark text is blank
def check_watermarktext(*args):
    if watermarktext.get().strip():
        watermark_button.config(state="normal")
        # if it is, disable watermark button
    else:
        watermark_button.config(state="disabled")

# Track watermark text box for text
entry_var = StringVar()
entry_var.trace_add("write", check_watermarktext)

# Create upload button
upload_button = Button(text="Upload", command=upload_image)
upload_button.place(x=100,y=550)

# Create watermark text box
watermarktext = Entry(width=20, bg="white", fg="black", textvariable=entry_var)
watermarktext.place(x=100,y=600)

# Create watermark button
watermark_button = Button(text="Watermark", command=water_mark, state="disabled")
watermark_button.place(x=100,y=500)

# Create download button
download_button = Button(text="Download", command=download_image)
download_button.place(x=300, y=500)

# Keep window open
window.mainloop()

