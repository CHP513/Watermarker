# Watermarker

This Python projects uses a simple GUI tool that allows you to upload an image, and add a custom water mark to it.  The custom water mark is made by taking an input text and then places it within the picture.  The watermarked picture can then be downloaded.  It uses 'tkinter' for the interface, and 'Pillow' for the Picture upload and the modification.


---

## ✨ Features
- Upload a picture (.jpg, .png).
- Resize and display picture in tkinter window.
- Takes Inputted Text in text box and puts it in the picture (watermark button will not work if text is not in entry box).
- Simple GUI built with **Tkinter**.

## 📦 Requirements
- Python 3.7+
- Libraries:
  - `tkinter` (bundled with Python)
  - ['Pillow'] (https://pillow.readthedocs.io/en/stable/)
 
Install dependencies with:
```bash
pip install PIL
```

---

## ▶️ GUI Usage
1. Clone or download this repository.
2. Run the program:
  ```bash
   python main.py
   ```
4. In the GUI:
   - Upload .jpg or .png image by clicking upload.
   - Enter text in input box.
   - Click **Watermark**.
   - Image with Watermark text is displayed.
   - Download watermarked image by clicking download.

## 📜 License
This project is open-source and available under the MIT License
